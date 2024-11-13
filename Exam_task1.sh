#!/bin/bash

mkdir -p ~/TXT
counter=0
for file in *.txt; do
    cp "$file" ~/TXT
    counter=$((counter+1))
done

echo "$counter .txt files moved"
