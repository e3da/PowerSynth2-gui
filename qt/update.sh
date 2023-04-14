#!/bin/bash

qtpkg=pyside2
declare -A exe=( ["ui"]="$qtpkg-uic" ["qrc"]="$qtpkg-rcc")
declare -A arg=( ["ui"]="--from-imports" ["qrc"]="")
declare -A post=( ["ui"]="" ["qrc"]="_rc")

for dir in "${!exe[@]}"
do
	echo -n "INFO: Processing $dir: "
	for file in $dir/*.$dir
	do
		base=`basename $file .$dir`
		echo -n "$base.$dir, "
		${exe[$dir]} $file ${arg[$dir]} -o py/$base${post[$dir]}.py
	done
	echo "DONE."
done
