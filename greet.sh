#!/bin/sh

DAY=$(date +%A)
GREETING="Hello dear $USER - it's yet another $DAY \\o/"

N=1
if [ -n "$1" ]; then
	N=$1
fi

while [ "$N" -ge 1 ]; do
	echo "${GREETING}"
	N=$((N - 1))
done
