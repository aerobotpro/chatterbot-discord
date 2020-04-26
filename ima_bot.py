#!/usr/bin/python3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime
import discord

config = list(open("config.ini", "r").read().split())
token = config[1]
dataset = config[8]

rich_presence = "this server, waiting for conversation."

client = discord.Client()
chatbot = ChatBot(dataset)
            
class log:
    def log(thing):
        with open("log.txt", "a") as myfile:
            time = str(datetime.now())
            thing = str(thing)
            myfile.write(f"\n[{time}]\n{thing}")
        return 0
    
@client.event
async def on_ready():
    log.log('')
    print('-\n[Ok] - Succesfully logged in as {0.user}'.format(client))
    activity = discord.Activity(name=rich_presence, type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
        if message.content:
            parsed = message.content.replace('^', '').replace('\\', '').replace("*",'').replace("#", '').replace("<", '').replace(">", '').replace("@",'').replace("ツ",'').replace("0",'').replace("1",'').replace("2",'').replace("3",'').replace("4",'').replace("5",'').replace("6",'').replace("7",'').replace("8",'').replace("9",'')#pruning/parsing our input
            try:
                with open("dialog.dat", "a", encoding="utf8") as a: a.write(f'{parsed}\n')       
            except Exception as f1:
                log.log("Failed to write user dialog to memory!\n"+str(f1))
                await message.channel.send(f"Sorry, I've lost our conversation :(\n```yaml\nError Flag 1:\n{str(f1)}\n```")
                bError = True
                pass
            if bError == False:
                try:
                    async with message.channel.typing():
                        response = str(chatbot.get_response(parsed)) #Grabbing a response then sending it back
                        await message.channel.send(f"<@{str(message.author.id)}> {response}")
                except Exception as f2:
                    log.log("Response failed!\n "+str(f2))
                    await message.channel.send(f"Sorry, I've failed to come up with a response :(\n```yaml\nError Flag 2:\n{str(f2)}\n```")
 

client.run(token)

