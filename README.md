# UE5 Studio Analytics server and plugin

This is basically a copy of 
    https://github.com/testdrivenio/flask-on-docker
and
    https://gist.github.com/regner/592bb2cfca82f064ccd5322ea4c5deb8
merged together to work with Unreal Engine 5 Studio Analytics feature

### Development
[label](https://devblogs.microsoft.com/cppblog/whats-new-in-cmake-for-vs-code/)
Uses the default Flask development server.

1. Rename *.env.dev-sample* to *.env.dev*.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
    - (M1 chip only) Remove `-slim-buster` from the Python dependency in `services/web/Dockerfile` to suppress an issue with installing psycopg2
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:5000](http://localhost:5000). The "web" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. Rename *.env.prod-sample* to *.env.prod* and *.env.prod.db-sample* to *.env.prod.db*. Update the environment variables.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders. To apply changes, the image must be re-built.

docker-compose exec web python manage.py seed_db
docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev
\c hello_flask_dev
select * from events;
\q
