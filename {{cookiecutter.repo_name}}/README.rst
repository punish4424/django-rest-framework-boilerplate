===============================
{{ cookiecutter.project_name }}
===============================


{{ cookiecutter.description }}

* Free software: BSD license

Requirements
------------

* Django 3.1+
* Python 3.8


Installation
----------------------------

#. Clone the git repository.
#. Create a production.py file in {{ cookiecutter.repo_name }}/{{ cookiecutter.project_name }}/{{ cookiecutter.project_name }}/settings, copying the content of production_example.py
    * Add your database details in the new production.py created.
    * Add the site admins in the ADMINS variable
    * Add server host in ALLOWED_HOSTS

#. Install project dependencies by running the following command::

    $ pip install -r requirements/development.txt

#. Apply migrations::

    $ python manage.py migrate

