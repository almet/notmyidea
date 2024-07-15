---
title: dangerzone
save_as: dangerzone/index.html
template: worklog-en
---

## Jeudi 11 Juillet 2024 (5h, 5/5)

- Update the REALEASE.md file with notes taken during the release
- Check how to run Dangerzone with Colima / explore the situation and give feedback to a user trying to make things work
- DZ biweekly meeting

## Mercredi 10 Juillet 2024 (8h, 5/5)

- We released 0.7.0, finally :-)

## Mardi 09 Juillet 2024 (8h, 5/5)

- Rebuilt all the Linux targeted distributions for the 0.7.0 release with the latest fixes, updated the pull requests on {apt,yum}-tools-prod repositories.
- Some poking around with L_ee to ensure the Windows virtualbox machine has access to the SmartCard.
- Rebuilt the Windows .msi
- Started thinking about what could be automated in our setup

## Lundi 08 Juillet 2024 (8h, 5/5)

- Sync up with a_pyrgio on the next steps for the release (when the mac mini will be back again).
- Documented myself on certificate transparency, and on how / if we should put trust in the Github releases pages for Dangerzone. I started an issue about that on the DZ repository.
- Discussed a bit with A_da about how the infra is setup and how we should use github PAT
- Read a bit about the latest SSL exploit, I didn't realized it was that problematic.

## Mardi 02 Juillet 2024 (6h, 5/5)

- 0.7.0 is almost there. Everything is signed and ready. Let's wait the green lights.
  
  We finished the last steps for the release. Building and signing everything, by pairing together most of the day with Alex_P.
- I now know how to juggle with three different keyboard layouts !

## Lundi 01 Juillet 2024 (6h, 5/5)

- QA on my windows machine, and then
- Hopping to the windows VM to do the build and sign. Session with Alex_P where we did some debugging
- Reviewed a PR about adding timeouts on kill commands

## Jeudi 27 Juin 2024 (8h, 5/5)

- Today way mostly QAing for the 0.7.0 release, which is lining up.
- And we merged the drag-n-drop feature!
- Biweekly meeting, we discussed about how to deal with security problems when maintainers aren't around, and what's next for the redesign :-)

## Mercredi 26 Juin 2024 (6h, 4/5)

- Understanding how the mac minis are working, starting drafting a release there ;
- Reviewing Alex_P PR about using custom seccomp profiles on some specific Docker Desktop versions (see above)
- Started bumping python to 3.12 for Windows and macOS buildd, finding some bumps in the road.


## Mardi 25 Juin 2024 (8h, 5/5)

- Sync with AlexP on the upcoming 0.7.0 release
- Debugged a seccomp filter related bug with runc old versions on silicon mac + Docker Desktop w/ AlexP
- Started drafting a solution for it
- Changelog-related discussions
- Attended the XZ postmortem meeting

## Jeudi 20 Juin 2024 (8h, 5/5)

- Started the 0.7.0 release
	- Updated dependencies
	- Removed support for Fedora 38
	- Started writing the CHANGELOG
- Synced w/ Alex
## Mercredi 19 Juin 2024 (8h, 4/5)

- Merged the two PRs for testing packages for fedora and debian
- Found out an issue with line endings on windows, when building the docker image
- 1:1 Discussion with M_icah
- Got access to the release machines, and found some way to circumvent the network at my workplace being tempered.

## Mardi 18 Juin 2024 (7h, 5/5)

- Fixing the CI for .deb testing
- Installing a windows machine to check current work on drag-n-drop there
- Started working on a PR for CI checking fedora packages

## Vendredi 14 Juin 2024 (6h, 4/5)

- Added CI for testing the built debian images are working properly. 
- Some more work on the drag-n-drop feature, it's now passing the CI tests and is working everywhere I tried.
## Jeudi 13 Juin 2024 (8h, 5/5)

- Extended session with w/ Alex where we prepared the next 0.7.0 release, trying to see how much effort each task would be.
- Made some minor changes to the drag-n-drop PR
- Follow-up discussion on an external contributor PR
- Merged rowen's PR, thanks!
- Biweekly dangerzone meeting, where we decided what'll go in the next release

## Mercredi 12 Juin 2024 (12h, 5/5)

