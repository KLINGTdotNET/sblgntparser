#!/bin/bash

DIRS=( 'dist' 'build' )

for d in ${DIRS[@]}; do
	if [ -d $d ]; then
        echo "removing $d ..."
        rm -r $d
    fi
done
