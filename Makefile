PELICAN=pelican

html:
	$(PELICAN) -s pelican.conf.py content

upload: html
	rsync -P -rvz --delete output/* artichaut:/home/www/blog.notmyidea.org

serve: html
	cd output && python -m pelican.server 8000&

regenerate: serve
	$(PELICAN) -r -s pelican.conf.py content
