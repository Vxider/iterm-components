#!/bin/bash

set -e

scripts_dir="$HOME/Library/Application Support/iTerm2/Scripts"

for src in */ ; do
    if [ $src = 'screenshots/' ]; then
        continue
    fi
    echo Linking scripts from $src to $scripts_dir
    ln -sf ${PWD}/$src "$scripts_dir"
done

