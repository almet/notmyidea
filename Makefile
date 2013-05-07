nmi:
	BLOG_URL="http://blog.notmyidea.org" BLOG_NAME="Alexis' log" pelican -s pelican.conf.py content --output blog
pyc:
	BLOG_URL="http://alexis.notmyidea.org/pycon" BLOG_NAME="Pycon notes" pelican -s pelican.conf.py pycon --output pycon-output

build: nmi pyc

upload: build
	rsync -e "ssh -p 22" -P -rvz --delete output/* alexis@172.19.2.119:/home/www/notmyidea.org/blog
	rsync -e "ssh -p 22" -P -rvz --delete pycon/* alexis@172.19.2.119:/home/www/notmyidea.org/pycon-output
