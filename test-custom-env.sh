#!/bin/bash
while IFS= read -r line; do                                       
    if [[ ! $line =~ (#.*) ]]; then
        export $line;
    fi
done <.env.custom
python3 main.py