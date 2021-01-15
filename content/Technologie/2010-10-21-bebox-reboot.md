# How to reboot your bebox using the CLI


I've an internet connection which, for some obscure reasons, tend to be
very slow from time to time. After rebooting the box (yes, that's a hard
solution), all the things seems to go fine again.

## EDIT : Using grep

After a bit of reflexion, that's also really easy to do using directly
the command line tools curl, grep and tail (but really harder to
read).

```bash

curl -X POST -u joel:joel http://bebox.config/cgi/b/info/restart/\?be\=0\&l0\=1\&l1\=0\&tid\=RESTART -d "0=17&2=`curl -u joel:joel http://bebox.config/cgi/b/info/restart/\?be\=0\&l0\=1\&l1\=0\&tid\=RESTART | grep -o "name='2' value='[0-9]\+" | grep -o "[0-9]\+" | tail -n 1`&1"
```

## The Python version

Well, that's not the optimal solution, that's a bit "gruik", but it
works.

```python

import urllib2
import urlparse
import re
import argparse

REBOOT_URL = '/b/info/restart/?be=0&l0=1&l1=0&tid=RESTART'
BOX_URL = 'http://bebox.config/cgi'

def open_url(url, username, password):
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, url, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)

    opener = urllib2.build_opener(authhandler)

    urllib2.install_opener(opener)

    return urllib2.urlopen(url).read()

def reboot(url, username, password):
    data = open_url(url, username, password)
    token = re.findall("name\=\\'2\\' value=\\'([0-9]+)\\'", data)[1]
    urllib2.urlopen(urllib2.Request(url=url, data='0=17&2=%s&1' % token))

if __file__ == '__main__':
    parser = argparse.ArgumentParser(description="""Reboot your bebox !""")

    parser.add_argument(dest='user', help='username')
    parser.add_argument(dest='password', help='password')
    parser.add_argument(boxurl='boxurl', default=BOX_URL, help='Base box url.  Default is %s' % BOX_URL)

    args = parser.parse_args()
    url = urlparse.urljoin(args.boxurl, REBOOT_URL)
    reboot(url, args.username, args.password)
```
