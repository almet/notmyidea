---
title: dangerzone
save_as: dangerzone/index.html
template: worklog-en
---

## Lundi 27 Mai 2024 ()

- Created PGP keys for `alexis@freedom.press` and setup github to work with it.

## Vendredi 24 Mai 2024 (5h, 5/5)

- Completed the Sexual Harassment NYC training, and forms. I was pretty surprised by the (good) quality of it, actually.
- Reviewed alex.p PR on the gVisor design document.
- Read the currently opened pull requests.
- build: bumped the minimum python version to 3.9 (in a PR)

## Jeudi 23 Mai 2024 (8h, 5/5)

- Read on how Dangerzone is currently being integrated in the tails docs, yay!
- Synced this morning with Alex, and discussed about how containerization works, and what's the difference between OSes.
- Split my "small changes" pull request in two parts, with minor changes on one side, and changes on how test fixtures are run on the other side.
- Spent some time with Alex understanding why the tests weren't working anymore, and we found that the current tests weren't using the proper fixtures. That was fun and instructive: I'm happy to have a better understanding of how the test suite works, and interacts with QT apps.
- Read the gVisor documentation Alex wrote. Learned about secomp filters.
- Started using the devscripts to install the different environments locally, and started to install a X11 server on OSX to have the application show up... to be continued tomorrow.

## Mercredi 22 Mai 2024 (8h, 5/5)

What I did today (a lot of reading, some meetings):

- Read a bunch of issues to better understand the packaging status of dangerzone. Notes for myself:
	- [Debian discussion](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=986856#29), how it works [on arch](), the goal to [have a small image for tails](https://github.com/freedomofpress/dangerzone/issues/669) (and in general, I guess)
	- The [Python Packaging User Guide](https://packaging.python.org), I was looking for resources on how to package on different targets, but didn't encounter this.
- Read the documentation of [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/installation.html), and [the presentation](https://github.com/freedomofpress/dangerzone/files/13821818/Considering.PyMuPDF-1.pdf) that was made for DangerZone (found out about [dangerzone-test-set](https://github.com/freedomofpress/dangerzone-test-set))
- Read on the difference between podman and Docker, I'm still lagging on this front, as I'm not a user myself.
- Read the different Pull Requests on the repository to get a grasp of what is currently going on. (I learned about MacOS [entitlements](https://developer.apple.com/documentation/bundleresources/entitlements) and more specifically [App Sandbox](https://developer.apple.com/documentation/security/app_sandbox))
- Read the [security audit](https://freedom.press/news/dangerzone-receives-favorable-audit/) for dangerzone (and the OWASP [Docker security cheatsheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html) that was linked there)
- Looked at the dangerzone redesign documents from superbloom, both for the application and for the website. Nice work :-)
- Read the current code and made [a PR with minor changes](https://github.com/freedomofpress/dangerzone/pull/811), and currently trying to setup my machine to work the same way Circle CI does.
- Did the security 101 presentation with Davis and David
- Welcome meeting with Erik, Harris and Alex.p


## Mardi 21 Mai 2024 (9h, 5/5)

- I'm looking at the current codebase and current infrastructure. I'm installing a development environment locally (using `uv`)
- I'm discovering how everything is structured. I find out about [yum-tools-prod](https://github.com/freedomofpress/yum-tools-prod) and [apt-tools-prod](https://github.com/freedomofpress/apt-tools-prod)
- I'm reading the [Code of Conduct](https://github.com/freedomofpress/.github/blob/main/CODE_OF_CONDUCT.md). It's nice to see this is though of, and well phrased.
- I'm reading the [meeting notes](https://github.com/freedomofpress/dangerzone/wiki/Meeting-Notes) and clicked on some issues to see what's worked-on at the moment ([Explore how to Simplify Save Options · Issue #427 · freedomofpress/dangerzone · GitHub](https://github.com/freedomofpress/dangerzone/issues/427))
- 
