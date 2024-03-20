#include <vector>
#include <iostream>
#include <numeric>
#include <bitset>
#include <string>
#include <stdio.h>
#include <set>
#include <iomanip>
using namespace std;

int main(){
    string s;
    int check = 0;
    cout << "char of check is " << bitset<32>(check) << endl;
    cin >> s;
    for (int i=0; i<s.size(); i++){
        int val = s[i] - 'a';
        cout << "char of " << s[i] << " is " << bitset<32>(s[i]) << endl;
        cout << "char of s[i] - 'a' is " << bitset<32>(s[i]-'a') << endl;
        if ((check&(1<<val)) > 0){
            cout << "NG" << endl;
            return 0;
        }
        check |= (1 << val);
        cout << "char of check is " << bitset<32>(check) << endl;
    }
    cout << "OK " << endl;
    return 0;
}