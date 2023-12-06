/* Copyright all wrongs deserved */
/* C++17
 *
 * https://adventofcode.com/2023/day/6
 */

#include <string>
#include <vector>
#include <iostream>
#include <math.h>
#include <iterator>
#include <sstream>

using namespace std;
typedef long long ll;
/* int: -2^31 .. 2^31-1  (2E+9) (32 bits)
 * ll:  -2^63 .. 2^63-1  (9E+18) (64 bits)
 * double: +- -1.7E+308
 * char,bool: 8 bits
 */

#define endl '\n'
#define println(X) cout<<X<<endl
// #define showvec(a) for(int i=0;i<a.size();i++) cout<<a[i]<<' ';cout<<endl

#define StreamMax numeric_limits<streamsize>::max()

vector<int> times;
vector<int> dists;
int N;

/// parsing ///////////////////////////////////////////////////////////////////

/** Read all integers in current line into vector V */
void read_line(vector<int> &V) {
    string line; getline(cin, line); istringstream S(line);
    S.ignore(StreamMax, ':');
    copy(istream_iterator<int>(S), istream_iterator<int>(), back_inserter(V));
}

/** Concatenate all ints in vector V into a single (large) long long */
ll merge_ints(vector<int> &V) {
    string n = "";
    for (auto const &x : V)
        n += to_string(x);
    return stol(n);
}

/// algorithm /////////////////////////////////////////////////////////////////

/** Find first and last integer solution using bruteforce */
int get_ways_bruteforce(ll time, ll dist) {
    int last, first;
    for (ll hold = 1; hold < time; ++hold) {
        if (hold * (time - hold) > dist) {
            first = hold;
            break;
        }
    }
    for (ll hold = time-1; hold > 0; --hold) {
        if (hold * (time - hold) > dist) {
            last = hold;
            break;
        }
    }
    return last - first + 1;
}

/** Find the two roots using quadratic formula */
int get_ways_formula(ll time, ll dist) {
    double det = sqrt((double)(time*time - 4 * dist));
    double root1 = ((double)time - det)/(double)2;
    double root2 = ((double)time + det)/(double)2;
    return ceil(root2) - 1 - floor(root1);
}

/** The selected algorithm to use */
int get_ways(ll time, ll dist) { return get_ways_formula(time, dist); }
int get_ways(int time, int dist) { return get_ways((ll)time, (ll)dist); }

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    int prod = 1;
    for (int i = 0; i < N; ++i) {
        prod *= get_ways(times[i], dists[i]);
    }
    println(prod);
}

void part2() {
    ll time = merge_ints(times);
    ll dist = merge_ints(dists);
    println(get_ways(time, dist));
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    read_line(times);
    read_line(dists);
    N = times.size();
    part1();
    part2();
}
