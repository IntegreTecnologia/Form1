import sqlite3
import json
import requests
import pprint

from replit import db


connection = sqlite3.connect("integre")

#connection.execute("CREATE TABLE IF NOT EXISTS tabNFSe (id INTEGER PRIMARY KEY, tomador STRING, valor STRING);")

#connection.execute("INSERT INTO tabNFSe (id,tomador,valor) VALUES (1, 'Steve Biko','150')")

# Read
#cursor_object = connection.execute("SELECT * FROM tabNFSe") 
#print(cursor_object.fetchall())

#connection.execute("CREATE TABLE IF NOT EXISTS servico (id varchar(3), data json)")



#connection.execute("INSERT INTO servico values (?, ?)", [2, json.dumps(strJson)])

#cursor_object = connection.execute("select json_extract(data, '$.nome') from servico")
#cursor_object = connection.execute("select * from servico")
#print(cursor_object.fetchall())

countries_api_res = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
countries = countries_api_res.json()[1]
#pprint.pprint(countries[1])

connection.execute("CREATE TABLE IF NOT EXISTS countries (id INTEGER PRIMARY KEY, nfse json)")

#for country in countries:
#  connection.execute("insert into countries values (?, ?)",
#  [country['id'], json.dumps(country)])
#  connection.commit()
#connection.close()

cursor_object =   connection.execute("select json_extract(data, '$.name') from countries");
print(cursor_object.fetchall())

connection.execute("CREATE TABLE IF NOT EXISTS tabnfse (id varchar(3), data json)")
notas = {"nnf":"126","demiss":"05/02/2023","tomador":"noleto"},{"nnf":"546","demiss":"08/02/2023","tomador":"vieira"}
nfses = json.dumps(notas)
pprint.pprint(notas[1]["nnf"])

for nota in notas:
  connection.execute("insert into tabnfse values (?, ?)",
  [nota["nnf"], json.dumps(nota)])
  connection.commit()
connection.close()

connection = sqlite3.connect("integre")
cursor_object =   connection.execute("select json_extract(data, '$.demiss') from tabnfse");
print(cursor_object.fetchone())

# Commit changes
#connection.commit()

# Close the connection
connection.close()


db["bd1"] = 'integre'

db["tomador"] = {'nome':'noleto','cpf':'526528','valor':'100.00','itens':[{'coditem':'1','descricao':'bola'},{'coditem':'2','descricao':'meia'}]}

db["tomador"] = {'nome':'vieira','cpf':'528401','valor':'350.00','itens':[{'coditem':'3','descricao':'arroz'},{'coditem':'4','descricao':'feijão'}]}