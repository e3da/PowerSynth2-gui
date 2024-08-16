#!/bin/bash

folder=$( dirname -- "$0" )

qtpkg=pyside6
declare -A exe=( ["ui"]="$qtpkg-uic" ["qrc"]="$qtpkg-rcc")
declare -A arg=( ["ui"]="--from-imports" ["qrc"]="")
declare -A post=( ["ui"]="" ["qrc"]="_rc")

for type in "${!exe[@]}"
do
	dir=$folder/$type
	echo -n "INFO: Processing $dir: "
	for file in $dir/*.$type
	do
		base=`basename $file .$type`
		echo -n "$base.$type, "
		${exe[$type]} $file ${arg[$type]} -o $folder/py/$base${post[$type]}.py
	done
	echo "DONE."
done
