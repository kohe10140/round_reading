#include <vector>
#include <iostream>
#include <numeric>
#include <bitset>
#include <string>
#include <stdio.h>
#include <set>
#include <iomanip>
#include <algorithm>
using namespace std;

bool permutation(string str1, string str2){
    int cnt1[256] = {};
    int cnt2[256] = {};
    bool result;
    if(str1.size()!=str2.size()) return false;
    for (int i=0; i<str1.size(); i++){
        int val1 = str1[i] - 'a';
        int val2 = str2[i] - 'a';
        cnt1[val1] += 1;
        cnt2[val2] += 1;
    }
    result = equal(begin(cnt1), end(cnt1), begin(cnt2));
    return result;
}


int main(){
    string str1, str2;
    cin >> str1 >> str2;
    if (permutation(str1, str2)) cout << "OK" << endl;
    else cout << "NG" << endl;
    return 0;
}