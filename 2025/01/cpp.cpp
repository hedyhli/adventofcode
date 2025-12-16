#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
/* int: -2^31 .. 2^31-1  (2E+9) (32 bits)
 * ll:  -2^63 .. 2^63-1  (9E+18) (64 bits)
 * double: +- -1.7E+308
 * char,bool: 8 bits
 */

#define endl '\n'

#define debug(x) cerr <<"["<<(#x)<<"="<<(x)<<"]"
#define debugln(x) cerr <<"["<<(#x)<<"="<<(x)<<"]\n"

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    char c;
    int amount;

    int dial = 50;
    int count = 0;

    while (cin >> c) {
        int mul = 1;
        if (c == 'L') {
            mul = -1;
        }
        cin >> amount;
        dial += mul * amount + 100;
        dial %= 100;
        if (dial == 0) {
            count += 1;
        }
    }
    cout << count << endl;
}

void part2() {
    char c;
    int amount;

    int dial = 50;
    int count = 0;
    
    int prev_was_0 = 1;

    while (cin >> c) {
        if (c == 'L') {
            cin >> amount;
            if (amount >= dial) {
                int v = -dial;
                if (dial != 0) {
                    v += 100;
                }
                v += amount;
                // cerr << "L "; debug(amount); debugln(v);
                count += (v - v%100)/100;
                // cerr << count << endl;
            }
            dial -= amount;
        } else if (c == 'R') {
            cin >> amount;
            dial += amount;
            // cerr << "R "; debugln(amount);;
            count += (dial - dial%100)/100;
            // cerr << count << endl;
        }
        dial = (dial + ((abs(dial)/100+1)*100)) % 100;
        // debugln(dial);
    }
    cout << count << endl;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    // part1();
    part2();
}
