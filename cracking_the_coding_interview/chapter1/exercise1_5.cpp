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

bool one_time_transform(string str1, string str2){
    int shift1 = 0;
    int shift2 = 0;
    bool flg = false;
    int len1 = str1.size();
    int len2 = str2.size();
    if (abs(len1-len2)>1) return false;

    for (int i=0; i<min(len1, len2); i++){
        if (str1[i+shift1]!=str2[i+shift2]){
            if (shift1+shift2>1) return false;
            if (len1<len2) shift1++;
            if (len1>len2) shift2++;
            // 1回の置換で変換できない場合
            if ((len1==len2)&flg) return false;
            else flg = true;
        }
    }
    return true;
}


int main(){
    string str1, str2;
    getline(cin, str1);
    getline(cin, str2);
    if (one_time_transform(str1, str2)) cout << "OK" << endl;

    else cout << "NG" << endl;
    return 0;
}