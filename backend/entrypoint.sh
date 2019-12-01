#!/usr/bin/env bash
set -o errexit
set -o pipefail

cmd="$@"

python manage.py db upgrade

exec $cmd
