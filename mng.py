#!/usr/bin/python
# -*- coding: utf-8 -*-
import sqlite3 as lite

class principal():
    def __init__(self):
        self.banco = None
        try:
            self.banco = lite.connect('manut.db')
            self.cur = self.banco.cursor()
            self.cur.execute('SELECT SQLITE_VERSION()')
            self.data = self.cur.fetchone()
            print "SQLite version: %s" % self.data
        except lite.Error , e:
            print "Error %s:" % e.args[0]
            sys.exit(1)


    def cad(self):
        print "Script para cadastrar e deletar tarefas para rodarem nos Lab's no SO Ubuntu"
        self.n = raw_input('Escolha "c" para cadastrar uma tarefa e "d" para deletar\n')
        if self.n == "c":
            print "A pasta onde deve-se colocar o script é \n"
            self.sc_nome = raw_input('Digite nome do script: \n')
            self.ask =  raw_input('Para cadastrar o script para uma sala inteira digite "s", e para uma máquina digite "m":\n')
            print self.ask
            if self.ask == "s":
                self.sala = raw_input('Digite a sala, que pode ser lp01, lp02, lp03, lp09 e lp10\n')
                ss.cur.execute("insert into tarefas (id,script,host) select null, \""+self.sc_nome+"\", hosts.id from hosts where hosts.sala =\""+self.sala+"\"")
                self.rows = ss.cur.fetchall()
            elif self.ask == "m":
                self.machine = raw_input('Digite o IP da maquina\n')
                i = ss.cur.execute("select id from hosts where nome = \""+self.machine+"\"")
                self.rows = ss.cur.fetchall()
                for j in self.rows:
                    idd = j[0]
                    idd = str(idd)
                    print idd
                    ss.cur.execute("insert into tarefas (script,host) values (\""+self.sc_nome+"\",\""+idd+"\")")
                    ss.banco.commit()
            else:
                print "escolha errada"
        elif self.n == "d":
            self.ask =  raw_input('Para deletar o script para uma sala inteira digite "s", e para uma máquina digite "m":\n')
            if self.ask == "s":
                self.sala = raw_input('Digite a sala, que pode ser lp01, lp02, lp03, lp09 e lp10\n')
                ss.cur.execute("delete from tarefas where host in ( select t.host from tarefas t join hosts h on (t.host=h.id) where h.sala=\""+self.sala+"\" )")
                self.rows = ss.cur.fetchall()
            elif self.ask == "m":
                self.machine = raw_input('Digite a máquina para excluir o script\n')
                ss.cur.execute("delete from tarefas where host in ( select t.host from tarefas t join hosts h on (t.host=h.id) where h.nome=\""+self.machine+"\" )")
                self.rows = ss.cur.fetchall()
            else:
                print "escolha errada"

        else:
            print "escolha errada"
            

if __name__=='__main__':
    ss = principal()
    ss.cad() 
    ss.banco.commit()
