---
title: Breaking NATO Radio Encryption
speaker: Lukas Stennes
link: https://events.ccc.de/congress/2024/hub/en/event/breaking-nato-radio-encryption/
date: 2024-12-27
type: talk
tags: 38c3, radio
---

<iframe width="1024" height="576" src="https://media.ccc.de/v/38c3-breaking-nato-radio-encryption/oembed" frameborder="0" allowfullscreen></iframe>

This was a fairly technical talk, in which the speaker explained how the cypher scheme used for NATO radion encryption works, why it was weak, and how he broke it.

## Intro to symmetric cryptography

Alice, Benjamin and Chalie are used as a replacement for Alice and Bob.


AES is Advanced Encryption Standard, it's one of the most used crypto out there, and it works well.

It takes an input and generate ciphertext from a key. It's the US standard since the 2000. [There is a lecture by Chirstof Paar if you want to understand how it works in depth: [Lecture 8: advanced Encryption Standard (AES)](https://www.youtube.com/watch?v=NHuibtoL_qk)

## High frequency radio

Frequencies between 3MHz and 30MHz. These signals can cover large distances, because the signals are reflected by upper atmosphere, and they don't need external infrastructure. 

For radio, SoDark / HALFLOOP is used for encrypting some of the material.


### Automatic Link Establishement / HALFLOOP

Here is how it works:

1. 3-way handshake in the beginning (authenticated with SoDark or HALFLOOP)
2. Voice or Data (unauthenticated ?)
3. Finish (authenticated)

SoDark was used more in the past, now it's more HALFLOOP.

It's encrypted:

- Authentication (be sure that who claims an id is the right one)
- Nobody can read else from the recipient.

### HALFLOOP24

<fig1>
<fig2>

HALFLOOP used a *tweakable* block cypher. SoDark cipher used 56-bits keys, which was easy to bruteforce.

- In addition to the key, it is ussing a "tweak" as another input: the current time a word counter and the used frequency.
- It's using the same S-box as AES
- It's using the same key schedule
- State is represented as 3x1 matrix.
- 10 rounds are used

### ECB is broken ?

It's a block cipher, and because it's possible to see the whole picture if you just use it (because it's applied on a block by block basis), except if you add a tweak.

- Split the input in 3 (8 bits each)
- On the two last ones we bit shift 6 and 4

### Presentation of how it works in detail.

He then went onto how this works and how he broke it. I didn't took note in there because it was already hard to follow along :-)

### Papers

Interestingly, one of the researchers is coming from Rennes: Patrick Derbrez (@IRISA, Rennes)

### Attacks

When trying to find attackers, they are often given extra power. In our exemple, Alice can answer to Charlie (the attacker), to encrypt, decrypt some stuff.

It's security in depth, because in practice the attackers might not have these "superpowers".

### Takeaways

It would have been possible to just use AES. The size of the block size is not a real reason for not using it.

The attack is basically using the tweak and knowing it to get back the key used to do the cypher.

### QA

Is there closer collaboration now between military and researchers in the public now than before? No real answer, as they asked NATO about this but never got an answer.

There is [an actual implementation of this](https://github.com/rub-hgi/destroying-HALFLOOP-24/blob/main/halfloop.c)
