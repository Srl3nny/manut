import sqlite3 as lite
sqlite_file = '/home/bruno/MEOCloud/python/manut/manut.sql'
###arquivo onde sera salvo o Banco de Dados
try:
	con = lite.connect(sqlite_file)
	print("conectado")
	print("Criando tabela hosts:")
	cursor = con.cursor()

	cursor.execute("""
		CREATE TABLE hosts(
		id INTEGER PRIMARY KEY,
		nome VARCHAR(15),
		sala VARCHAR(15)
		);
		""")
	print("Tabela hosts Criada com sucesso!")

	cursor.execute("""
		CREATE TABLE tarefas(
		id INTEGER PRIMARY KEY,
		script VARCHAR(15),
		host INTEGER,
		FOREIGN KEY(host) REFERENCES hosts(id)
		);
		""")
	print("Tabela tarefas Criada com sucesso!")
	con.close()	

except Exception, e:
	print("Erro na criacao do banco")
   
