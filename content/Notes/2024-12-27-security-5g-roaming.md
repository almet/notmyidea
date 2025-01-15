---
title: How roaming agreements enable 5G MitM Attacks
link: https://events.ccc.de/congress/2024/hub/en/event/how-roaming-agreements-enable-5g-mitm-attacks/---
date: 2024-12-27
tags: 38c3, telecoms
---
*These are notes taken during and after the 38C3 conference in Hambourg. Notes might be a bit sketchy at times*

<iframe width="1024" height="576" src="https://media.ccc.de/v/38c3-how-roaming-agreements-enable-5g-mitm-attacks/oembed" frameborder="0" allowfullscreen></iframe>

High value targets (politicians, journalists, activisits) can hardly hide right now. 

## TL; DR

5G Roaming is done to avoid/prevent billing fraud, not to enhance security.

- It is difficult for a trusted operator to decide if an authentication request is legitimate or not
- Smartphones are unable to verify roaming decisions and trust assumptions
- Visited networks can arbitrarily choose the network name displayed on the screen

## Introduction of protocols

- 2G has been used with rogue-based attacks. Turning off 2G saves us from these.
- 3G adds network authentication, and so limits the attack sruface to pre-authentication messages. But it's possible to use roaming for attacks. Past talks on this (but I didn't found which ones).
- 4G added crypto session keys, which are bound the one network. But you can bind session keys to roaming networks as well. Session keys only valid for one roaming network.
- 5G: Adds a concpet of "proof of presence" in roaming. It's more secure, but there are reports that law enforcement agencies use roaming to exploit the target phones. How can they do this?

## How roaming attacks work?

Legitimate roaming: when you travel, you can connect to the visited network, it then asks the home network to get the authentication. Between the two parts there is an agreement, and the home network can see the traffic only if it's routed there.

An attacker would: rogue base station a network looking like an extended network. The networks don't really check if the remote network is legitimate or not.

A state-sponsored attacker might force the operator to get access to the station.

Decrypted at the base station. So the good candidate for MiTM. It's encrypted by TLS. Basement exploits.

## From the user perspective

- There is a roaming operator. Like "F SFR | Telecom.de". There are local lists with the names and network IDs, but it can be out of sync (and it's expected that they'll be). You see an "R" indicating that the phone is roaming.
- The network ID is whatever the attacker want, so it's possible to impersonate legit networks.
- Roaming indicator disapears if the name is the proper one.

AV = Authtentication Network

Client cannot observe who requested AV, only if we're billed for it.

## Mitigations?

### Turning off roaming?

If the base station says it's your home network, it's sent before the Authentication. No proof required. The phone has to accept. The connection doesn't differentiate from the real legit connection.

### Firewalls?

There are firewalls, but they're not public, we don't know.

### End to end encryption

- Rogue based stations provide aacess to decrypted traffic of any connected phone. It could be prevented by E2EE. But they don't want this because of law enforcement.

### Visible trust chain

- Visible trust chain: trust decisions would be taken by core networks. Indicate information used to build trust to the user. Enable user to inspect network properties. The home networks checks identity of visited networks and roamning intermediaries.

### Indicators of Roamnig Abuse

1. Trace the routing path
2. Detect rogute base station
3. Measure the duration of authentication

Also rogue stations are very specialized. Measuring the time is not reliable, and not really possible to use right now.

### Disable 2G

Lockdown mode in apple, disables 2G. Lockdown mode will change a bit the behaviour of your apps. 

## Turn off automatic network detection

Picking it yourself, but it means that you need to know what you're doing.

## CellGuard (beta test)

It's a tool to collect information, the idea being to being able to notify you when it's needed.

### Roaming intermediaries

It's not clear exactly how the contracts are defined between the oeprators. 


## Q & A

### How much of it is by design?

Lawful interception is meant to be used. States and Law Enforcement agencies should be able to inspect the traffic in their countries. 

### What do we know about the intermediaries

We don't really know. These companies have a big impact, they collaborate with a lot of operators and are in the middle of the system. They are everywhere. Companies sitting in the middle, and they have political agency.

### Did yoy look on using hardware to improve security?

We looked in the specification and looked for how the phones behave. CellGuard looks on a database where the base stations are supposed to be, and warns you if there is another one?

### Is diabling roaming okay?

As shown, you can impersonate the home network, so no.

### Have you looked at Starlink, as they might be able to do the same kind of stuff?

Nope, not looked.

### What is the real risk? Is it only SMS? Did you do threat modeling?

We didn't do this, but I can say that SMS is unencrypted so yeah. The more TLS, the more secure it gets. it's used to target a single person, so it's really for speicifc people, and not for groups.

This is an expensible attack.

### is this used in the wild?

In our reeasearch, we didn't look so much on compromise, Citizen Lab and Amnesty Tech are trying to document this. 

### How does the connection work between base and 

You need to connect to the base operator (different from the "plain" internet). You have to contect the core network, I want to add more notes here as to how it works.

### How can this be fixed without changing the infra?

You have to have E2EE? Is VPN fixing this? Right from the start of the connection.
Having such a VPN would be good, BUT phone calls and SMS are not gong trough internet. 

## How much does it cost?

A rogue station is about 10k€ and then exploits are pretty costly.

---

@swantje@chaos.social
