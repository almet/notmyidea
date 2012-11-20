walint - tilt
#############

:status: draft

Things start to fold together. I still need some time to be up to
speed (new job / new city / new people), but the projects I'm working on are
pretty exciting and I like what I'm doing. We've been working with Tarek on a
tool about web services testing.

At Mozilla, we produce and consume web services. As an organisation defending
web standards, providing services that match these specifications is the least
we can do. 

Web App Lint (WALint) is a simple tool to help you to test your web services
against the HTTP specification. The goal is to detect potential problems a
service could be subject to, and to provide a simple-to-configure tool to test
your WS against HTTP as speced.  The long term goal is to be exhaustive on the
controllers we provide, but if you have special needs, you should be able to
define tests in a simple way.

As everything we do at Mozilla, the tool is an opensource project. Our goal is
to have something useful for web service consumers and providers.  If you think
you can be of any help, don't hesitate to drop me an email or fork on github.

Testing the HTTP specification
==============================

A lot of web services are written on top of HTTP. The protocol is fully
described in a specification and introduce some really interesting stuff we
should care about when implementing our services. This tool wants to check this
up and provide a ways to ensure that you are defining your web services the
right way. It's not a replacement for manual service testing, thus: you still
have to test that your web service is doing what you think it does. WALint is
checking the stuff we almost forgot all of the time.

For instance, the HTTP specification specifies that if the client sends a
request with a Content-Type not handled by the server, it should answer with a
"406 Not Acceptable" and should return the list of accepted headers (so the
client is able to send again the request with the right accept header). We also
check that sending weird data (broken json objects or authentication headers)
does not break the tested service.

Obviously, we don't have all the scenarios in mind, and they aren't all
implemented. That's where being an open source project makes sense. You, as
service providers and consumers, know what are the kind of mistake you are used
to do / to deal with. It should make "tilt": fork the project and write some
lines checking the particular behavior that's disturbing you, everyone will
enjoy it. If you prefer, just open a ticket and we'll care about the
implementation.

The documentation defines a list of all the implemented controllers:
http://packages.python.org/walint/controllers.html

What does it looks like?
========================

Here is an example of a configuration file: you describe the paths and
signatures of your web services, the controllers you want to use and the test
scenarios you want to run, that's it, just run "walint config.cfg" and you're
good.

Here's a capture of the output of the command line invocation: you get all the
paths tested with the different listed methods, and if needed what's not
working.  In the future, why not putting some documentation online with
information about how to fix common mistakes?

We also provide a wizard so it's possible to describe your web service in a
simple and easy way. Just invoke it with "walint --create config.cfg".

What's next ?
=============

We plan to do some fun stuff with WALint. Here are some thoughts:

* service discovery: just provide an API root URI and we'll try to discover
  what's in there and how to generate configuration files 

* unittest integration, so it's possible to have an unified way to describe web
  services with existing tools. (heh, we can do Web Services CI the easy way!)
* integration with cornice description language and other web services description
  languages (still to be defined) 
* your ideas, so please fill issues and provide us feedback, it's useful!
