#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int p,q;
    cin>>p>>q;
    int a[p][q];
    int rot;
    cin>>rot;
                  
   for ( int i = 0; i < p; i++ )
      for ( int j = 0; j < q; j++ ) {
                 cin>>a[i][j];
      }
    
   int iter=(min(p,q)/2);
        
   int mx,my;
    mx=p;
    my=q;
   int rotation_same,rotation;
    
for(int k=0;k<iter;k++){
    

    
     rotation_same=2*(mx+my-2);
     rotation=rot%rotation_same;
     
for(int num=0;num<rotation;num++){        
    int i,j;
        i=k;
        j=k;
    int temp=a[k][k];
    a[i][j]=a[i][j+1];
    j=k+1;    
    start1:    
    if(j!=(q-1-k)){
            a[i][j]=a[i][j+1];
            j=j+1;
            goto start1;
        } 
    start2:
    if(j==(q-1-k) && i!=(p-1-k)){
            a[i][j]=a[i+1][j];
            i=i+1;
        goto start2;
        }    
    if(j==(q-1-k) && i==(p-1-k)){
           start3: 
        a[i][j]=a[i][j-1];
            j=j-1;
        if(j>k)
            goto start3;
        }
    
    if(i==(p-1-k) && j==k){
        start4:
        a[i][j]=a[i-1][j];
        i=i-1;
        if(i>k)
            goto start4;
    }
    
    if(i==k && j==k){
        a[i+1][j]=temp;
    }
}  
        
           mx=mx-2;
           my=my-2;  
        
}
   

    
    
    
    
    
    
    
    
        for ( int i = 0; i < p; i++ ){
      for ( int j = 0; j < q; j++ ) {
                 cout << a[i][j]<< " ";
      }
        cout<<endl;
     }
    
       
    
    
    return 0;
}

