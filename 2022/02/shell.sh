#!/usr/bin/env sh

# answers have been checked


mapscore () { echo $1 | tr ABC 123; }
# mapXYZ () { echo $1 | tr XYZ ABC; }
towin () { echo $1 | tr CAB ABC; }
tolose () { echo $1 | tr CAB BCA; }


# part 1
# SLOW (<1min but still)
score=0
while read line; do
    col1=$( echo "$line" | grep -o '[ABC]' )
    col2=$( echo "$line" | grep -o '[XYZ]' )
    abc=$(echo $col2 | tr XYZ ABC)

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
# aoc -y 2022 -d 2 submit 1 $score

# part 2
# getscore () { echo $1 | tr XYZ 036; }

score=0
while read line; do
    col1=$( echo "$line" | grep -o '[ABC]' )
    col2=$( echo "$line" | grep -o '[XYZ]' )

    # score=$((score + $(getscore $col2)))
    score=$((score + $(echo $col2 | tr XYZ 036)))

    shape=$col1  # Assume draw first
    case $col2 in
        X)
            # lose
            shape=$(tolose $col1);;
        Z)
            # win
            shape=$(towin $col1);;
    esac
    score=$((score + $(mapscore $shape)))
done < input.txt
echo $score
# aoc -y 2022 -d 2 submit 2 $score
