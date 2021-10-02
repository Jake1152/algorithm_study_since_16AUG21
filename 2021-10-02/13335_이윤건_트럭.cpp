#include "bits/stdc++.h"

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);
    
    int n,w,L,a[1000],time=1;
    queue<int> Q;
    cin>>n>>w>>L;
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int in=0,out=0;
    for(;;time++){
        if(Q.size() && time==w+Q.front()){ //나갈 트럭은 나간다.
            Q.pop();
            L+=a[out++];
        }
        if(in==n && Q.empty()) break;
        if(in<n && L>=a[in]){
            Q.push(time);//트럭이 진입한 시간.
            L-=a[in++];
        }
        else{ //더이상 추가할 트럭이 없는 경우
            time=Q.front()+w-1; //시간은 맨처음 들어간 트럭시간 + 다리길이
        }
        
    }
    cout<<time;
    
    return 0;
}
