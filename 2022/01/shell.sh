#!/usr/bin/env sh

sorttotals() {
    t=0
    while IFS= read -r line; do
        if [ -z "$line" ]; then
            echo $t; t=0; continue
        fi
        t=$((t + line))
    done < input.txt | sort
}

# part 1
echo max is $(sorttotals | tail -n1)
# part 2
echo sum of top three is $(sorttotals | tail -n3 | paste -sd+ | bc)


################ ugly solution
# part 1
# max=0
# total=0
# while IFS= read -r line; do
#     if [ -z "$line" ]; then
#         if [ $total -gt $max ]; then
#             max=$total
#         fi
#         total=0
#         continue
#     fi

#     total=$((total + line))
# done < input.txt

# echo max is $max
# echo -n sum of top three is' '
# t=0
# while IFS= read -r line; do
#     if [ -z "$line" ]; then
#         echo $t
#         t=0
#         continue
#     fi

#     t=$((t + line))
# done < input.txt | sort | tail -n3 | paste -sd+ | bc
