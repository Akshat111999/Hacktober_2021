#include<iostream>
using namespace std;
int main(){
    int nrows;
    cout<<"enter number of rows: ";
    cin>>nrows;
    cout<<"\n";
    for(int i=1;i<=nrows;i++){
        for(int j=1;j<=i;j++){
            cout<<i*j<<" ";
        }
        cout<<"\n";
    }
}
