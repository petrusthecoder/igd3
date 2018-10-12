def session_start():
	def run_branch():
		branch_name = input("Nome da branch ->")
		os.system("git branch " + branch_name )
	def run_igd():
		arquivo = open("igd2.bat", "w")
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
		see = console[5]
		print(see)
		loop = 0
		while(loop < quant):
			os.system(console[loop])
			loop += 1
	while (True):
		git_c = input("-> ")
		if (git_c == "branch"):
			run_branch()
		if (git_c == "igd"):
			run_igd()
