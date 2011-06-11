Using JPype to bridge python and Java
#####################################

:date: 11/06/2011
:tags: python, java

Java provides some interesting libraries that have no exact equivalent in 
python. In my case, the awesome boilerpipe library allows me to remove
uninteresting parts of HTML pages, like menus, footers and other "boilerplate"
contents.

Boilerpipe is written in Java. Two solutions then: using java from python or 
reimplement boilerpipe in python. I will let you guess which one I chosen, meh.

JPype allows to bridge python project with java libraries. It takes another
point of view than Jython: rather than reimplementing python in Java, both 
languages are interfacing at the VM level. This means you need to start a VM 
fro your python script, but it does the job and stay fully compatible with
Cpython and its C extensions.

First steps with JPype
======================

Once JPype installed (you'll have to hack a bit some files to integrate
seamlessly with your system) you can access java classes by doing something
like that:

.. code-block:: python
    
    import jpype
    jpype.startJVM(jpype.getDefaultJVMPath())

    # you can then access to the basic java functions
    jpype.java.lang.System.out.println("hello world")

    # and you have to shutdown the VM at the end
    jpype.shutdownJVM()

Okay, now we have a hello world, but what we want seems somehow more complex. 
We want to interact with java classes, so we will have to load them.

Interfacing with Boilerpipe
===========================

To install boilerpipe, you just have to run an ant script::

    $ cd boilerpipe
    $ ant

Here is a simple example of how to use boilerpipe in Java, from their sources

.. code-block:: java

    package de.l3s.boilerpipe.demo;
    import java.net.URL;
    import de.l3s.boilerpipe.extractors.ArticleExtractor;

    public class Oneliner {
        public static void main(final String[] args) throws Exception {
            final URL url = new URL("http://notmyidea.org");
            System.out.println(ArticleExtractor.INSTANCE.getText(url));
        }
    }

To run it:

.. code-block:: bash

   $ javac -cp dist/boilerpipe-1.1-dev.jar:lib/nekohtml-1.9.13.jar:lib/xerces-2.9.1.jar src/demo/de/l3s/boilerpipe/demo/Oneliner.java 
   $ java -cp src/demo:dist/boilerpipe-1.1-dev.jar:lib/nekohtml-1.9.13.jar:lib/xerces-2.9.1.jar de.l3s.boilerpipe.demo.Oneliner

Yes, this is kind of ugly, sorry for your eyes. 
Let's try something similar, but from python

.. code-block:: python

    import jpype

    # start the JVM with the good classpaths
    classpath = "dist/boilerpipe-1.1-dev.jar:lib/nekohtml-1.9.13.jar:lib/xerces-2.9.1.jar"
    jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % classpath)

    # get the Java classes we want to use
    DefaultExtractor = jpype.JPackage("de").l3s.boilerpipe.extractors.DefaultExtractor

    # call them !
    print DefaultExtractor.INSTANCE.getText(jpype.java.net.URL("http://blog.notmyidea.org"))

And you get what you want. 

I must say I didn't thought it could work so easily. This will allow me to 
extract text content from URLs and remove the *boilerplate* text easily 
for infuse (my master thesis project), without having to write java code, nice!
