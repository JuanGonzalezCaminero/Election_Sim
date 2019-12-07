#!/bin/bash
coverage run --source="main" manage.py test main
coverage report