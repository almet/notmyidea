---
title: Setting up GPG signing key for github
tags: gpg, github
---

I recently had to create a new GPG signing key and add it as a correct signature
for my github account. Here is how I did, for future reference.

## Creating the key and exporting it

I created the key in thunderbird, which I use for my mails. I did it directly
there to avoid having to import it then, but I could also have generated it on
the command line.

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

There is [a comprehensive guide](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits)
on how to do that, which basically tells you to:


```bash
git config --global commit.gpgsign true

```

## Using multiple identities dependening the git repo

Because I have multiple identities I commit with, I had to change the identity
used for a specific repository.

The way to do that was to have a different `.gitconfig` loaded depending on the
repo being used. I put this in my `.gitconfig`:

```ini
[includeIf "gitdir:~/dev/**/.git"]
  	path = .gitconfig-user

[includeIf "gitdir:~/dev/fpf/**/.git"]
  	path = ~/.gitconfig-fpf
````

And the `~/.gitconfig-fpf` file to be like:

```ini
[user]
	name = Alexis Métaireau
	email = --redacted--@freedom.press
```

## Exporting the public PGP keys

At some point, I needed to give github the public key associated with my private
key. As I'm using Thunderbird to store the keys, I asked it to export the public
key.
