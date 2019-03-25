#!/bin/bash

d=`/bin/pwd`

# modify the following to be the root of the 'ca-steel-design' tree
casd=$d/../ca-steel-design

PYTHONPATH=$d:$casd/lib:$PYTHONPATH
echo $PYTHONPATH
PYTHONPATH="$PYTHONPATH" jupyter lab
