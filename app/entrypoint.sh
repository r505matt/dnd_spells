#!/bin/bash
set -ex

args=("$@")

case $1 in
    # beat)
    #     exec celery -A app -l INFO beat --scheduler django_celery_beat.schedulers:DatabaseScheduler --pidfile /tmp/celerybeat.pid
    #     ;;

    # worker)
    #     exec celery -A app -l INFO worker
    #     ;;

    *)
        exec "$@"
        ;;
esac