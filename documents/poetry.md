# Docuementation for poetry



## First we need to install poetry



`pipx` is used to install Python CLI applications globally while still isolating them in virtual environments


`pipx` will manage upgrades and uninstalls when used to install Poetry


```bash
pipx install poetry
```

```bash
pipx uninstall poetry
```

```bash
pipx upgrade poetry
```



## Usage

There are two way of usage `poetry`

* First thing we need to create a new project

```bash
poetry new my-project
```

* Or install a pre-existing project

```bash
poetry init
```



```bash
poetry add django
poetry add djangorestframework
```


Next thing we need to do activate our virtual environment


```bash
poetry env activate
```


List of installed application
```bash
poetry show
```



After then we can create our djagno prjojects and apps



```bash

poetry run djang-admin startproject core .
poetry run python manage.py runserver
poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py createsuperuser

```


