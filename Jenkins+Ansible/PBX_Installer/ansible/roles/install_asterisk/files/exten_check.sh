#!/bin/bash

LENEXTEN=$(asterisk -rx 'sip show peers' | grep $1 | awk 'NR==1{print $1}' | wc -c)
if [ ${LENEXTEN} -eq 0 ]; then
        echo "SET VARIABLE res ERROR"
else
        echo "SET VARIABLE res OK"
fi
