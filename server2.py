#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import os
import sys
import sqlite3 as lite
import base64

class start_server():
    def inicia_bd(self):
        self.banco = None
        try:
        
            self.banco = lite.connect('/root/manut/manut.sql')
            self.cur = self.banco.cursor()    
            self.cur.execute('SELECT SQLITE_VERSION()')
            self.data = self.cur.fetchone()
            print "SQLite version: %s" % self.data 
        except lite.Error , e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
    def inicia_socket(self):
        self.PORT = 5000
        self.HOST = ''
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.orig = (self.HOST, self.PORT)
        self.tcp.bind(self.orig)
        self.tcp.listen(1)

class autentica():
    def __init__(self):
        self.user='info'
        self.passwd='mnd'
    def auth(self):
        self.token=base64.encodestring('%s:%s' % (self.user,self.passwd))
        con.send(self.token)
        self.sinal = con.recv(8192)
        if self.sinal == 'ok':
            print 'ok'
        else:
            print "autenticacao falhou"
            sys.exit()
class enviar():
    def envia(self):
        ss.cur.execute("select t.script from tarefas t join hosts h on (t.host=h.id) and h.nome=\""+cliente[0].strip()+"\"")
        self.rows = ss.cur.fetchall()
        for i in self.rows:
            self.nm = i[0]
            self.arq = open('/root/manut/'+i[0], 'r')
            for j in self.arq.readlines():
                con.send(j)
                self.arq.close()
class apagar():
    def apaga(self):
        ss.cur.execute("delete from tarefas where host in ( select t.host from tarefas t join hosts h on (t.host=h.id) where h.nome=\""+cliente[0].strip()+"\")")
        ss.banco.commit()

        
if __name__=='__main__':
    ss = start_server()
    ss.inicia_bd()
    ss.inicia_socket()
    while True:
        con, cliente = ss.tcp.accept()
        pid = os.fork()
        if pid == 0:
            ss.tcp.close()
            print 'Conectado por', cliente[0]
            print "'",cliente[0].strip(),"'"
            #dado = con.recv(8192)
            #print dado+'eeee'
            aut = autentica()
            aut.auth() 
            env = enviar()
            env.envia()
            print "apagando tarefa"
            ap = apagar()
            ap.apaga()
            print "tarefa apagada"
        else:
            con.close()
        print 'Finalizando conexao do cliente', cliente
        con.close()
    banco.close()
