/* Copyright all wrongs deserved */
/* C++17
 */

#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <string>
#include <cassert>

using namespace std;

#define endl '\n'
#define println(X) cout << X << endl
// #define debug(x) cerr <<"["<<(#x)<<"="<<(x)<<"]"
// #define debugln(x) cerr <<"["<<(#x)<<"="<<(x)<<"]\n"
// #define showvec(a) for(int i=0;i<a.size();i++) cout<<a[i]<<' ';cout<<endl;
/* #define StreamMax numeric_limits<streamsize>::max() */


/// defs //////////////////////////////////////////////////////////////////////

unordered_map<char, int> strength {
    {'2', 0}, {'3', 1}, {'4', 2}, {'5', 3}, {'6', 4}, {'7', 5}, {'8', 6}, {'9', 7},
    {'T', 8}, {'J', 9}, {'Q', 10}, {'K', 11}, {'A', 12}
};

unordered_map<char, int> strength2 {
    {'J', 0}, {'2', 1}, {'3', 2}, {'4', 3}, {'5', 4}, {'6', 5}, {'7', 6}, {'8', 7},
    {'9', 8}, {'T', 9}, {'Q', 10}, {'K', 11}, {'A', 12}
};

typedef struct {
    int rank;             // returned by get_rank
    vector<int> scards;   // strength of each card
    // from input
    string cards;
    int bid;
} Hand;

/* sort to have highest ranks on top */
bool greaterHand(Hand const& lhs, Hand const& rhs) {
    if (lhs.rank != rhs.rank)
        return lhs.rank > rhs.rank;
    return greater<vector<int>>()(lhs.scards, rhs.scards);
}

typedef pair<int, char> CardFreq;

vector<Hand> hands;

/// parsing ///////////////////////////////////////////////////////////////////

/* hands must be uninitialized */
void parse_cards() {
    string x;
    while (cin >> x) {
        Hand h;
        h.cards = x;
        cin >> h.bid;
        hands.push_back(h);
    }
}

/// algorithm /////////////////////////////////////////////////////////////////

/* F must be uninitialized */
void get_freqs(vector<CardFreq>& F, string &cards) {
    unordered_map<char, int> freq;
    for (const char &c : cards) {
        try {
            int f = freq.at(c);
            freq[c] = f + 1;
        } catch (const exception &e) {
            // Any better way to emulate freq.contains(c) from C++20?
            freq[c] = 1;
        }
    }
    // std::map can't seem to sort by value so...
    for (const auto& [c, f] : freq) { F.push_back(make_pair(f, c)); }
    sort(F.begin(), F.end(), greater<CardFreq>());
}

int get_rank(string &cards) {
    vector<CardFreq> F;
    get_freqs(F, cards);

    if (F[0].first == 5) return 7;
    if (F[0].first == 4) return 6;
    if (F[0].first == 3 && F[1].first == 2) return 5;
    if (F[0].first == 3) return 4;
    if (F[0].first == 2 && F[1].first == 2) return 3;
    if (F[0].first == 2) return 2;
    if (F[0].first == 1) return 1;

    assert(0);
    return 0;
}

int get_result() {
    int result = 0;
    int i = hands.size();
    for (auto &h : hands) {
        result += i * h.bid;
        --i;
    }
    return result;
}

/// solution //////////////////////////////////////////////////////////////////

void part1() {
    for (auto &h : hands) {
        h.rank = get_rank(h.cards);
        vector<int> s;
        for (const char &c : h.cards) {
            s.push_back(strength[c]);
        }
        h.scards = s;
    }
    sort(hands.begin(), hands.end(), &greaterHand);
    println(get_result());
}

void part2() {
    for (auto &h : hands) {
        string jokify = h.cards; // resolve wildcards
        if (h.cards != "JJJJJ") {
            vector<CardFreq> F;
            get_freqs(F, h.cards);
            char top = F[0].second;
            if (top == 'J') top = F[1].second;
            replace(jokify.begin(), jokify.end(), 'J', top);
        }

        h.rank = get_rank(jokify);
        vector<int> s;
        for (const char &c : h.cards) {
            s.push_back(strength2[c]);
        }
        h.scards = s;
    }
    sort(hands.begin(), hands.end(), &greaterHand);
    println(get_result());
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    parse_cards();
    part1();
    part2();
}
