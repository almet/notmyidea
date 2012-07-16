build:
	pelican -s pelican.conf.py .
upload: build
	scp -r output/* alexis@files.lolnet.lan:/home/www/notmyidea.org/blog
