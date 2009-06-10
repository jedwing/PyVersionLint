#! /bin/sh

plugin_dir="`dirname $0`/.."
export PYTHONPATH=$plugin_dir:${PYTHONPATH:-.}
${PYLINT:-pylint} --load-plugins=pyver.py24_checker,pyver.py23_checker "$@"
