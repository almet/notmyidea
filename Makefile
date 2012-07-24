build:
	pelican -s pelican.conf.py .
upload: build
	rsync -e "ssh -p 22" -P -rvz --delete output/* alexis@fileS.lolnet.lan:/home/www/notmyidea.org/blog
