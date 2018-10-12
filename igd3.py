from callback import *
import os
def ask_bin_treat(ask, case_yes, case_no):
	if (ask == "s"):
		case_yes
	elif (ask == "n"):
		case_no
	else:
		print("Responda apenas 's' ou 'n'!")

def linux_or_win():
	quest = input("Está rodando esse software em um terminal Linux?")
	if (quest == "s"):
		pacotes = ["git", "npm"]
		pacotes_size=len(pacotes)
		loop = 0
		while (loop < pacotes_size):
			print("Essa aplicação depende do pacote "+ pacotes[loop] +" para funcionar corretamente.")
			you_have=input("Deseja instalá-lo agora?->")
			case_yes = os.system("apt-get install "+ pacotes[loop])
			case_no = print(pacotes[loop] + " não será instalado.")
			ask_bin_treat(you_have, case_yes, case_no)

def session_start():
	def run_branch():
		branch_name = input("Nome da branch ->")
		os.system("git branch " + branch_name )
	def run_igd():
		console = ["npm init -y",
		"npm install --save-dev gulp",
		"npm install --save-dev gulp-sass", 
		"npm install --save-dev gulp-rename", 
		"npm install --save-dev gulp-minify",
		"npm install --save-dev gulp-watch",
		"npm install --save-dev gulp.spritesmith",
		"npm install --save-dev gulp-imagemin",
		"npm install --save-dev gulp-changed",
		"npm install --save-dev browser-sync",
		"gulp"]
		quant = len(console)
		loop = 0
		while(loop < quant):
			os.system(console[loop])
			loop += 1
	def hello_git():
		print("Iniciando um repositório git...")
		os.system("git init")
		print("Configurando as informações do autor...")
		os.system('git config user.name "'+ user +'"')
		os.system('git config user.email "'+ mail +'"')
		clone = input("Digite o link do git clone->")
		os.system("git remote add origin "+ clone)
		
		ask = input("Deseja stagear? ->")
		case_yes = os.system("git add .")
		case_no = print("Repositório não será commitado!")
		ask_bin_treat(ask, case_yes, case_no)

		ask = input("Deseja commitar? ->")
		case_yes = os.system('git commit -m "Bot Commit IGD3 <3"')
		case_no = print("Repositório não será commitado!")
		ask_bin_treat(ask, case_yes, case_no)


	# Listeners Tree
	while (True):
		git_c = input(user + "-> ")
		if (git_c == "branch"):
			run_branch()
		if (git_c == "igd"):
			run_igd()
		if (git_c == "hello git"):
			hello_git()


print("---------IGD3 v.1.0.0----------")
print("Automatize Já!")
print("Desenvolvido por Petrus Rennan")
print("-------------------------------")
linux_or_win()
while (True):
	ask = input("Já possui conta?")
	if (ask == "s"):
		while (user != "Petrus"):
			user = input("Login: ")
			if (user == "Petrus"):
				while(passw != "qweasd"):
					passw = input("Password: ")
					if (passw =="qweasd"):
						print("Bem vindo, " + user + "!")
						session_start()
					else:
						print("A senha está incorreta")
			else:
				print("O usuário não existe.")
		
	elif (ask== "n"):
		warning = """

----CADASTRO----------------------------------------------------------

É essencial que você forneça seus dados pessoais para nosso algoritmo,
com eles iremos automatizar taarefas chatas como por exemplo cadastros
de configs locais no git, ou registro de informações autorais em .json.

----------------------------------------------------------------------


		"""
		print(warning)
		user = input("Digite seu nome: ")
		mail = input("Digite seu e-mail: ")
		passw = input("Digite uma senha bem forte: ")
		confirm_p = input("Confirme sua senha: ")
		if(passw == confirm_p):
			print("Usuário cadastrado no banco de dados!")
			session_start()

	else:
		print("Responda apenas 's' ou 'n'!")