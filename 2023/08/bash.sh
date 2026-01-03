#!/usr/bin/env bash
#
# >= bash 5.0

set -e

infile="input.txt"
ins=$(head -n1 $infile)
len=$(echo $ins | wc -c)
let len--

declare -A map1
declare -A map2
eval "$(sed -e '1,2d; s/^/map1[/; s/ = /]=/; y/()/""/; s/,.*/"/' < $infile)"
eval "$(sed -e '1,2d; s/^/map2[/; y/()/""/; s/ = ...., /]="/;' < $infile)"

get_z() {
    node="$1"
    count=0
    i=0
    # must not add quotes around the regex $2
    while [[ ! $node =~ $2 ]]; do
        if [[ ${ins:i:1} == L ]]; then
            node=${map1[$node]}
        else
            node=${map2[$node]}
        fi
        i=$(( (i+1) % len ))
        count=$(( count + 1 ))
    done
    echo $count
}

# part1
# get_z AAA ZZZ

# part2
# array "as"
eval $(sed -e '1,2d' < $infile | grep '^..A' | sed -e 's/ .*//' | tr '\n' ' ' | sed -e 's/^/as=("/; s/$/)/; s/ /" "/g; s/ ")/)/')
len=$(sed -e '1,2d' < $infile | grep '^..A' | wc -l)

# echo this will take a while
#
# for (( i=0; $i < $len; i++ )) do
#     echo -en "\r"$i / $len
#     as[$i]=$(get_z ${as[$i]} ..Z)
# done

get_z BXA ..Z

# echo
# echo getting lcm
#
# # find gcd & lcm
# prev=${as[0]}
# next=${as[1]}
# for (( i=1; i <= $len; i++ ));do
#     temp1=$prev
#     temp2=$next
#     while [ $prev -ne $next ];do
#         if [ $prev -gt $next ];then
#             prev=`expr $prev - $next`
#         else
#             next=`expr $next - $prev`
#         fi
#     done
#     gcd=$prev
#     buff=`expr $temp1 \* $temp2`
#     lcm=`expr $buff / $gcd`
#     next=${as[$i]}
#     prev=$lcm
# done
#
# echo $lcm