- Read the Drag-n-drop PR (#752)and rebased it on latest main branch
- Viewed Ron Deibert's / The Citizen Lab presentation
- Prepared the work for tomorrow "sprint planning", by reading the issues that will probably go into it
- Reviewed [Illegal chars filenames - Pull Request #834](https://github.com/freedomofpress/dangerzone/pull/834)
- Installed the new machine (on arch in the end, I wanted to use ubuntu at first, but was discouraged by a few errors I couldn't debug easily)

Tomorrow looks like:

- Sprint planning
- Read about alternatives to Docker Desktop on macOS and windows.

## Mardi 11 Juin 2024 (7h, 5/5)

- Sync w/ Alex in the morning
- Described my plans for the Docker Desktop version check and user notification, followed up with some research on how the retrieved version is stored locally. I which this Docker Desktop was opensource to know where to look at.
- Tried reproducing the CI errors locally on the PR rowen did, pushed a small fix (actually a revert from previous changes) on how the tests are run.
- Proofread the work on gVisor and gVisor design docs another time

Tomorrow will be:

- Trying locally the drag-n-drop feature, reading the changes, rebasing and trying to make it trough.
- Installing the Framework laptop I received today (to replace my Silicon m1 as a development machine).
- Mapping the space of Docker Desktop alternatives on macOS.


## Jeudi 06 Juin 2024 (8h, 5/5)

- Sync w/Alex, and planned what's next
- Started writing a mechanism to check Docker Desktop updates (for Windows and MacOS), including some fun setting up mitm-proxy to reverse-engineer it)
- Discussed gVisor specifics w/Alex, and provided feedback on the presentation
- 1:1 with Harris
- Attended the gVisor presentation, with lots of interesting questions :-)

## Mercredi 05 Juin 2024 (6h, 5/5)

- Installed `lima` and `colima` to try to circumvent the "podman in docker" limitation with Apple Silicon. Coming to the same conclusion: it doesn't work, unfortunately. Stated a discussion with podman folks. Let's see where it goes.
- [Landed some "minor changes"](https://github.com/freedomofpress/dangerzone/pull/811) removing dead code, imports, and fixing some minor concerns in the code.
- [Landed a PR](https://github.com/freedomofpress/dangerzone/pull/813) where we change the way fixtures are loaded by pytest, and fixes some tests. This makes it possible to run all tests in the same process, and removes the need for spawning multiple `pytest` commands.
- Started looking at the "on host conversion" PR.

## Mardi 04 Juin 2024 (8h, 2/5)

- Syncing w/ Alex this morning
- Pairing on a debugging session w/ Alex
- Found out that pymupdf changed their package name from `fitz`to `pymupdf`, which is why the CI wasn't happy
- Finished the PR on python version update

## Jeudi 30 Mai 2024 (8h, 4/5)

- Reproducing the currently failing CI issues locally and finding out that it might be related to the way the inner image current state, as it seems to not contain the pymupdf python module.
- 1:1 with Harris
- Dangerzone biweekly meeting w/ erik, alex and harris.

## Mercredi 28 Mai 2024 (9h, 5/5)

- While trying to install the `rpm` files generated by a_rpygio, I finally found out that the silicon m1 machine I'm using isn't fit for the job, as it's currently hitting some bugs when running "podman in docker", with rosetta enabled on the host. I created an issue on the repository about this: https://github.com/freedomofpress/dangerzone/issues/824
- I've switched to my linux amd64 machine, and was able to install the dangerzone dev environment there, and test that the rpms are working great. I've validated the pending pull request by a_rpygio accordingly.
- I'm currently following-up on the python 3.9 version bump, as the produced `.deb` packages don't seem to work properly. I'm currently trying to reproduce the issue locally, with the hopes of fixing it tomorrow.


## Mardi 28 Mai 2024 (6h, 5/5)

- Learned how Debian python packaging works, and specifics of how `stdeb` does it.
- Reviewed PRs by AlexP about 
	- A 1:1 with AlexP where we discussed both the release process for fedora and debian packages, what are the specificities on how we're doing the signing etc.
- Took another approach for supporting the latest pyside6 version on debian + from sources.
- Started testing the new `rpms` that were uploaded by AlexP. Been caught on the silicon architecture differences, and started making changes in the current scripts for it to work.

## Lundi 27 Mai 2024 (7h, 4/5)

- Created PGP keys for `alexis@freedom.press` and setup github to work with it.
- Synced 1:1 with AlexP
- Got a better understanding of how containers work on different OSes, what's the role of hyperkit, etc.
- Triggered Debian builds on my machine, and continued the deep dive in Debian packages and stdeb to fix #780 (to have pyside6 newer versions work on our releases).

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
