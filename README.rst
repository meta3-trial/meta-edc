|pypi| |codecov| |downloads|


META3 Edc
---------

Metformin Treatment for Diabetes Prevention in Africa: META3 Trial

A randomised placebo-controlled double-blind phase III trial to determine the effects of metformin versus placebo on the incidence of diabetes in HIV-infected persons with pre-diabetes in Tanzania.

Liverpool School of Tropical Medicine

EDCTP grant number: RIA2018CO-2513

Trial registration: ISCRTN 77382043

https://ico.org.uk/ESDWebPages/Entry/Z4763134


See also https://meta-trial/meta-edc, https://github.com/clinicedc/edc

Installation
------------

To setup and run a test server locally

You'll need mysql. Create the database

.. code-block:: bash

  mysql -Bse 'create database meta character set utf8;'


Create a virtualenv, clone the main repo and checkout master

.. code-block:: bash

  conda create -n edc python=3.7
  conda activate edc


Clone the main repo and checkout master

.. code-block:: bash

  mkdir ~/projects
  cd projects
  https://github.com/meta-trial/meta-edc.git
  cd ~/projects/meta-edc
  git checkout master


Copy the test environment file

.. code-block:: bash

  cd ~/projects/meta-edc
  git checkout master
  cp .env.tests .env


Edit the environment file (.env) to include your mysql password in the ``DATABASE_URL``.

.. code-block:: bash

  # look for and update this line
  DATABASE_URL=mysql://user:password@127.0.0.1:3306/meta


Continue with the installation

.. code-block:: bash

  cd ~/projects/meta-edc
  git checkout master
  pip install .
  pip install -U -r requirements/stable-v0.1.10.txt
  python manage.py migrate
  python manage.py import_randomization_list
  python manage.py import_holidays


Create a user and start up `runserver`

.. code-block:: bash

  cd ~/projects/meta-edc
  git checkout master
  python manage.py createsuperuser
  python manage.py runserver


Login::

  localhost:8000


Once logged in, go to you user account and update your group memberships. As a power user add yourself to the following

* ACCOUNT_MANAGER
* ADMINISTRATION
* AE 
* AE_REVIEW
* CLINIC
* DATA_MANAGER
* DATA_QUERY
* EVERYONE
* EXPORT
* LAB
* LAB_VIEW
* PHARMACY
* PII
* RANDO
* REVIEW
* SCREENING
* TMG
* UNBLINDING_REQUESTORS
* UNBLINDING_REVIEWERS


.. |pypi| image:: https://img.shields.io/pypi/v/meta3-edc.svg
    :target: https://pypi.python.org/pypi/meta3-edc

.. |codecov| image:: https://codecov.io/gh/meta3-trial/meta-edc/branch/develop/graph/badge.svg
  :target: https://codecov.io/gh/meta3-trial/meta-edc

.. |downloads| image:: https://pepy.tech/badge/meta3-edc
   :target: https://pepy.tech/project/meta3-edc
