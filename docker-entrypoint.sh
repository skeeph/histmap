#!/usr/bin/env bash
while ! nc -w 1 -z db 5432;
    do sleep 0.1;
done;
./manage.py migrate;
./manage.py collectstatic --no-input
./manage.py mksuperuser

if [ -e loaded ]
then
    echo "Fixtures've been already loaded"
else
    ./manage.py loaddata world/fixtures/world.json
    touch loaded
fi
service nginx restart
./manage.py runserver 0.0.0.0:8000
