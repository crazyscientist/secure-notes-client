.. SecureNotes Client documentation master file, created by
   sphinx-quickstart on Sun Jan  6 14:35:36 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SecureNotes Client's documentation!
==============================================

The SecureNotes server just provides a means to store encrypted content and the
corresponding keys needed to share the encrypted content.

.. important::

   The server cannot access the keys as these are also encrypted. The
   passphrases are only known to the users.

There the handling of encryption is up to the clients:

.. uml:: encryption.puml

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   api
   cli

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
