//Todos pares e impares
#include <iostream>
using namespace std;
int main (){
    int limite;
    int i;
    char salida;
    for( i=0; i <=100; i++){
         if(i%2 == 0){
                cout << i;
                cout << " es par";
                cout << "\n";
                }
         else{
              cout << i;
              cout << " es impar";
              cout << "\n";
              }
}
     cin >> salida;
     return 0;         
}
              
