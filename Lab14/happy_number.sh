#!/bin/bash

happy() {
    n=$1

    # In a Happy Number check, any non-happy number enters a cycle containing 4
    while [ "$n" -ne 1 ] && [ "$n" -ne 4 ]; do
        sum=0

        while [ "$n" -gt 0 ]; do
            digit=$((n % 10))
            sum=$((sum + digit * digit))
            n=$((n / 10))
        done

        n=$sum
    done

    if [ "$n" -eq 1 ]; then
        echo "TRUE"
    else
        echo "FALSE"
    fi
}

read -p "Enter a number: " num
happy "$num"
