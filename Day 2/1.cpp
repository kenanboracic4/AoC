#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;


bool isInvalidID(long long x) {
    string s = to_string(x);
    int n = s.size();

    
    for (int len = 1; len <= n/2; len++) {
        if (n % len != 0) continue; 

        int repeats = n / len;
        if (repeats < 2) continue; 

     
        string pattern = "";
        for (int i = 0; i < len; i++) {
            pattern += s[i];
        }

        string test = "";
        for (int i = 0; i < repeats; i++) {
            test += pattern;
        }

        if (test == s) {
            return true; 
        }
    }

    return false; 
}


vector<string> splitByComma(string s) {
    vector<string> result;
    string temp = "";

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == ',') {
            if (temp != "") result.push_back(temp);
            temp = "";
        } else {
            temp += s[i];
        }
    }

    if (temp != "") result.push_back(temp);

    return result;
}

int main() {

    ifstream file("input.txt");
    if (!file.is_open()) {
        cout << "Ne mogu otvoriti fajl input.txt" << endl;
        return 1;
    }

    string input = "";
    string line;
    while (getline(file, line)) {
        input += line; 
    }
    file.close();

    vector<string> ranges = splitByComma(input);
    long long suma = 0;

    for (int i = 0; i < ranges.size(); i++) {
        string r = ranges[i];

        
        string startStr = "";
        string endStr = "";
        bool beforeDash = true;

        for (int j = 0; j < r.size(); j++) {
            if (r[j] == '-') {
                beforeDash = false;
            } else {
                if (beforeDash) startStr += r[j];
                else endStr += r[j];
            }
        }

        long long start = stoll(startStr);
        long long end = stoll(endStr);

        
        for (long long id = start; id <= end; id++) {
            if (isInvalidID(id)) {
                suma += id;
            }
        }
    }

    cout << "Suma svih neispravnih ID-ova: " << suma << endl;
    return 0;
}
