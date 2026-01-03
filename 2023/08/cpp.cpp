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

#define debug(x) cerr <<"["<<(#x)<<"="<<(x)<<"]"
#define debugln(x) cerr <<"["<<(#x)<<"="<<(x)<<"]\n"

#define cendl cout << endl
#define println(X) cout << X << endl

/* #define max3(X, Y, Z) max(X, max(Y, Z)) */
/* #define min3(X, Y, Z) min(X, min(Y, Z)) */

#define showvec(a) for(int i=0;i<a.size();i++) cout<<a[i]<<' ';cout<<endl;
/* #define show1d(a) for(auto const &x : (a)) cerr<<x<<' ';cerr<<endl; */

/* void iswap(int *a,int *b) {int c=*a; *a=*b; *b=c;} */

/* const double PI = 3.141592653589793238462643383279; */
/* const ll INF = numeric_limits<ll>::max(); */
/* const int INFI = numeric_limits<int>::max(); */
/* #define StreamMax numeric_limits<streamsize>::max() */

typedef unordered_map<string, string> Map;

vector<Map> maps;  // 0 for L, 1 for R
string ins;

/// parsing ///////////////////////////////////////////////////////////////////
void setup() {
    cin >> ins;
    replace(ins.begin(), ins.end(), 'L', '0');
    replace(ins.begin(), ins.end(), 'R', '1');

    char a[3], b[3], c[3];

    Map m1, m2;
    cin.ignore(1);
    string tmp;

    //    1234   12   1
    // AAA = (BBB, CCC)
    cin >> a;
        cin >> tmp;
        cin.ignore(2);
        cin >> b;
        cin.ignore(2);
        cin >> c;
        cin.ignore(2);
        m1[a] = b;
        m2[a] = c;
    maps.push_back(m1);
    maps.push_back(m2);
}

/// algorithm /////////////////////////////////////////////////////////////////

/// solution //////////////////////////////////////////////////////////////////

void part1() {
}

void part2() {
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    setup();
    for (const auto &c : maps) {
        for (const auto &[x, y] : c) {
            println(x << " : " << y);
        }
        println("");
    }

    part1();
    part2();
}
