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

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    string line;
    vector<vector<int>> grid;
    vector<vector<int>> resg;
    while (cin>>line) {
        vector<int> row;
        vector<int> resrow;
        row.push_back(0);
        int i = 0;
        for (char c : line) {
            int cur = c == '@' ? 1 : 0;
            row.push_back(row[i++] + cur);
            resrow.push_back(cur);
        }
        // showvec(row);
        grid.push_back(row);
        resg.push_back(resrow);
    }

    auto get = [&grid](int i, int j) { /* debug(i);debugln(j) */; return grid[i][j]; };

    int result = 0;
    for(int i = 0; i < grid.size(); ++i) {
        vector<int> row = grid[i];
        int maxj = row.size()-1;
        for(int j = 0; j < maxj; ++j) {
            if (grid[i][j] != grid[i][j+1]) {
                int count = 0;
                //top
                if (i != 0) {
                    count += get(i-1, min(j+2, maxj)) - get(i-1, max(j-1, 0));
                }
                //mid
                    count += get(i  , min(j+2, maxj)) - get(i, max(j-1, 0));
                //bot
                if (i != grid.size()-1) {
                    count += get(i+1, min(j+2, maxj)) - get(i+1, max(j-1, 0));
                }
                if (count < 5) {
                    ++result;
                    resg[i][j] = 2;
                }
            }
        }
    }

    // for (vector<int> row : resg) {
    //     for (int c : row) {
    //         cerr << (c == 0 ? '.' : c == 1 ? '@' : 'x');
    //     }
    //     cerr << endl;
    // }
    cout << result << endl;
}

void part2() {
    string line;
    vector<vector<int>> grid;
    vector<vector<int>> resg;
    while (cin>>line) {
        vector<int> row;
        vector<int> resrow;
        row.push_back(0);
        int i = 0;
        for (char c : line) {
            int cur = c == '@' ? 1 : 0;
            row.push_back(row[i++] + cur);
            resrow.push_back(cur);
        }
        // showvec(row);
        grid.push_back(row);
        resg.push_back(resrow);
    }

    auto get = [&grid](int i, int j) { /* debug(i);debugln(j) */; return grid[i][j]; };

    int total = 0;

    while (true) {
        int result = 0;
        for(int i = 0; i < grid.size(); ++i) {
            vector<int> row = grid[i];
            int maxj = row.size()-1;
            for(int j = 0; j < maxj; ++j) {
                if (grid[i][j] != grid[i][j+1]) {
                    int count = 0;
                    //top
                    if (i != 0) {
                        count += get(i-1, min(j+2, maxj)) - get(i-1, max(j-1, 0));
                    }
                    //mid
                        count += get(i  , min(j+2, maxj)) - get(i, max(j-1, 0));
                    //bot
                    if (i != grid.size()-1) {
                        count += get(i+1, min(j+2, maxj)) - get(i+1, max(j-1, 0));
                    }
                    if (count < 5) {
                        ++result;
                        resg[i][j] = 0;
                    }
                }
            }
        }
        if (result == 0)
            break;

        total += result;

        // remove the rolls
        for (int i = 0; i < resg.size(); ++i) {
            vector<int> row = resg[i];
            for (int j = 1; j <= row.size(); ++j) {
                grid[i][j] = grid[i][j-1] + row[j-1];
            }
        }
    }

    // for (vector<int> row : resg) {
    //     for (int c : row) {
    //         cerr << (c == 0 ? '.' : c == 1 ? '@' : 'x');
    //     }
    //     cerr << endl;
    // }
    cout << total << endl;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    // part1();
    part2();
}
