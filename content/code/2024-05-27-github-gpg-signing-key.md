---
title: Multiple identities and GPG keys for git
tags: gpg, git
---

I recently had to create a new identity and GPG signing key for my github profile. 
Here is how I did, for future reference:

## Creating the key and exporting it

I created the key in thunderbird, which I use for my emails. I did it directly
there, but it's also possible to generate it directly on the command line.

I had some trouble finding how to export the key from thunderbird, you actually
have to open the OpenPGP key manager, select you key and then do "file/export",
which is kind of unintuitive.

I realized afterhand that the code I entered here will be stored in my keyring
manager. Choose something unique ;-)

## Importing it in the local keyring

```bash
gpg --import /Volumes/o5avOD-1fyGp/Clés/Alexis\ Métaireau\ --redacted--@freedom.press-\(0xC65C7A89A8FFC56E\)-secret.asc  
```

It should show up when using `gpg --list-keys`:

```bash
gpg --list-keys
[keyboxd]
---------
pub   ed25519 2024-05-27 [SC] [expire : 2027-05-27]
      454294C6FF8B9716A5F641A9C65C7A89A8FFC56E
uid          [ inconnue] Alexis Métaireau <--redacted--@freedom.press>
sub   cv25519 2024-05-27 [E] [expire : 2027-05-27]
```

## Signing your commits

Add this section to you `.gitcommit` file:

```ini
[commit]
	gpgsign = true
```

Which is also possible by entering this on the command line:


```bash
git config --global commit.gpgsign true
```

## Using multiple identities dependening the git repo

So, I want to use only one github account, tied to different identities. 

In your `.gitconfig`, you can load different configuration files depending on the
repo being used using the `includeIf` key. Here's what my file look likes:

```ini
[includeIf "gitdir:~/dev/**/.git"]
  	path = .gitconfig-user

[includeIf "gitdir:~/dev/fpf/**/.git"]
  	path = ~/.gitconfig-fpf
````

And the `~/.gitconfig-fpf` file:

```ini
[user]
	name = Alexis Métaireau
	email = --redacted--@freedom.press
```

## Exporting the public PGP keys

At some point, I also needed to give github the public key associated with my private
key. As I'm using Thunderbird to store the keys, I asked it to export the public
key.
