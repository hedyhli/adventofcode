/* Copyright all wrongs deserved */
/* C++17
 */

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
/* int: -2^31 .. 2^31-1  (2E+9) (32 bits)
 * ll:  -2^63 .. 2^63-1  (9E+18) (64 bits)
 * double: +- -1.7E+308
 * char,bool: 8 bits
 */

#define endl '\n'
#define println(X) cout<<(X)<< endl
#define showvec(a) for(int i=0;i<a.size();i++) cout<<a[i]<<' ';cout<<endl

vector<int> times;
vector<int> dists;
int N;

void read_line(vector<int> &V) {
    char c;

    // Read until start of numbers
    do { c = getchar(); } while (c != ':');
    c = getchar();

    // There are numbers
    while (c != '\n') {
        // Next number
        while (c == ' ') {
            c = getchar();
        } 

        string n = "";

        // Read number
        while (c != ' ' && c != '\n') {
            n += c;
            c = getchar();
        }
        V.push_back(stoi(n));
    }
}

ll merge_ints(vector<int> &V) {
    string n = "";
    for (auto const &x : V)
        n += to_string(x);
    return stol(n);
}

int get_ways(ll time, ll dist) {
    int w = 0;
    for (ll hold = 1; hold < time; ++hold) {
        if (hold * (time - hold) > dist)
            ++w;
    }
    return w;
}

int get_ways(int time, int dist) { return get_ways((ll)time, (ll)dist); }

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
