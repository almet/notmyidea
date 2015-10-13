PELICAN=pelican

build:
	$(PELICAN) -s pelican.conf.py content

upload: build
	rsync -e "ssh -p 22" -P -rvz --delete output/* files:/home/www/notmyidea.org/blog

serve: build
	 cd output && python -m pelican.server 8000
