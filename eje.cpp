#include <iostream>
#include <string>
using namespace std;

int main() {
    string passwordCorrecto = "clave123";
    string intento;
    int intentos = 0;
    const int MAX_INTENTOS = 3;

    while (intentos < MAX_INTENTOS) {
        cout << "Ingrese el password: ";
        cin >> intento;

        if (intento == passwordCorrecto) {
            cout << "Acceso concedido!" << endl;
            break;
        } else {
            cout << "ERROR Password incorrecto." << endl;
            intentos++;
        }
    }

    if (intentos == MAX_INTENTOS) {
        cout << "Acceso denegado. Se agotaron los intentos." << endl;
    }

    return 0;
}
