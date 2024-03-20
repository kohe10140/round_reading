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

string compress(string str){
    string cmp = "";
    char tmp = str[0];
    long long cnt = 1;
    for (int i=1; i<str.size(); i++){
        if(tmp==str[i]){
            cnt++;
        }else{
            cmp = cmp + tmp + to_string(cnt);
            tmp = str[i];
            cnt=1;
        }
    }
    cmp = cmp + tmp + to_string(cnt);
    if (str.size()>cmp.size()) return cmp;
    else return str;
}


int main(){
    string str, res;
    getline(cin, str);
    res = compress(str);
    cout << res << endl;
    return 0;
}