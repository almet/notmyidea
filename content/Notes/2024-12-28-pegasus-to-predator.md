---
title: From Pegasus to Predator
speaker: Matthias Frielingsdorf
tags: 38c3, iOS, spyware
---
*These are notes taken during and after the 38C3 conference in Hambourg. Notes might be a bit sketchy at times*

Subtitle: the evolution of Commercial Spyware on iOS

<iframe width="1024" height="576" src="https://media.ccc.de/v/38c3-from-pegasus-to-predator-the-evolution-of-commercial-spyware-on-ios/oembed" frameborder="0" allowfullscreen></iframe>

A talk by a researcher on how exploits are being used on iOS devices over time. He is the VP of research at [iVerify](https://iverify.io/).

He is offering an overview of the evolution on the field of malwares for iOS in the past years.

## History of commercial spyware

It's covering offensive capabilities provided by companies for nation states to infect individuals.

It's clear by now that this use is not for terrorism detection, because we've seen it being used against journalists and activists.

Unfortunately, their detection is non trivial on iOS. There are cases of jounalists that were killed after such infections

### Pegasus

2016: Pegasus. It was detected after a jounalist sent the SMS to Citizen Lab, and they were able to analyse and reveal it. It was pretty amateurish. Pretty easy to detect.

2021: Pegasus was a lot more advanced. The exploit is pretty famous. Google project Zero blogpost. Zero click attack. With iCloud account or phone number. There is nothing the user can stop. It was very public, a lot of organisations talked about it. Amnesty research on the topic is very good.

The main change is the move to zero click attack, because it is invisible. 1-click attacks need to use persistence to continue, 0-click attacks leaves a lot less traces, because a reboot removes the attack, but it can be applied again.

In 2021 they were hiding (launch from a specific `/private/var/db/com.apple.xpc.roleaccountd.staging`), and they were disguising as normal system processes.

So it looks like pegasus is a normal process, so it's harder to find.

2023 Pegasus Blastpass exploit

2019: A campagin against Uyghures (Ouïghours) / I-SOON. 14 individual exploits. The target was in Nepal, they were transmitting the details in plain text (so anybody looking at the network could see it)

2022, Hermit: Google TAG unveiled this, It was targeting Kazakhstan and Italy, This was using a side-loaded App as a vector.

2023: Last year, by Kasperky ([see talk at 37C3](https://media.ccc.de/v/37c3-11859-operation_triangulation_what_you_get_when_attack_iphones_of_researchers)). The infection vector was iMessage. The interesting case here is that it started with malicious domains. Backup Agent is not used in recent versions of iOS, so it's possible to detect.

In terms of cleanup, they were taking a lot of steps to avoid being found.

2021 Predator, infection vector by Webkit. uncovered by Citizen Lab, Google Tag and Cisco Talos.

2023: Predator v2: Webkit via O-click. Targets the EU commission, the former MP of egypt. Here in this version they were checking for additional root certificates authorities and check if developer mode is enabled, to hide even more. They were also checking for log monitoring, and checked running processes from `/private/var/tmp` to not do anything if specific processes were running.

2024: NoClip. Unveiled by Google TAG. Using Webkit as an infection vector.  There is even a function named `pwnCitizenLab` in there. It's deleting all crashlogs, delete unified logs, delete aggregates and clean the application state.

[!Comparison table](comparison-table.png)

## How to detect commercial spyware

It's possible to run a Desktop Application, and if you trust the app you can get crash logs, get a list of apps, get transport traffic intercetion.

- [MVT](mvt.re) is a tool to analyze backups, a project done by Citizen Lab.
- Sysdiagnose is a diagnosing tool from Apple, it's running on the backups, it's in fot585.com/sysdiagnose. There are guides on this.
With sysdiagnose you can get a lot of info. Things to note:

- It takes 10-15mn
- iTunes backups may take hours depending on the size and USB.
- It needs user interaction. They require some knowledge of IT (python, etc). So it's a challenge for end users to do it themselves. It's actually better to ship the phone in some areas.

It's great to check for old malware, IOCs are not publicly available, because they don't want to expose it to attackers.

## BlastPass

Vuln disclosed, and used directly by NSO, in about the same day (!!). 

They found 25x crashes of `homed` which was a bit suspicious. The crashes from homed looked normal, the `messagesBlastDoorServices` crashes looked weird. 

He used the backup to see `IMTransferAgent` was using `sample.pkpass` files. It was containing files that were a bit weird (image not using the proper image format). 

The image contained an `NSExpression`; It's been used in the past in Pegasus and operation triangluation. It's a way to execute code on iOS.

The NSExpression has different payloads, but it was a bit scrumbled together.

After trying to debug what were the NSExpressions, he found [`dlsym`](https://linux.die.net/man/3/dlsym) was used. He got a number back that was `-2`, so that looked like a way to access a place it wasn't supposed to access.

They were using Imsg to receive the messages, not sure exaclty what it does and why it matters. It seems a nice to way to hide. 

## Current state and outlook

iOS added a bunch of mitigations, but it doesn't make it easier to detect malware. There are a bunch of orgs that publish research on these: RSF, Amnesty International,.

In 2024:

- we don't have ways to share data between the different organisations.
- The security higiene is not great, people aren't keeping their systems updated properly.
- Apple doesn't provide specific devices to people that would like to work on this.

## Security VS privacy VS visibility

- Too less visibility harms security
- Too less security harms privacy
- Too much visibility harms privacy

## Lockdown mode

Unfortunately, doesn't prevent all attacks, but it reduces the attack surface. It's not a silver bullet. Attackers are going to find ways around it.

## What will happen in the future?

The attack surface might change, and also target directly the applications (Signal, WhatsApp).

## Wishlish

- It could be great to avoid duplication of work.
- Apple could start a programme for people doing forensics
- Research could also discuss who is being targeted, and scientific study on this could be done to objectify.
- Forensics on Apple Vision, and other hardware that's getting used nowadays.
