//Tablas multiplicar
#include <iostream>
using namespace std;
int main()
{
    int i;
    int numero;
    char salida;
    cout << "Que tabla quieres que haga";
    cin >> numero;
    for(i=1;i<=10;i++){
                      cout << i;
                      cout << " x ";
                      cout << numero;
                      cout << " = "; 
                      cout << i*numero;
                      cout << "\n";
    }
    cout << "Toca cualquier tecla para salir";
    cin >> salida;
    
    
}
