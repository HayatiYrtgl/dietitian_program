import tkinter as tk
import sqlite3 as sql
from tkinter import messagebox


# class for login page
class LoginPage(tk.Tk):
	
	# override
	def __init__(self):
		super().__init__()
		
		# main settings of login page
		self.title("Login Page")
		self.geometry("970x800+500+100")
		
		# main label
		self.main_label = tk.Label(self, text="LOGIN PAGE", font=("Times New Roman", 25), fg="green4")
		
		self.main_label.grid(row=0, column=1, sticky="w")
		
		# user name and assword section
		self.user_name_label = tk.Label(self, text="User Name :", font=("Times New Roman", 15), fg="brown")
		
		self.user_name_label.grid(row=1, column=0, sticky="w", padx=10, pady=20)
		
		# password
		self.password_label_section = tk.Label(self, text="Password :", font=("Times New Roman", 15), fg="brown")
		
		self.password_label_section.grid(row=2, column=0, sticky="w", padx=10, pady=20)
		
		# entries
		self.username_entry = tk.Entry(width=30)
		
		self.username_entry.grid(row=1, column=1, sticky="w", padx=10, pady=20)
		
		# entries
		self.password_entry = tk.Entry(width=30, show="*")
		
		self.password_entry.grid(row=2, column=1, sticky="w", padx=10, pady=20)
		
		# button 1 create new user
		self.new_user_button = tk.Button(self, text="Create new user", fg="blue2", bg="snow1", command=self.create_new_user)
		
		self.new_user_button.grid(row=3, column=0, sticky="w", padx=10, pady=150)
		
		# button2 login
		self.login_button = tk.Button(self, text="Login", fg="black", bg="green2", width=15, command=self.login)
		
		self.login_button.grid(row=3, column=1, sticky="e", padx=10, pady=150)
		
		# show password
		self.show_pw_button = tk.Button(self, text="(:)", command=self.show_password)
		
		self.show_pw_button.grid(row=2, column=2, sticky="w")
		
	
	# command Section
	# show password 
	def show_password(self):
		
		# get situation
		stiuation = self.password_entry['show']
		
		# decision maker
		if str(stiuation) == "*":
	
			self.password_entry['show'] = ""
			
		else:
			
			self.password_entry['show'] = '*'
			
	# login command
	def login(self):
		
		# get varaibles
		username = self.username_entry.get()
		
		# password
		password = self.password_entry.get()
		
		# sql function will be here
		messagebox.showinfo("info", [username, password])
	
	# create new user function
	def create_new_user(self):
		
		# destroy the app
		self.destroy()
		
		# create new app
		new_app = CreateUser()
		new_app.mainloop()
		

# class for creatng user
class CreateUser(tk.Tk):
		
		#  const and override
		def __init__(self):
			super().__init__()
			
			# const vars
			self.geometry("800x800+500+100")
			self.title("create user")
			
			# main label
			self.main_label = tk.Label(self, text="Create User", font=("Times New Roman", 20), fg="brown4")
			self.main_label.grid(row=0, column=0)
			
			# entries
			self.name = tk.Entry(width=20)
			self.name.insert("0", "İsim")
			self.name.grid(row=1, column=0, sticky="w", padx=10, pady=20)
			
			# surname
			self.surname = tk.Entry(width=20)
			self.surname.insert(tk.END, "Soyisim")
			self.surname.grid(row=1, column=1, sticky="w", padx=10, pady=20)
		
			# username
			self.username = tk.Entry(width=20)
			self.username.insert(tk.END, "Gmail")
			self.username.grid(row=2, column=0, sticky="w", padx=10, pady=20)
			
			# password
			self.password = tk.Entry(width=20)
			self.password.insert(tk.END, "Şifre")
			self.password.grid(row=2, column=1, sticky="w", padx=10, pady=20)
			
			# yaş
			self.age = tk.Entry(width=20)
			self.age.insert(tk.END, "Yaş")
			self.age.grid(row=3, column=0, padx=10, pady=20, sticky="w")
			
			# gender
			options = ["Erkek", "Kadın", "Belirtmek İstemiyorum"]
			str_var = tk.StringVar()
			str_var.set("--")
			self.gender = tk.OptionMenu(self, str_var, *options)
			self.gender.grid(row=3, column=1, padx=10, pady=20, sticky="w")
			
			# gmail key
			self.gmail_key = tk.Entry(width=20)
			self.gmail_key.insert(tk.END, "Gmail_key-https://security.google.com/settings/security/apppasswords")
			self.gmail_key.grid(row=4, column=0, padx=10, pady=20, sticky="w")
			
			# goto login page
			self.goto_login = tk.Button(self, text="Giriş Yap", fg="black", bg="yellow", command=self.goto_login_page)
			self.goto_login.grid(row=5, column=0, sticky="w", padx=10, pady=20)
			
			# register button
			self.register_button = tk.Button(self, text="Kayıt Ol!", fg="black", bg="green2")
			self.register_button.grid(row=5, column=1, sticky="w", padx=10, pady=20)
			
		# goto login page funcion
		def goto_login_page(self):
		
			# destroy the current page
			self.destroy()
		
			# create new page
			new_app = LoginPage()
			new_app.mainloop()
		
		# register function sql will be here
		


app = CreateUser()
app.mainloop()