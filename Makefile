build:
	pelican -s pelican.conf.py .
upload: build
	scp -rP 20004 output/* alexis@notmyidea.org:/usr/local/www/notmyidea.org/blog
	curl http://notmyidea.org/reload
