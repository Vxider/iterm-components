#!/bin/bash

set -e

scripts_dir="$HOME/Library/Application Support/iTerm2/Scripts/AutoLaunch"
mkdir -p "$scripts_dir"

for src in */ ; do
    if [ $src = 'screenshots/' ]; then
        continue
    fi
    for script in "$src"/*.py; do
        echo Linking $script to $scripts_dir
        ln -sf ${PWD}/$script "$scripts_dir"
    done
done

