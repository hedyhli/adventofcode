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


/// parsing ///////////////////////////////////////////////////////////////////

/// algorithm /////////////////////////////////////////////////////////////////
int find_largest(string s, int start, int end) {
    int a = 0;
    int ai = 0;
    for (int i = start; i < end; ++i) {
        int v = s[i] - '0';
        if (v > a) {
            a = v;
            ai = i;
        }
    }
    return ai;
}

ll solve_for(string s, int n, int start, int end) {
    int li = find_largest(s, start, end - n + 1);
    if (n == 1) {
        return s[li]-'0';
    }
    return (s[li]-'0')*(ll)pow(10, (double)(n-1)) + solve_for(s, n-1, li+1, end);
}

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    string s;

    int result = 0;
    while (cin >> s) {
        int ai = find_largest(s, 0, s.length());
        int li = find_largest(s, 0, ai);
        int ri = find_largest(s, ai+1, s.length());

        int a = s[ai] - '0';
        int l = s[li] - '0';
        int r = s[ri] - '0';
        int th = max(l*10 + a, a*10 + r);

        if (ai == 0) {
            th = a*10 + r;
        } else if (ai == s.length()-1) {
            th = l*10 + a;
        }

        result += th;
        // debugln(th);
    }
    cout << result << endl;
}

void part2() {
    string s;

    ll result = 0;
    while (cin >> s) {
        // part 1 can hence just be solve_for(s, 2, ...)
        ll th = solve_for(s, 12, 0, s.length());
        // debugln(th);
        result += th;
    }
    cout << result << endl;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);


    // part1();
    part2();
}
