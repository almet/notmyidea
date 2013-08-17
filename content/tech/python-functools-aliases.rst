Python, functools and aliases
#############################

:status: draft

I have been playing lately with python and functools to make method aliases. I
wanted to have something like this.

.. code-block:: python

    class Baby(object):
        
        def eat(self, thing):
            self.intestine.digest(thing)
