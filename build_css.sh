#!/bin/sh

set -e

cd bootstrap_themes/static/bootstrap/themes
for theme in *; do
  if [ -d "$theme" ]; then
    mkdir -p "$theme/css"
    recess --compile "$theme/less/bootstrap.less" > "$theme/css/bootstrap.css"
    recess --compile --compress "$theme/less/bootstrap.less" > "$theme/css/bootstrap.min.css"
  fi
done
