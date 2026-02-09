#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect Static Files
# This gathers all your CSS into the 'staticfiles' folder
python manage.py collectstatic --noinput --clear