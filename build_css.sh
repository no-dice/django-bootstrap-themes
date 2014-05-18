#!/bin/sh

set -e

cd bootstrap_themes/static/bootstrap/themes
for theme in *; do
  if [ -d "$theme" ]; then
    mkdir -p "$theme/css"
    lessc "$theme/less/bootstrap.less" > "$theme/css/bootstrap.css"
    recess --compress "$theme/css/bootstrap.css" > "$theme/css/bootstrap.min.css"
  fi
done
