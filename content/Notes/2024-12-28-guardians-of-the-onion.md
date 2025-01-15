---
title: Guardians of the onion
speakers: gus and hiro
tags: 38c3, Tor
---
*These are notes taken during and after the 38C3 conference in Hambourg. Notes might be a bit sketchy at times*

<iframe width="1024" height="576" src="https://media.ccc.de/v/38c3-guardians-of-the-onion-ensuring-the-health-and-resilience-of-the-tor-network/oembed" frameborder="0" allowfullscreen></iframe>

This was a talk to discuss what makes a "good" community, and a good Tor network. I liked how it was focused on politics mainly, rather than tech stuff.

So, is the Tor network healthy? And how do we assess it?

It should have:

- Strong community support
- Continuous improvements, protocol updates
- Wide adoption

Currently, relay diversity could be improved, the community is not necessarily sustainable, and there are adversaries.

## Is tor still safe to use?

First they wanted to adress the elephan in the room, as [attacks on Tor](https://blog.torproject.org/tor-is-still-safe/) have been advertized in the past few months. They believe that the attacks were conducted before they added some security measures to the Tor network, and that the affected sotware was using a now deprecated protocol.

They learned these lessons:

- Somebody used a retired version of Ricochet, that didn't use new security measures implemented in Tor now.
- [Vanguard measures](https://spec.torproject.org/vanguards-spec/index.html) are able to protect service operators running behind `.onion` services.

They added documentation on how to run hidden services. As part of this discussion, they've seen people stating things that don't really make a lot of sense:

- Traffic padding is already used in the protocol ;
- Some people said that mixnets is the solution, but because it adds traffic it is currently slow. They believe it will lead to people leaving the network because it is not usable.

## So, how to check the health of the network?

They are using some numbers to objectify this. 8 000 relays and 2500 exit nodes.

Performance has been better, and they see a concentration of the nodes, that needs to be adressed.
A lot of nodes are hosted in germany and in the US, this can be better. 

[Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) quantifies the diversity in the distribtion of network attributes.

Diversity is important for obvious reasons, but also for legal reasons. They compared this with some other data, and has seen that the distribution is the same.

They looked at Cloudfare data about [AS](https://en.wikipedia.org/wiki/Autonomous_system_(Internet)) and it seem that WHAT ?

They believe taht the Tor network is well distributed against AS and ISPs.

## What can we do about it?

They have [a tool named bandwisth scanner](https://blog.torproject.org/how-bandwidth-scanners-monitor-tor-network/) that picks a relay and look a its bandwidth. That allows to keep a list of running relays and influence how circuits are built.

Location bias is a thing when measuring performance, because of how we measure (and from where we measure). 

Congestion control eleminates the speed limit of current C-Tor., it reduces the latency by minimizing queue lenghts at relays.

So it results in signifcant perfomance improvements, and increase the overall network capacity.

They say that the concentration they see in the Tor network is the concentration of the infrastructure.

## Community

It's important to have a diverse community that is able to trust each other.

To combat bad relays, and because it's very common to have false negatives, [they now have a policy](https://gitlab.torproject.org/tpo/community/policies/-/issues/25) explaining how to operate relays.

The relay operator community governance is also important. They have a documentation with ["expectations" for relay operators](https://community.torproject.org/policies/relays/expectations-for-relay-operators/). Excerpt:

> not run more than 20% of the total exist capacity or more than 10% of consensus weight.

## Outreach with the global south

They have a micro-grant to support the Tor community in the global south and to add geographical diversity to the network.

Snowflake outreach in the GS seem a better approach for their current capacity and resources. 

## Impact on the environment

Partnership between SEEKCommons and Tor project. They want to measure the Tor network carbon footprint. 

## Call to action

They need more bridges. This can be a Snowflake proxy or a WebTunnel bridge. They launched a campaign [and you can get Tshirts ](https://blog.torproject.org/call-for-webtunnel-bridges/)

;)
