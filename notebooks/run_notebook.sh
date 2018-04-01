#!/bin/bash

d=`/bin/pwd`
PYTHONPATH=$d:~/work/git/ca-steel-design/lib:$PYTHONPATH jupyter lab
