Installation
============

The client can be installed via ``pip``

.. code::

    pip install securenotes-client

Configuration
=============

The configuration is written in the INI format and saves basic parameters. The
available sections are described below:

DEFAULT
-------

.. list-table:: Options
    :header-rows: 1

    * - Option
      - Description
    * - username
      - Used for authentication
    * - password
      - Used for authentication
    * - passphrase
      - Used for decryption and encryption
    * - host
      - FQDN to API