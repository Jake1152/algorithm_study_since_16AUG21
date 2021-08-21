#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int SW,ST,sex,num;
    bool arr_SW[101];
    
    
    cin>>SW;
    for(int i=1;i<=SW;i++){
        cin>>arr_SW[i];
    }
    cin>>ST;
    for(int i=0;i<ST;i++){
        cin>>sex>>num;
        if( sex==1 ){
            for(int j=num;j<=SW;j+=num)
                arr_SW[j]=!arr_SW[j];
            continue;
        }
        //sex==FEMALE
        arr_SW[num]=!arr_SW[num];
        for(int j=num+1,k=num-1; j<=SW && 0<k; j++,k--){
            if(arr_SW[j]==arr_SW[k]){
                arr_SW[j]=!arr_SW[j];
                arr_SW[k]=!arr_SW[k];
                continue;
            }
            break;
        }
    }
    for(int i=1;i<=SW;i++){
        cout<<arr_SW[i];
        if(i%20==0) cout<<'\n';
        else cout<<' ';
    }
    
    return 0;
}
