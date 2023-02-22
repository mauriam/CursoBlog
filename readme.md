### Iniciar el Proyecto

- crear un entorno virtual

  $ python -m virutalenv env

- activar entorno virtual

  - windows

  $ env/scripts/activate

  - linux

  $ source env/bin/activate

- una vez activo el env instalar requeriments

  $ pip install -r requirements.txt

## correr el proyecto

    * ejecutar las migraciones

    $ python manage.py migrate

    * correr el server

    $ python manage.py runserver 8000
