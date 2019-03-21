#!/bin/bash


# modify the following to be the root of the 'ca-steel-design' tree
casd=../ca-steel-design

d=`/bin/pwd`
PYTHONPATH=$d:$casd/lib:$PYTHONPATH jupyter lab
