
install:
	python3 -m venv .v
	.v/bin/pip install -r requirements.txt
	mkdir output

regenerate:
	.v/bin/pelican -lr

publish:
	.v/bin/pelican -s publishconf.py
	echo "blog.notmyidea.org" > output/CNAME
	.v/bin/ghp-import -n output
	git push origin gh-pages
