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

#define showvec(a) for(int i=0;i<a.size();i++) cout<<a[i]<<' ';cout<<endl;

/** Sum array per row */
vector<vector<int>> grid;
/** Actual representation of the grid */
vector<vector<int>> resg;

/// parsing ///////////////////////////////////////////////////////////////////

void getInputs() {
    string line;
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
        grid.push_back(row);
        resg.push_back(resrow);
    }
}

/// algorithm /////////////////////////////////////////////////////////////////

/**
 * Calculate the number of rolls that can be removed in this round, and remove
 * them in `resg` (does not change `grid`).
 * */
int removeRolls() {
    int result = 0;
    for(int i = 0; i < grid.size(); ++i) {
        vector<int> row = grid[i];
        int maxj = row.size()-1;
        for(int j = 0; j < maxj; ++j) {
            if (grid[i][j] != grid[i][j+1]) {
                int count = 0;
                //top
                if (i != 0) {
                    count += grid[i-1][min(j+2, maxj)] - grid[i-1][max(j-1, 0)];
                }
                //mid
                    count += grid[i  ][min(j+2, maxj)] - grid[i][max(j-1, 0)];
                //bot
                if (i != grid.size()-1) {
                    count += grid[i+1][min(j+2, maxj)] - grid[i+1][max(j-1, 0)];
                }
                if (count < 5) { // 4 + 1 because current cell is also a roll
                    ++result;
                    resg[i][j] = 0;
                }
            }
        }
    }
    return result;
}

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    cout << removeRolls() << endl;
}

void part2() {
    int total = 0;

    while (true) {
        int result = removeRolls();
        if (result == 0)
            break;

        total += result;

        // Update grid
        for (int i = 0; i < resg.size(); ++i) {
            vector<int> row = resg[i];
            for (int j = 1; j <= row.size(); ++j) {
                grid[i][j] = grid[i][j-1] + row[j-1];
            }
        }
    }

    cout << total << endl;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);

    getInputs();
    part1();
    part2();
}
