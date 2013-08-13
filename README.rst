ressl
=====

A simple `importd`_ based SSL redirector. It accepts requests and redirects
to the SSL version of the same page.

Why?
----

I needed something like this for a couple of sites that were hosted on a
shared hosting provider but I wanted to only have one process doing the
SSL redirects.

Usage
-----

Simply run::

    ressl

This launches ``ressl`` on port 8000 using Django's runserver management
command.

For production use it's **strongly** recommended to instead use a real
WSGI server like gunicorn_ or uWSGI_ , e.g.::

    gunicorn ressl

To use a different port, use the server's options, e.g.::

    gunicorn -b 127.0.0.1:12345 ressl

Debugging is done by setting the environment variable ``RESSL_DEBUG``
to any value::

    RESSL_DEBUG=yep gunicorn -b 127.0.0.1:12345 ressl

If your site runs behind a proxy, you may have to tell ``ressl`` how to
figure out if a request is SSL or not. Use the ``RESSL_PROXY_PROTOCOL``
environment variable to define it (defaults to
``'HTTP_X_FORWARDED_PROTOCOL'``)::

    RESSL_PROXY_PROTOCOL=HTTP_X_FORWARDED_PROTO gunicorn ressl

Feedback
--------

Feel free to open tickets at https://github.com/jezdez/ressl/issues.
Say thanks at https://www.gittip.com/jezdez/.

.. _gunicorn: http://gunicorn.org/
.. _uWSGI: https://github.com/unbit/uwsgi
.. _importd: http://pythonhosted.org/importd/
