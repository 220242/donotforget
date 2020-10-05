#!/bin/bash
#sudo crontab -e
#*/1 * * * * /home/pi/reconnect.sh
router=`ip route | awk '/default/ {print $3}'`
/bin/ping -q -c5 1.1.1.1 > /dev/null

if [ $? -eq  0 ]
then
  true
  echo "Network OK"
else
  echo "Network down, fixing..."
  # ifdown --force wlan1
  # sleep 5
        #  /bin/kill -9 `pidof wpa_supplicant`
        #  /sbin/ifup --force wlan1
        #  /sbin/ip route add default via $router dev wlan0
        #  /bin/mount -a
        sudo ifconfig wlan1 down
        sudo macchanger -r wlan1
        sudo ifconfig wlan1 up
        curl --header 'Content-Type: application/json' --request 'POST' --data '{"chat_id":"**UserID**","text":"wlan1 reconnected"}' "https://api.telegram.org/bot**api**/sendMessage"
fi
