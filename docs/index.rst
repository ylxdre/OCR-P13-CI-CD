.. OC Lettings Site documentation master file, created by
   sphinx-quickstart on Tue Sep 23 11:01:06 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

==============================
OC Lettings Site documentation
==============================

--------------
ylxdre OCR P13
--------------

.. toctree::
   :maxdepth: 3
   :caption: Contents:

Architecture
============

This Django project contains two main applications, with the following files  :

* profiles
    * views
    * models
    * templates
* lettings
    * views
    * models
    * templates
.. important::
    the `'settings.py'` file and the index base template and view are located under the base ``oc_lettings_site`` app

Models, as usual, are manageable from the admin page.


Tests
-----

| Tests are located in the ``tests`` directory, in the ``unit`` subdirectory.
| Then, there is a subfolder for every application, containing three files : `test_models`, `test_urls`, `test_views`
Temporary db (popuplated with some sample objects) is created for testing purpose; you can see fixtures used for this
in the ``conftest.py``.


Fixed issues
------------
| Linting is PEP8 compliant, see the HTML report in flake-report
| Plural of Address objects appears now well on admin (addresses, with a Meta method)
| There are 404 and 500 custom html template
| Every class or function has doctrings
| Test coverage is 100%



Logging in Sentry
=================

CI/CD
=====

github
------

gitlab
------

Docker
======
| You can retrieve the latest docker image from the DockerHub with the following command :

..  code-block::
    docker pull

