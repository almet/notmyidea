---
title: Hello Quit X
speakers: grrr, Vinci and somebody else
tags: 38c3, musk, X
---
*These are notes taken during and after the 38C3 conference in Hambourg. Notes might be a bit sketchy at times*

I met with a collective of people behind the "Hello, Quit X" project. They are trying to help folks to get out of X / Twitter, and prepared a presentation about why they are doing it.

TLDR is: Fascism is coming, and Musk is really helping in that regard, controlling twitter and changing its algorithm.

One of the questions they are trying to answer is how to assess if a social media is "good" or not.

They believe that these are the questions to ask yourself:

- Portability: do you own your data?
- How the contents are selected / editorialized? How the protocol makes you see the environment?
- Can it be bought by someone?

Note how this last bullet point gets BlueSky out of the picture, as it's possible for it to be bought (it's even what they want it to happen).

## So, what did Musk do to Twitter?

When Musk bought and destroyed Twitter, it was something we could see coming. (I personally can relate to this, we very much knew that having a social media this centered would become a problem at some point)

They displayed [one tweet from Musk](https://x.com/elonmusk/status/1625368108461613057) that I wasn't aware of, where you can see an image of a women putting milk in the mouth of another women. They explained how milk is a symbol of nazis, and stated that "the message is clear here".

I found [an interesting article](https://knowyourmeme.com/editorials/guides/what-is-the-forced-to-drink-milk-meme-heres-the-explanation-behind-that-image-elon-musk-tweeted) about this, explaining where the "forced to drink milk" meme is coming from, and [another one from the NYT](https://www.nytimes.com/2018/10/17/us/white-supremacists-science-dna.html) explaining how white supremacists thought that white people are more common to get a gene to digest milk. I also found out an article explainng [how milk is a symbol of the neo-nazis](https://theconversation.com/milk-a-symbol-of-neo-nazi-hate-83292). As they put it:

>  Milk as a symbol of white supremacy has also entered the Twitterverse. In early 2017, it replaced Pepe the Frog as the newest emoji symbolizing white superiority.

---

Here is a list of what happened to Twitter since Musk bought it:

- Abandoned moderation. People doing moderation were fired. On this subject, they mentioned that even before Musk, Twitter weren't really moderating far-right.
- Suspension of accounts / journalists / activists (see [the Wikipedia article about it](https://en.wikipedia.org/wiki/December_2022_Twitter_suspensions))
- Threatened of cyber-squatting to get back the handles.
- Blackmailing of advertisement companies, framing it like they were doing it on purpose to destroy twitter. Musk threats have big impact.
- Algorithmic censorship. 
- He took for instance @america and gave it to the Trump presidency (not with the followers)

### Polarization

[David Chavalarias](https://iscpif.fr/chavalarias/), a CNRS researcher, pointed that Twitter contained 49% more toxic content after Musk joined ([link to the research](https://www.nature.com/articles/s41598-023-43980-4)).

People at standford university found that when you see toxic content, you stay longer on the platforms. So it's a way to hack attention.

There is [a book](https://editions.flammarion.com/toxic-data/9782080274946) (in French) about it.

It has been measured that there is a political polarisation going on, for instance two separae groups with pro climate and denialists.

Musk promotes white-supremacist contents, and he is "very close" to the Kremlin, and relays Kremlin propaganda and attacks against the media. One of the way he does it is by telling people they don't need the media anyore, saying to them that "the people is the media now". I'm just reproducing their claims here, and I've not searched for sources yet.

In mastodon, we see that people participate more and more in different topics. You see people from different point of views, because there is no algorithm that filters everything.

![The picture, description below](/images/38c3/chavalarias-twitter-evolution.png)

A picture comparing 2016 VS 2022 with Left and Right wing in Twitter. We see that the connections between people shifted and do not exist a lot now.

### Hello Quit X

Okay, so what are they proposing? 

They built [a tool](https://www.helloquitx.com/) to help people get away from Twitter / X. It's currently in beta, and the goal is to help people migrate. The way they intend to do that is by fixing the biggest problem if the way: the network effect.

They have a public database where they make connections between accounts on X and accounts on Mastodon and Bluesky. They bootstrapped their database partially manually, and you can help this go further by registering yourself and letting them know the connection between your different accounts.

As a symbol, the goal is to flee away from Twitter on the 20th of January, the day Trump will access the presidency.

They want to also help you request the data out of Twitter, by using the RGPD (the law in France for data protection) to retrieve your tweets as a `.zip` archive.

It's a pretty fresh project, and they need help. If you know how to translate in your language, please pop up :-)


### Some technical stuff

As part of OAuth, the process might request some specific permissions. They are only using OAuth to prove the identities.

This has been coded by Fanny (from CNRS), who lead the thing. It's based on SPIP, but I couldn't find where the actual codebase is.


### On mastodon and engagement

Mediapart (a French media) is on Mastodon and Twitter. They have (had?) millions of followers on twitter, but actually very few interaction, compared to mastodon, where they have less followers but a lot more replies, retoots, etc. The engagement ratio is really better.

A lot of accounts on Twitter were inactive for years, and also a lot of bots. 
