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

bool IsSubstring(string str1, string str2){
    if(str1.find(str2)!=string::npos) return true;
    else return false;
}


int main(){
    string s1, s2;
    getline(cin, s1);
    getline(cin, s2);
    s2 += s2;
    if (IsSubstring(s2, s1)) cout << "OK" << endl;
    else cout << "NG" << endl;

    return 0;
}