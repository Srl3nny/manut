#!/bin/bash
mkdir /root/manut
cd /root/manut
touch status 
touch script.sh
wget http://cluster.ft.unicamp.br/pop/client2.py
wget http://cluster.ft.unicamp.br/pop/client.py
cp client.py /etc/init.d
chmod 755 /etc/init.d/client.py
chmod 755 /root/manut/client2.py
chmod 755 /root/manut/script.sh
echo "1" > /root/manut/status
update-rc.d client.py defaults 
