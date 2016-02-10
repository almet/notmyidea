PELICAN=pelican

build:
	$(PELICAN) -s pelican.conf.py content

upload: build
	rsync -P -rvz --delete output/* artichaut:/home/www/blog.notmyidea.org

serve: build
	 cd output && python -m pelican.server 8000
