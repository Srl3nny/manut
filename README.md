# manut
Script em python para fazer manutenções automáticas em máquinas com Linux:
É possível adicionar scripts e dizer se será executado em uma determinada sala ou máquinas.

Script feito com base na versão cliente servidor Sockets.

Para usar altere as variáveis do I.P do servidor, crie a pasta onde ficará o script python e coloque ele na inicialização do Linux.

No meu caso foi:

#mkdir /opt/manut

#touch /opt/manut/script.sh

#chmod 750 /opt/manut/script.sh /opt/manut/client.py
 
Copiei o arquivo manut.sh na pasta /etc/init.d

#chmod 750 /etc/init.d/manut.sh

#update-rc.d manut.sh defaults

