---
title: dangerzone
save_as: dangerzone/index.html
template: worklog-en
---


## Mardi 24 Décembre 2024 (6h, 3/5)

The release

## Lundi 23 Décembre 2024 (4h, 3/5)

Found a security issue in Dangerzone via our security scans, we published a new
0.8.1 release. At the wrong time, but we've managed to keep things fast, and
release in one day where in the past we had to take way longer for this.

## Jeudi 19 Décembre 2024 (7h, 5/5)

- Moving our packages pyproject.toml to the new PEP 508 format, and use `uv` on it. Not completely there yet, but it's able to install and build, I'm expecting to hit some issues with packaging on macOS, windows and Linux, so that's the missing step right now.
- Discussing with Alex on ICU, trying to understand some of the missing pieces. It's not completely clear clear, but it's better than before. Bundles everywhere!
- Meeting with A_lex, A_da and G_iulio on ICU, it was very interesting to have their point of view and general "approval"
- Quick 1:1 with Alex, wrapping up for the year.

## Mercredi 18 Décembre 2024 (7h, 4/5)

- Quick sync with a_pyrgio
- Quick pairing session on blocked tests and blocked io for stderr
- Two PRs about these two, one for a `--debug` flag that can get debug information from gVisor, and the other one about checking Docker Desktop version.
## Mardi 17 Décembre 2024 (6h, 5/5)

