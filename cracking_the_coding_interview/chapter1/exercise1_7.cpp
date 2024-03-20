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

using Matrix = vector<vector<int>>

bool rotate(Matrix &mat){
    if (mat.size()!=mat[0].size()) return false;
    int n = mat.size();
    for (int layer=0; layer<n/2; layer++){
        int first = layser;
        int last = n - 1 - layer;
        for (int i=first; i<last; i++){
            int offset = i - first;
            int top = mat[first][i];
            mat[first][i] = mat[last-offset][first];
            mat[last-offset][first] = mat[last][last-offset];
            mat[last][last-offset] = mat[i][last];
            mat[i][last] = top;
        }
    }
    return true;
}


int main(){
    string str, res;
    getline(cin, str);
    res = compress(str);
    cout << res << endl;
    return 0;
}