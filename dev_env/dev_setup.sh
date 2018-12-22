#!/usr/bin/env bash

echo cd $PWD
echo $PWD


virtualenv --python=python3.6 venv

pip install -r webapp/requirements.txt

source venv/bin/activate