- Opened issues about Independent Container Updates in our repository, summarizing where we are at, proposed a meeting with A_da and G_iulio about it. [Here is the main issue, if you want to follow along](https://github.com/freedomofpress/dangerzone/issues/1006)
- 1:1 with Harris
- Tour of the open PRs, merging what could be. (We now have ruff support!)

## Lundi 16 Décembre 2024 (8h, 5/5)

- Sync point with Alex this morning, where we discussed the overall state of ICU (Idependent Container Updates)
- Some more discussions about sigstore. Agreed upon the signing and attestation story about Sigstore
- Started porting our packaging to the PEP 508, as a first step to replace `poetry` with `uv`. Will continue tomorrow.
## Jeudi 12 Décembre 2024 (6h, 3/5)

Continued looking at the documentation for sigstore in order to have a better understanding of how it works, with the goal in mind to be able to generate Sigstore's bundles attached to container registries myself, without having to use GH Actions (that will prove useful when building the images on our own infra). 

We synced with Alex, as we're getting both pieces of the overall context that's needed to understand how it works. I've been able to create attestations locally and add them to a container registry, but cosign follows its own signing scheme (when attaching the info to the container registries), rather than following sigstore's bundles. It's about the same place as yesterday, but with better understanding of how things work.

Updated the ruff PR, waiting for the CI to be green before merging.
## Mercredi 11 Décembre 2024 (9h, 4/5)

Trying to have image verification working for both GHA attestations and signature done via the cosign client.  
It turns out that there are differences between signing / verifying container images and doing the same with attestations.Mainly, this means reading documentation around sigstore, the different specs and trying to get the whole picture. Not there yet, but making progress !

## Mardi 10 Décembre 2024 (4h, 5/5)

- Had a quick look at how python-sigstore is organised, to see if it would be possible to use our own certificate to verify sigstore bundles.
- Documented the HTTP requests and Accept headers needed to interact with the container registry in order to get the attestations / bundles to verify.
- Final review of the work by Alex on image references and using pydoit to paralellize the generation of the release assets.
- 1:1 with Harris
- Started using cosign (rather than a Github Action) to create attestations

## Lundi 09 Décembre 2024 (9h, 4/5)

- We synced this morning with Alex, focusing on what's next for the Independent container update effort.
- We discussed quickly about [an exploit](https://github.com/ultralytics/ultralytics/issues/18027) that was used to poison the Github actions cache. Interesting because we're on the verge of trusting Github at some point for our build process, so this gives us some more weight to wait on this until we reach reproducibility.
- I did another round of reviews (ruff integration from an external contributor, the change of how we refer to our images, integration of pydoit to help the release process)
- Integrated a few comments from H_arris in the blog platform, which is now able to detect the last published version from the posts metadata.
- Consolidated our findings from last week in [a script able to get the attestation from the container registry](https://gist.github.com/almet/de10e2b258df5a666c94fbb91be7e315#file-registry_client-py-L8) with python and requests.

## Jeudi 05 Décembre 2024 (7h, 4/5)

Discussions and implementation around Independent Container Updates with Alex, find a way to do the HTTP calls ourselves rather than relying on an external tool to interact with the container registry.
Team meeting, with E_than around :slightly_smiling_face:

## Mercredi 04 Décembre 2024 (7h, 4/5)

No notes taken

## Mardi 03 Décembre 2024 (8h, 4/5)

- Finally understood why Podman Desktop wasn't working as a drop-in replacement for Docker Desktop on macOS, as it was not mounting the volumes properly.
- Reviewed Alex's work where image IDs are changing from IDs to tags.
- 1:1 discussion with Harris
- Some discussion with Giulio about Webcat, to get some more understanding around the project
- Continuation of the work checking the Podman Desktop version and displaying a warning to the users when that happens.

## Lundi 02 Décembre 2024 (7h, 4/5)

- Sync with Alex
- Some more research on ICU (Indep. Container Updates)
- Progress on checking the version of Docker Desktop and mentionning it to the user
- Review of ruff format / lint as a replacement to black / isort

## Jeudi 28 Novembre 2024 (7h, 5/5)

- [An exploration](https://freedomofpress.slack.com/archives/C03FVBEFA86/p1732807630508179?thread_ts=1732525206.464909&cid=C03FVBEFA86) on signing container images and verifying them
- The beginning of adding checks for minimum Docker Desktop version on macOS and Windows
- Some discussion with Tails devs to see if they would like to give us a hand on Debian integration
- Listening to [Bonobo's Animal Magic album](https://www.youtube.com/watch?v=clsczmHXf9U). It's still magic.
## Mercredi 27 Novembre 2024 (7h, 4/5)

- Looking at the needed changes to bump our runners to `ubuntu-24`
- Finish a PR for the Dangerzone.rocks website, making it find the latest released version automatically and generate links for the releases automatically
- Started playing with independent container updates: created a GH action to release container images, generate, sign with cosign and upload to the ghcr. Currently the digests generated on the runner differ from the ones of the container registry, and that's where I left it.
- Took some time to organize the project issues and fit them in the next `0.9.0` release

## Mardi 26 Novembre 2024 (7h, 4/5)

- Checked the situation of the VFS driver on Debian, to see if we are missing something.
- Updated the release instructions so they're clearer and easier to reproduce
- Updated `apt-tools-prod` to use podman rather than docker, since that's what we're now using
- Proposed a change to the issue templates so the docker/podman info is included more often
- Update all the PRs that were pending and getting a bit out of date
- Applied changes to the "check changelog entry" PR, which should make it easier to populate changelog with each PR.
- Merged the "drop fedora 39 support" PR
- Removed the container scan on mac silicon for now, since it's not working well
- Investigated a bit on this subject to understand why colima isn't able to run on our silicon mac runners.

Mainly tidying and some post 0.8.0 stuff. Tomorrow I want to change the way we generate the release notes on the blog (it's still missing one small thing).

## Lundi 25 Novembre 2024 (5h, 4/5)

- Refining a bit the proposal about independent container updates;
- Meeting with Alex, synchronizing, talking about general directions for the project, redefining a bit how we organize during our syncs
- Had a look at the FOSDEM devrooms to see where it would make more sense to answer an RFP
- Organizing myself for the rest of the week, the goal being to finish post 0.8.0 pending tasks
- Debug macOS runners not doing parameter expansion the same way as other shells, and also trying to install docker on the macOS runners to do some more CI there.

## Jeudi 21 Novembre 2024 (7h, 2/5)

- Merged a few more post-release fixes
- Discussed with Alexis about independent container updates, how we can use Sigstore. Probably we will reach to our security experts within FPF with more questions.
- Dangerzone biweekly meeting, where we met Leila!
## Mercredi 20 Novembre 2024 (7h, 3/5)

-   Rebased and merged a few PR that were waiting for me: [https://github.com/freedomofpress/dangerzone/pull/975](https://github.com/freedomofpress/dangerzone/pull/975), [https://github.com/freedomofpress/dangerzone/pull/961](https://github.com/freedomofpress/dangerzone/pull/961) [https://github.com/freedomofpress/dangerzone/pull/994](https://github.com/freedomofpress/dangerzone/pull/994) [https://github.com/freedomofpress/dangerzone/pull/959](https://github.com/freedomofpress/dangerzone/pull/959)
- Reviewed some work by Alex, his document on GH merge queues
- We had a meeting on this. It looks promising, and we need to decide on our trust model on GH
## Mardi 19 Novembre 2024 (7h, 3/5)

- Sync up with Alex on what happened last week while I was out
- Reviewing all notifications and acting on them.
- Updated PRs, reviewed some that were pending, and trying to get everything that's in the pipes closer to the exit side.
- All-staff meeting, with a dropping connection just when I needed it ![:wink:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/google-medium/1f609@2x.png)

## Lundi 11 Novembre 2024 (3h, 5/5)

Created a stats dashboard for dangerzone.

# Jeudi 07 Novembre 2024 (7h, 4/5)

Post release stuff.

## Mercredi 06 Novembre 2024 (7h, 4/5)

We released DZ 0.8.0, after fixing some issues with it, rebuilt the container image and the .deb files, signed and published everything.

I've started doing some post-release tasks, which should help us in the long run.
## Mardi 05 Novembre 2024 (7h, 4/5)

- We really close to releasing Dangerzone 0.8.0. We have built and pushed all the required artifacts, and sent a PR for our website.
- .... but we are investigating a last minute issue with old Podman versions
- 1:1 with Harris
- 1:1 with Erik

It was a bit hard to continue facing problems when we wanted to "just release", and that really build a motivation for me to streamline the whole process.

## Lundi 04 Novembre 2024 (7h, 3/5)

Today was mostly release-related: Sync with Alex + Preparation of the release, hit again some "out of space" issues, but we're almost there.

## Jeudi 31 Octobre 2024 (8h, 4/5)

Today was mainly some QA on different platforms, testing that the next 0.8.0 release works on Ubuntu, Silicon macOS. I've hit a few issues down the road, the mac mini was full and I didn't figured why it wasn't working out directly.

My general feeling is that it takes too much time on repetitive tasks. I would like to find ways to streamline the whole process.

Then, the DZ Biweekly meeting. I have a feeling that things aren't really smooth between Alex and I, and I would like to ensure that 

## Mercredi 30 Octobre 2024 (4h, 3/5)

- Prepared the CHANGELOG
- Reviewed some PRs by a_pyrgio
- Started QA on Debian and derivatives

## Mardi 29 Octobre 2024 (9h, 5/5)

- Sync with Alex about the upcoming 0.8.0 release
- Updated the deprecation warning message for ubuntu focal users
- Wrote release notes + a small script to gather them.
- Found out via user feedback that our CI isn't actually running the produced .exe files on windows. Trying to update the CI accordingly.
- Started to have a look at how to "attest" our artifacts on Github, using sigstore.

## Lundi 28 Octobre 2024 (11h, 5/5)

- Catchup on last week work
- Adding a deprecation warning for Ubuntu Focal users, asking them to upgrade their system to continue using Dangerzone
- Continue research on independent container updates.
- Removed the duplication of the action runs on the Github CI. We now only run on PRs
- Publish artifacts built in the CI (.msi, .app, .deb and .rpms). Not signed for now.

## Jeudi 17 Octobre 2024 (9h, 4/5)

Merge-day :-)

- We finally merged the on-host conversion PR! Nice work by A_pyrgio. Happy to have it incorporated in time for the 0.8.0 release in the next few weeks: https://github.com/freedomofpress/dangerzone/pull/748
- Automating the closing of stale issues with the needs info tag after some inactivity: https://github.com/freedomofpress/dangerzone/pull/955
- Rebased and merged a PR catching installation errors (and other podman/docker errors) and displaying them in the UI to help gather feedback from users when things go wrong: https://github.com/freedomofpress/dangerzone/pull/952
- Small reviews: https://github.com/freedomofpress/dangerzone/pull/958.
- Rebased the PR adding a --debug flag to dangerzone-cli. Running with gVisor in debug mode seem to block, not sure if it's related to the on-host conversion or some work I did in there. Will investigate later on.



## Mercredi 16 Octobre 2024 (6h, 4/5)

- Sync with Alex
- Published the Ubuntu 24.10 package
- Continued exploring the possibilities for signing container images. The fact we're using podman and/or docker on different platforms doesn't make it easy, as the two have different ways to sign / verify.

## Mardi 15 Octobre 2024 (6h, 5/5)

- Reviewed PRs for F41 and Ubuntu 24.10 support
- Changed the approach to testing the container installation failures. It's more reliable now and easier to think about. Submitted a PR for it.
- Proposed a change to close automatically stale issues with a specific `need-info` tag

## Lundi 14 Octobre 2024 (9h, 3/5)

We've started with a sync point with Alex, where we discussed the next items on the table. We found out that there are new releases out for Fedora 41 and Ubuntu 24.10, and they will need to be supported on the next 0.8.0 release.

As spinoffs of this discussion, I've had a look at how distrowatch could provide us RSS feeds for when new beta/RC releases are out, but the feeds doesn't seem to be that customisable, unfortunately. 

I also created an issue about moving from argparse to click and from urllib to requests, as it seem it will allow for more uniformisation.

I've had a look at all the open issues. I wanted to do it for quite some time but never manage to find the time. It's good to now see what are a few blind spots, and seeing that the whole project can fit in my head.

Also built the package for ubuntu 24.10, and updated our CI to reflect this. Unfortunately it's not currently working (that's expected).

Summary:

- Sync with Alex on the tasks on the table + a few discussion points.
- Built a .deb file for ubuntu 24.10, to find out it's not working out of the box.
- Started having a look at why it's failing, and updating our CI to test for this platform.
- Had a look at all the issues in the repo. I wanted to do this since quite some time. Happy to see it fits in my head nicely, made a few comments on my way.
- Pushed a PR for #193 (Error detection and display)


## Jeudi 10 Octobre 2024 (9h, 5/5)

I continued to work on adding tests for the container installation failure, and it turns out I want to do it in two ways: 1) check that errors are displayed when `.install()` returns `False` or raises an exception and 2) check that return values are what they should be.

Then, we debugged why colima isn't working on MacOS, and it turns out to be apparmor-related. We found out that dangerzone was working with an older colima version, where the VM was using alpine, and not ubuntu, so no apparmor in there. We proposed a solution to the user. It was a productive session.

We continued discussing a bit with Alex on different matters, and one of them was about how to use the python's `logging` utility while in the imports. We finally decided the added complexity to handle this right wasn't worth the added value of it.

I also attended Giulio "braindump" session, where he explained how TUF and Sigstore work. My takeaway is that TUF can be seen as a kind of framework to decide how to validate new certs, and how to make it possible for the end users to have some sort of canary: if there are no updates, there is a problem somehow.

Sigstore is basically a way to a) have a proof that you are the owner of a {Google, Github} account, issuing certificates for this and b) sign and publish information related to artifacts you want to publish. There is an observatory inside it, to publish what's going on, following the same principles as Google CT for TLS certificates.

## Mercredi 09 Octobre 2024 (8h, 5/5)

I've reviewed the work done by Alex on the on host conversion, which spawned some interesting discussions about how to deal with our scripts generally speaking, covered by [#946](https://github.com/freedomofpress/dangerzone/issues/946) . I tested the branch locally on a M1 mac and it works well 🎉

I've updated the Github issue templates with the review, and we should be good soon there.

Also, I spent some time mocking `subprocess.Popen`, to finally use `pytest-mockpopen` which does the heavy lifting for us (it's not working with the `unittest.mock` out of the box, unfortunately).

I sent and merged a quick PR replacing `set-output` by environment variables in our CI.

## Mardi 08 Octobre 2024 (6h, 5/5)

I started writing tests for the branch which checks the image installation. It seems that the best way forward will be to `@mock.patch` the calls to docker/podman, to see if the errors are displayed. I'm not really sure if I should consider this a unit test or a functional test (probably both ? 🤔).

What I want to test is:

- Are the logs generated by the calls to docker / podman present ?
- When clicking on retry, do the messages go away ?

I also started writing a blueprint of how the independent container updates might work, and what are the problems this will solve. I've started creating an API, but I stopped in the middle of it, wondering if it could make sense to use signing mechanisms from the registries, rather than doing it ourselves.

It's possible to do so [on podman at least](https://github.com/containers/podman/blob/main/docs/tutorials/image_signing.md) ([another link](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/building_running_and_managing_containers/assembly_signing-container-images_building-running-and-managing-containers#proc_signing-container-images-with-gpg-signatures_assembly_signing-container-images)), but it requires some control on the receiving machine, which we might not have. See this: 

```
$ cat /etc/containers/policy.json
{
  ...
  "transports": {
    "docker": {
      "<registry>/<namespace>": [
        {
          "type": "signedBy",
          "keyType": "GPGKeys",
          "keyPath": "<path>/key.gpg"
        }
      ]
    }
  }
}
```

[Skopeo](https://github.com/containers/skopeo) is a tool to transport the containers from one machine to another, so it's something we might want to use, but it's not installable on windows unfortunately.

Started reviewing the onhost conversion PR Alex proposed. Will resume tomorrow on this.

## Lundi 07 Octobre 2024 (6h, 5/5)

-  Sync with Alex
- Another pass on the GH issue templates, to have issue templates for different OSes
- Reviews on different changes proposes by Alex
- Added a `--debug` flag to the dangerzone-cli to help getting more logs when needed
- Some more debugging on the colima support issue

## Jeudi 03 Octobre 2024 (6h, 5/5)

- Github issue templates
- Error handling during the container installation phase

## Mercredi 02 Octobre 2024 (7h, 4/5)

- Sync with Alex about what goes in 0.8.0
- Merged the migration to Github Actions
- Did some reviewing on the preparation of the on host conversion PR
- Team meeting !

## Mardi 01 Octobre 2024 (7h, 4/5)

- Release of the DZ 0.7.1 hotfix release, announcements etc. with Alex!
- Attended Trevor's brownbag presentation on the history of FPF
- Updated the "move to GHA" branch

## Lundi 30 Septembre 2024 (8h, 4/5)

- Sync with @a_pyrgio about last week
- Review the 0.7.1 hotfix, updated commits, and created assets via our mac minis (.dmg for silicon, .deb and fedora 39,40 rpms). Tested the hotfix on an Apple M1 machine, it works.
- Updated the "migrate to CI branch" according to @a_pyrgio comments

## Jeudi 19 Septembre 2024 (8h, 4/5)

- Some debugging on colima, gVisor is not able to run there (yet)
- Proposed a fix to use our seccomp policy for all container techs, which makes Orbstack work
- Tried Podman Desktop on OSX, and with a few changes on the detection side, it works.
- Short appointment with G_race
- Added the current date in the hash of the dz dev containers
- Had a quick look at the CSS for the DZ blogpost
- 1:1 with Harris
- DZ team meeting
## Mercredi 18 Septembre 2024 (8h, 4/5)

- Merged #906 - Fix wrong container runtime detection on Linux
- Changed the caching strategy for the Github actions, now we have a `build-dev --sync` flag to pull / build / push to the ghcr if needed, the PR is now ready for review
- Started looking back at how to make colima work on OSX, currently failing due to compatibility issues with gVisor wanting to write to /tmp

## Mardi 17 Septembre 2024 (8h, 4/5)

- Continued working on the migration to Github Actions, it's now working, probably some polishing tomorrow. Build times are down to 9mn!
- Read some user research about DZ
- Minor changes to the PR to show an error to the end users when there is a containerd misconfiguration.

## Lundi 16 Septembre 2024 (8h, 3/5)

- Continued the migration to Github Actions, now using the GHCR and more caching.
- Sync with Alex and plan for the rest of the week
- Debugging on some issues opened by end users

## Jeudi 12 Septembre 2024 (8h, 4/5)

- I did work on migrating our CI to Github (from CircleCI), and spent some time changing what's being cached. It still needs some more work, probably will happen next week.
- Did some review of the tasks in the next milestone, took the opportunity to close some issues in the repo.
## Mercredi 11 Septembre 2024 (5h, 5/5)

- Updated the "remove stdeb" branch and merged it https://github.com/freedomofpress/dangerzone/pull/901
- Updated the runtime detection and error displaying PR https://github.com/freedomofpress/dangerzone/pull/906

## Mardi 10 Septembre 2024 (7h, 5/5)

- Proofread the gVisor x Dangerzone article, did some editing and changes to the overall diagram.
- Changed the architecture to "any" for the debian packages
- Merged various PRs, now that the CI is green again (https://github.com/freedomofpress/dangerzone/pull/905, https://github.com/freedomofpress/dangerzone/pull/902, https://github.com/freedomofpress/dangerzone/pull/915, https://github.com/freedomofpress/dangerzone/pull/904)
- 1:1 with Harris
## Lundi 09 Septembre 2024 (8h, 5/5)

- Quick tour of the 0.8.0 issues, comments when appropriate to move the items forward;
- Follow-up on the libexpat CVE that we detected this weekend and that G iulio had a look at (thanks again)
- Sync w/ Alex on what are the next steps
- Debugging session with Alex to find out why our CI was failing on CircleCI runners. Turns out to be a problem with the AWS patched kernel (or maybe something that changed in Linux 5.x), anyway updating the runners was the solution. It kept us wondering for a few hours.
## Vendredi 06 Septembre 2024 (8h, 5/5)

- Doing another pass the the pull requests on the repo, updating them wrt to comments and new findings after a fresh read ;
- Pushed some changes on the branch which removes stdeb in favor of more modern debian packaging tools ;
- Opened a few issues as follow ups
- Finding that there actually is a tool to [automate migrating from circle CI to github actions](https://docs.github.com/en/actions/migrating-to-github-actions/using-github-actions-importer-to-automate-migrations/migrating-from-circleci-with-github-actions-importer), gave it a try.
## Jeudi 05 Septembre 2024 (8h, 5/5)

- Updated multiple PRs following Alex's review  
- In depth discussion about how to handle CVEs in the future, and how to ship separated container updates in the future  
- Started moving the dev_scripts data out of dz git repository  
- Updated the debian packaging branch with recent developments.  
- DZ Biweekly meeting (thanks again G_iulio for joining) (edited)

## Mercredi 04 Septembre 2024 (4h, 4/5)

- 1:1 w/ Erik
- Discussion about how we should handle CVEs with Alex
- Getting some more understanding of Debian packaging, more specifically on how to make it skip some specific folders

## Mardi 03 Septembre 2024 (5h, 3/5)

- Debian packaging, answering to various issues.

## Lundi 02 Septembre 2024 (7h, 4/5)

- Sync point with Alex where we covered a wide range of topics (on-host conversion, security and docker images distribution, how should we organize ourselves?)
- Discussion about how dangerzone can be used with colima
- Minor changes to the my PR fixing how the runtime is detected on Linux
- Currently ~~fighting with~~ working on using Github Workflow / Actions rather than Circle CI.
## Vendredi 30 Août 2024 (4h, 5/5)

- Some discussion with the securedrop team about how to integrate with DZ in order to print images.
- Fixed the wrong container runtime detection on Linux, displaying the error log inside dangerzone, see https://github.com/freedomofpress/dangerzone/pull/906

## Jeudi 29 Août 2024 (6h, 5/5)

- Research and discussions about java CVEs
- [PR](https://github.com/freedomofpress/dangerzone/pull/905) fixing exceptions getting thrown when encountering invalid desktop entries
- Started looking at [212](https://github.com/freedomofpress/dangerzone/issues/212) - wrong container runtime detection on linux

## Mercredi 28 Août 2024 (5h, 5/5)

- PR on the removal of stdeb in favor of dpkg-buildpackage : https://github.com/freedomofpress/dangerzone/pull/901
- PR for updating our container image build process when installing PyMuPDF musl wheels, which aren't provided for ARM : https://github.com/freedomofpress/dangerzone/pull/902
- Checked tests are passing for Fedora 40 (everything seems fine), since they fail on the CI
- 
## Mardi 27 Août 2024 (6h, 4/5)

- Read about Debian packaging to get a better understand of how things work, and started removing `stdeb` in favor of more vanilla debian packaging. (Got some help from Kunal along the way, thanks!)
- Started investigating why the CI is currently failing for Fedora 40.
- Attended the all-staff meeting

## Lundi 26 Août 2024 (10h, 3/5)

- Catchup on Slack / GH issues and docs that were written when I was away.
- Read and added small comments to the gVisor article to come on the blog
- Ran the security scan on our latest image and dig a bit on some CVEs
- Trying to understand why `.deb` packages aren't building for trixie see [Pull Request #900](https://github.com/freedomofpress/dangerzone/pull/900)

## Jeudi 11 Juillet 2024 (5h, 5/5)

- Update the `RELEASE.md` file with notes taken during the release
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
