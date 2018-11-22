//Suma pares, impares y todos
#include <iostream>
using namespace std;
int main (){
    int numero;
    int x; x = 0;
    int y; y = 0;
    char exit;
    int i;
    cout << "Hasta que numero quieres que sume pares e impares ";
    cin >> numero;
    for (i=0; i<= numero; i++){
        if (i%2 == 0){
                     x = x + numero;}
        else{
                     y = y + numero;}
    }
    cout << "La suma de los numeros pares es: "; cout << x; cout << "\n";
    cout << "La suma de los numeros impares es: "; cout << y; cout << "\n";
    cout << "La suma de numeros pares e impares es: "; cout << x+y; cout << "\n";
    cin >> exit;
    return 0;
}
