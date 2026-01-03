#include <bits/stdc++.h>
using namespace std;

void solve() {
    int group = 0;
    string line;

    priority_queue<int> top;

    while (getline(cin, line)) {
        if (!line.size()) {
            top.push(group);
            group = 0;
            continue;
        }
        istringstream iss(line);
        int x;
        iss >> x;
        group += x;
    }

    // Part 1
    int maxgroup = top.top();
    top.pop();

    // Part 2
    int part2 = maxgroup;
    int want_top_n = 3;
    for(int i=0; i<want_top_n-1; ++i) {
        part2 += top.top();
        top.pop();
    }
    cout << maxgroup << endl;
    cout << part2 << endl;
}

int main() {
    solve();
}
