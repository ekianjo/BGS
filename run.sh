#!/bin/bash
export HOME=$('pwd')
export PYTHONPATH=$HOME/site-packages
echo 'HOME: '$HOME
echo 'APPDATADIR: '$APPDATADIR
echo 'PYTHONPATH: '$PYTHONPATH

python $HOME/main.py
