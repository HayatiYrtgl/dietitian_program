import sqlite3 as sql
import json
from tkinter import messagebox as msg

cursor = None
db = None

# get connection
def get_connection():
	global db, cursor
	
	# create db
	db = sql.connect("dbs/my_database.db")
	
	# create cursor
	cursor = db.cursor()

# create table
def create_table():
	
	#  get connection
	get_connection()	
	
	# command
	command = """CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, name string, surname string, username string, password string, gmailkey string, age string, gender string) """
	
	# execute command
	cursor.execute(command)
	
	# commit
	db.commit()
	
	# close
	db.close()
	
# register sql function
def register_sql_command(name, surname, username, password, gmailkey, age, gender):
	
	# get connection
	get_connection()
	
	# create querry function to register
	def querry_function(username):
		
		# querry
		command = "SELECT * FROM users WHERE username=?"
		
		querry = cursor.execute(command, (username,))
		
		querry = querry.fetchone()
		
		# if user is already exists deny to accessability
		if querry is True:
			
			# deny
			return False
		
		else:
			
			return True
	
	# run the querry function
	access = querry_function(username)
	
	# if user is not exists insert to table
	if access:
		
		# password length, alphanumeric control
		if len(password) >= 8 and password.alphanumeric():
			
			# command
			command = "INSERT INTO users(name, surname, username, password, gmailkey, age, gender) VALUES (?,?,?,?,?,?,?)"
		
			# execute
			cursor.execute(command, (name, surname, username, password, gmailkey, age, gender))
		
			# commit the db
			db.commit()
		
			# close the db
			db.close()
		
			# write to jsonfile
			create_json_profile(name, surname, username, password, gmailkey, age, gender)
		
			# give message
			msg.showinfo("BİLGİ", f"MERHABA {name}, PROGRAMA KAYDINIZ TAMAMLANMIŞTIR...\nLÜTFEN GİRİŞ YAPINIZ")
			
		
		else:
			
			msg.showwarning("UYARI", "ŞİFRE 8 HANEDEN UZUN VE HAR VE SAYI İÇERMELİDİR")
	
	else:
		
		msg.showerror("HATA", "KULLANICI ZATEN VAR!!")
		
# create json profile
def create_json_profile(name, surname, username, password, gmailkey, age, gender):
	
	my_profile = {"isim": name, "soyisim": surname, "şifre": password, "username": username, "gmailkey": gmailkey, "age": age, "gender":gender}
	
	# open json file
	with open("profiles/profile.json", "w", encoding="utf-8") as profile:
		
		json.dump(my_profile, profile, ensure_ascii=False,indent=4)
		
# login
def login(username, password):
	
	# get connection
	get_connection()
	
	# command 
	command = """SELECT password FROM users WHERE username=? """
	
	querry = cursor.execute(command, (username,))
	
	querry = querry.fetchone()
	
	# password querry
	if password == querry[0]:
		
		msg.showinfo("Bilgi", "HOŞGELDİNİZ")
		
		# return value
		return 1
	else:
		
		msg.showerror("HATA", "ŞİFRE YALIŞ")
	
		return 0
