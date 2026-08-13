#!/bin/bash

echo "$HOME"

bc_output=$(bc <<EOF
scale=4
23934/44343
EOF
)

echo "The calculated value is $bc_output"

echo 'Files in HOME that starts with 'D': ' "$HOME"/D*

echo 'Entry containing username:'
grep "$USER" /etc/passwd


