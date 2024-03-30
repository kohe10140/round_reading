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

using Matrix = vector<vector<int>>;

bool rc_zero(Matrix &mat){
    int m = mat.size();
    int n = mat[0].size();
    //先頭行・先頭列をフラグに使う
    for (int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            if(mat[i][j]==0){
                mat[0][j] = 0;
                mat[i][0] = 0;
            }
        }
    }
    //フラグにしたがって0に置換(先頭列は最後に置換)
    for(int j=1; j<n; j++){
        if(mat[0][j]==0){
            for (int i=1; i<m; i++) mat[i][j] = 0;
        }
    }
    for (int i=0; i<m; i++){
        if(mat[i][0]==0){
            for (int j=0; j<n; j++) mat[i][j] = 0;
        }
    }

    //先頭列を置換
    if(mat[0][0]==0){
        for (int i=1; i<m; i++) mat[i][0] = 0;
    }
    return true;
}


int main(){
    int M, N;
    cin >> M >> N;
    vector<vector<int>> mat(M, vector<int>(N));
    for (int i=0; i<M; i++){
        for(int j=0; j<N; j++){
            cin >> mat[i][j];
        }
    }
    rc_zero(mat);


    cout << endl;
    for (int i=0; i<N; i++){
        for(int j=0; j<N; j++){
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}