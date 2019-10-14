echo -e "\033  \e[31m[+] \e[32mUpdating/Preparing - \e[36mPython3-Chatterbot-Discord On Debian 10!\e[0m " && sleep 3
echo ""
echo ""
echo ""
apt -y upgrade
apt install -y python3-pip
apt install build-essential libssl-dev libffi-dev python3-dev
echo ""
echo ""
echo ""
echo -e "\033[  \e[31m[+] \e[32mInstalling - \e[36mChatterBot/Discord...\e[0m " && sleep 3
echo ""
echo ""
echo ""
pip3 install ChatterBot && pip3 install discord
echo ""
echo ""
echo ""
echo -e "\033[ \e[31m[+] \e[32mInstalling - \e[36mDirectory...\e[0m " && sleep 3
echo ""
echo ""
echo ""
apt install screen
mkdir ~/ChatterBot/
mv ~/chatterbot-discord-master/ima_bot.py ~/ChatterBot/ima_bot.py
mv ~/chatterbot-discord-master/token.txt ~/ChatterBot/token.txt
cd ~/ChatterBot/ && chmod 777 *
echo ""
echo ""
echo -e "\033[ \e[31m[+] - \e[32mInstallation Complete! \e[36m Enter Bot's Filename > ima_bot < [w/o .py] When Prompted! Make Sure Its In The Directory :) \e[0m "
echo "" 
echo ""
read -p "Enter Your Filename: "  botname
echo ""
echo ""
echo -e "\033[ \e[31m[+] - \e[32mOk! \e[36m Starting Discord $botname ... \e[0m " && sleep 3
echo ""
echo ""
echo -e "\033[ \e[31m[+] - \e[32m Be Sure To Hit \e[1;33m CTRL + A + D In About 15 Seconds \e[36m To Detach From Screen!!! \e[0m " && sleep 3
screen python3.6 ~/ChatterBot/$botname


