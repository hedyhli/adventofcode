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
bool badbad(string s, int repcount) {
    if (repcount == 0) {
        vector<int> counter = vector<int>(10, 0);
        int minc = 0;
        for (char c : s) {
            counter[c - '0'] += 1;
            minc = counter[c - '0'];
        }
        for (int count : counter) {
            if (count != 0 && count < minc) {
                minc = count;
            }
        }
        if (minc == 1) {
            return false;
        }
        for (int count : counter) {
            if (count % minc != 0) {
                return false;
            }
        }
        repcount = minc;
    }
    if (s.length() % repcount != 0) {
        return false;
    }
    int unitlen = s.length() / repcount;
    for (int i = 0; i < unitlen; ++i) {
        for (int add = unitlen; (i+add) < s.length(); add += unitlen) {
            if (s[i] != s[i+add]) {
                return false;
            }
        }
    }
    return true;
}

ll get_value(string s) {
    ll value = 0;
    ll base = 1;
    for (int i = s.length()-1; i >= 0; --i) {
        value += base * (s[i] - '0');
        base *= 10;
    }
    return value;
}

string get_string(int value) {
    string s;
    vector<int> digits;
    while (value > 0) {
        digits.push_back((int)(value%10));
        value /= 10;
    }
    for (int i = digits.size()-1; i>= 0; --i) {
        s.push_back(digits[i] + '0');
    }
    return s;
}

ll partial1(string s, string s2) {
    ll result = 0;
    ll vs = get_value(s);
    ll vs2 = get_value(s2);
    // cout << vs << " " << vs2 << endl;

    while (vs <= vs2) {
        if (badbad(s, 0)) {
            // cout << s << endl;
            result += vs;
            vs += 10-(vs%10);
        } else {
            vs += 1;
        }
        s.clear();
        s = to_string(vs);
    }
    return result;
}

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    char c;
    string s = "";
    string s2 = "";
    bool at_ub = false;
    ll result = 0;

    while (cin >> c) {
        if (c == '-') {
            at_ub = true;
        } else if (c == ',') {
            result += partial1(s, s2);
            at_ub = false;
            s.clear();
            s2.clear();
        } else if (c < '0' || c > '9') {
            cerr << "Invalid character: " << c << endl;
        } else {
            if (!at_ub)
                s.push_back(c);
            else
                s2.push_back(c);
        }
    }
    result += partial1(s, s2);
    cout << result << endl;
}

void part2() {
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    part1();
    part2();
}
