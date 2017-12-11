#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import thread
import sqlite3
DIR = '/tmp/manut/'
HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

def conectado(con, cliente):
	print 'Iniciando o banco SQLITE'
	banco = sqlite3.connect('manut.db')
	cursor = banco.cursor()
	cursor.execute('SELECT SQLITE_VERSION()')
	data = cursor.fetchone()
	print 'Versao do banco %s' % data
	print 'Conectado por', cliente
	print 'Endereco: ', cliente[0].strip()
	cursor.execute("select t.script from tarefas t join hosts h on (t.host=h.id) and h.nome=\""+cliente[0].strip()+"\"")
	rows = cursor.fetchall()
	for i in rows:
            	nm = i[0]
            	arq = open(DIR+i[0], 'r')
             	for j in arq.readlines():
              		con.send(j)
  	cursor.execute("delete from tarefas where host in ( select t.host from tarefas t join hosts h on (t.host=h.id) where h.nome=\""+cliente[0].strip()+"\")")
 	banco.commit()
    
	print 'Finalizando conexao do cliente', cliente
	con.close()
	thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()
banco.close()