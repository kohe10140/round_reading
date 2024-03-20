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

string replace(string str, int length){
    string result = "";
    for(int i=0; i<length; i++){
        if (str[i] == ' ') result += "%20";
        else result += str[i];
    }
    //string result = regex_replace(str, regex(" "), "%20");
    return result;
}


int main(){
    string str;
    int length;
    getline(cin, str);
    cin >> length;
    cout << replace(str, length) << endl;
    return 0;
}