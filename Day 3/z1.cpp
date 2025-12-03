#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <fstream>

using namespace std;


const string IME_DATOTEKE = "input.txt"; 
const int DULJINA_TRZAJA = 12; 


string pronadiMaksimalniTrzaj(const string& red) {
  

    
    int brojZaIzbaciti = red.length() - DULJINA_TRZAJA;
    
    
    vector<char> rezultat;

    for (char trenutnaZnamenka : red) {
       
        while (!rezultat.empty() && brojZaIzbaciti > 0 && trenutnaZnamenka > rezultat.back()) {
            rezultat.pop_back(); 
            brojZaIzbaciti--;    
        }
        
      
        rezultat.push_back(trenutnaZnamenka);
    }

  
    while (rezultat.size() > DULJINA_TRZAJA) {
        rezultat.pop_back();
    }


    return string(rezultat.begin(), rezultat.end());
}

int main() {
    
    long double ukupniTrzaj = 0.0; 
    
  
    ifstream ulaznaDatoteka(IME_DATOTEKE); 


    
    string red;
    cout << "Čitanje podataka: " << IME_DATOTEKE << endl;
    cout << "------------------------------------------------------" << endl;

    // Čitanje red po red
    while (getline(ulaznaDatoteka, red)) {
        if (!red.empty() && red.length() >= DULJINA_TRZAJA) {
            
            string maxTrzajString = pronadiMaksimalniTrzaj(red);
            
           
            try {
                long double maxTrzajVrijednost = stold(maxTrzajString);
                ukupniTrzaj += maxTrzajVrijednost;
            } catch (const std::exception& e) {
                 cerr << "greska " << maxTrzajString << endl;
            }
        }
    }
    
    ulaznaDatoteka.close();

  
    cout << "Ukupnp: " << fixed << (long long)ukupniTrzaj << endl;
    
    return 0;
}