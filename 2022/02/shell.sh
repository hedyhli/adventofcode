#!/usr/bin/env sh


mapscore () { echo $1 | tr ABC 123; }
mapXYZ () { echo $1 | tr XYZ ABC; }
towin () { echo $1 | tr CAB ABC; }
tolose () { echo $1 | tr CAB BCA; }


# part 1
# SLOW (<1min but still)
score=0
while read line; do
    col1=$( echo "$line" | grep -o '[ABC]' )
    col2=$( echo "$line" | grep -o '[XYZ]' )
    abc=$(mapXYZ $col2)
    if [ $abc = $col1 ]; then
        # draw
        score=$((score + 3))
    fi
    if [ $(towin $col1) = $abc ]; then
        # win
        score=$((score + 6))
    fi
    score=$((score + $(mapscore $abc)))
done < input.txt
echo $score
