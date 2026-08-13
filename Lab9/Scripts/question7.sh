#!/bin/bash

mass=1
speed=3*10^8

var=$(bc << EOF
$mass*$speed*$speed
EOF
)

echo 'Energy-mass equivalence (in J): '$var


