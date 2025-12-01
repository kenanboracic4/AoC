#include <iostream>
#include <string>

using namespace std;

int main() {
    string linija;
    long long trenutni = 50;
    long long brojac = 0;

    while (getline(cin, linija)) {
        if (linija.empty()) continue;

        char smjer = linija[0];
        long long x = stoll(linija.substr(1));

        long long start = trenutni;
        long long krozNulu = 0;

        if (smjer == 'R') {
            long long mod = start % 100;
            long long prvok = (100 - mod) % 100;
            if (prvok == 0) prvok = 100;

            if (prvok <= x)
                krozNulu = 1 + (x - prvok) / 100;

            trenutni = (start + x) % 100;
        }
        else if (smjer == 'L') {
            long long mod = start % 100;
            long long prvok = mod;
            if (prvok == 0) prvok = 100;

            if (prvok <= x)
                krozNulu = 1 + (x - prvok) / 100;

            trenutni = (start - (x % 100)) % 100;
            if (trenutni < 0) trenutni += 100;
        }

        brojac += krozNulu;

        
        if (krozNulu == 0 && trenutni == 0)
            brojac++;
    }

    cout << brojac << endl;
    return 0;
}
