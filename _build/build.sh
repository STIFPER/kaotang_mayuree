#!/bin/sh
# Rebuild every page from _build/master.html. Run from anywhere.
cd "$(dirname "$0")/.." || exit 1
python3 -I _build/build_pages.py && python3 -I _build/build_home.py && echo "Built all pages"
