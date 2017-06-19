# milo-django

## Installation instructions

- Clone the repository from GitHub:

```bash
git clone https://github.com/alex-shamray/milo-django
```

- Create and activate isolated Python environments:

```bash
cd milo-django
virtualenv env --python=python3
source env/bin/activate
```

- Install project requirements:

```bash
pip install -r requirements.txt
```

- Prepare the DB:

```bash
python manage.py migrate
```

- (Optional) Create super user:

```bash
python manage.py createsuperuser
```

- Starting Django development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

The project is available on http://localhost:8000/


## Alternative way of installation

- Download and install VirtualBox https://www.virtualbox.org/wiki/Downloads
- Download and install Vagrant https://www.vagrantup.com/downloads.html
- Start Vagrant environment

```bash
vagrant up
```

- Prepare the DB:

```bash
vagrant django-manage migrate
```

- (Optional) Create super user:

```bash
vagrant django-manage createsuperuser
```

- Starting Django development server:

```bash
vagrant runserver
```
