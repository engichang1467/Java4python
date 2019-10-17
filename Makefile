all: gitInit

gitInit:
	git init
	git add .
	git commit -m "give what I have"
	git remote add origin git@github.com:engichang1467/Java4python.git
	git remote -v
	git push -u origin master