#!/bin/bash
set -e

case "$1" in
    develop)
        echo "Running Development Server"
        echo -e "$GS_PRO_SERVICE_ACCOUNT" | base64 -d > spreadsheet.json
        exec python main.py
        ;;
    test)
        echo "Test"
        exec python test.py
        ;;
    start)
        echo "Running Start"
        echo -e "$GS_PRO_SERVICE_ACCOUNT" | base64 -d > spreadsheet.json
        exec gunicorn -c gunicorn.py proconfig:app
        ;;
    *)
        exec "$@"
esac
