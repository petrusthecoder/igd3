import os

# FUNÇÕES GLOBAIS

def linux_or_win():
	quest = input("Está rodando esse software em um terminal Linux?")
	if (quest == "s"):
		pacotes = ["git", "nodejs"]
		pacotes_size=len(pacotes)
		loop = 0
		while (loop < pacotes_size):
			key = False
			while (key == False):
				print("Essa aplicação depende do pacote "+ pacotes[loop] +" para funcionar corretamente.")
				ask = input("Deseja instalá-lo agora?->")	
				if (ask == "s"):
					os.system("sudo apt-get install "+ pacotes[loop])
					key = True
					loop += 1
				elif (ask == "n"):
					print(pacotes[loop] + " não será instalado.")
					key = True
					loop += 1
				else:
					print("Responda apenas 's' ou 'n'!")
	elif (quest == "n"):
		minimal = """
----------------IGD3 FOR WINDOWS-------------------------

	Requisitos Mínimos
	Copie e Cole os seguintes links em seu browser
		para instalar os pacotes necessários!

	(*) Git: (  https://git-scm.com/download/win  )
	(*) Node.js: (  https://nodejs.org/en/  )

---------------------------------------------------------
		"""
		print(minimal)
	else:
		print("Responda apenas 's' ou 'n'!")

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
		print("Iniciando um novo repositório git...")
		os.system("git init")
		print("Configurando as informações do autor...")
		os.system('git config user.name "'+ user +'"')
		os.system('git config user.email "'+ mail +'"')
		clone = input("Link do repositório remoto (origin)->")
		os.system("git remote add origin "+ clone)
		
		ask = input("Deseja subir a versão para o repositório remoto agora? ->")
		if (ask == "s"):
			print("Stageando alterações...")
			os.system("git add .")
			print("")
			print("Efetuando commit local...")
			os.system('git commit -m "Initial Commit With IGD3 <3"')
			print("")
			print("Fazendo upload para repositório remoto...")
			os.system('git push origin master')
			print("")
		elif (ask == "n"):
			print("Repositório remoto não atualizado!")
			print("")
		else:
			print("Responda apenas 's' ou 'n'!")
			print("")
	def git_commit():
		msg = input("o que foi alterado nessa versão? -> ")
		print("")
		os.system("git add .")
		print("")
		print("Efetuando commit local...")
		os.system('git commit -m "'+ msg +' (IGD3 Bot Commit)"')
		print("")
		print("Commitado!")
		print("")
	# Listeners Tree
	while (True):
		git_c = input(user + "-> ")
		if (git_c == "branch"):
			run_branch()
		if (git_c == "igd"):
			run_igd()
		if (git_c == "hello git"):
			hello_git()
		if (git_c == "commit"):
			git_commit()


print("---------IGD3 v.1.0.0----------")
print("Automatize Já!")
print("Desenvolvido por Petrus Rennan")
print("-------------------------------")
while (True):
	ask = input("Já possui conta?")
	if (ask == "s"):
		user = "Visitante"
		mail = "email@padrao.com.br"
		passw = "root"
		session_start()
	elif (ask == "n"):
		warning = """

----CADASTRO----------------------------------------------------------

É essencial que você forneça seus dados pessoais para nosso algoritmo,
com eles iremos automatizar taarefas chatas como por exemplo cadastros
de configs locais no git, ou registro de informações autorais em .json.

----------------------------------------------------------------------


		"""
		linux_or_win()
		print(warning)
		user = input("Digite seu nome: ")
		mail = input("Digite seu e-mail: ")
		key = False
		while (key == False):
			passw = input("Digite uma senha bem forte: ")
			confirm_p = input("Confirme sua senha: ")
			if(passw == confirm_p):
				print("Usuário cadastrado no banco de dados!")
				session_start()
			else:
				print("As senhas não conferem!")
				key = False
		
	
	else:
		print("Responda apenas 's' ou 'n'!")