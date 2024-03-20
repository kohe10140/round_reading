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

bool palindorme(string str){
    string result = "";
    int cnt[256] = {0};
    
    for (int i=0; i<str.size(); i++){
        int val = str[i] - 'a';
        cnt[val] += 1;
    }
    int odd_cnt = 0;
    for (int i=0; i<end(cnt) - begin(cnt); i++){
        if(cnt[i]%2 == 1) odd_cnt++;
    }
    if (odd_cnt > 1) return false;
    return true;
}


int main(){
    string str;
    getline(cin, str);
    if (palindorme(str)) cout << "OK" << endl;
    else cout << "NG" << endl;
    return 0;
}