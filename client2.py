### BEGIN INIT INFO
# Provides:          scriptname
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO
import socket
import base64
import subprocess
import sys
import time

HOST = '143.106.243.209'              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
class start_server():
    def __init__(self):
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.orig = (HOST,PORT)
        self.tcp.connect(self.orig)

class autenticacao():
    def __init__(self):
        self.user='info'
        self.passwd='mnd'
    def auth(self):
        self.token=base64.encodestring('%s:%s' % (self.user,self.passwd))
        #ss.tcp.send('login')
        self.login = ss.tcp.recv(8192)
        if self.token == self.login:
            print "autenticacao ok"
            ss.tcp.send('ok')
        
        else:
            print "autenticacao falhou"
            ss.tcp.send('err')
            sys.exit()

class recebe():
    def __init__(self):
        pass
    def recebe_script(self):
        self.arq = open('/root/manut/script.sh', 'w')
        while 1:
            self.dados = ss.tcp.recv(1024)
            if not self.dados:
                break
            self.arq.write(self.dados)
        self.arq.close()
        ss.tcp.close()
        self.bashcmd="/root/manut/script.sh"
        subprocess.call(self.bashcmd, shell=True)

class verifica():
    def __init__(self):
        pass
    def tem_script(self):
        self.arq2 = open('/root/manut/status', 'r')
        status = int(self.arq2.read())
        self.arq2.close()
        print status
        if status == 1:
            self.bashcmd="/root/manut/script.sh"
            subprocess.call(self.bashcmd, shell=True)
        r = recebe()
        r.recebe_script()


if __name__=='__main__':
    ss=start_server()
    b=autenticacao()
    b.auth()
    v=verifica()
    v.tem_script()
