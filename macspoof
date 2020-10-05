arp -a | grep wlan1 | grep -o -E '([[:xdigit:]]{1,2}:){3}[[:xdigit:]]{1,2}' > mac
awk '{ printf "sudo macchanger -m "; printf $1; printf ":"; printf int(rand()*(10-19))+20; printf ":"; printf int(rand()*(10-19))+20; printf " "; printf "wlan0" }' mac > output
cat output
sudo chmod +x output
sh output
