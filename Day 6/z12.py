from functools import reduce
from operator import mul
import sys

def ucitaj_linije(putanja):
    # Čita sve linije iz fajla i uklanja \n na kraju
    with open(putanja, "r", encoding="utf-8") as f:
        return [linija.rstrip("\n") for linija in f.readlines()]

def podijeli_u_blokove(linije):
    # Izjednačava dužinu svih linija razmacima
    max_duzina = max(len(l) for l in linije)
    linije = [l.ljust(max_duzina) for l in linije]

    redovi = len(linije)
    kolone = max_duzina

    # Traži kolone koje su potpuno prazne (samo razmaci)
    razdvajac = [all(linije[r][c] == " " for r in range(redovi)) for c in range(kolone)]

    blokovi = []
    c = 0
    while c < kolone:
        if razdvajac[c]:
            c += 1
            continue
        
        pocetak = c
        while c < kolone and not razdvajac[c]:
            c += 1
        kraj = c - 1
        
        blokovi.append((pocetak, kraj))

    return linije, blokovi

def parsiraj_i_izracunaj(linije, blokovi):
    ukupan_zbir = 0
    redovi = len(linije)

    for (a, b) in blokovi:
        # Operator se nalazi u zadnjem redu bloka
        operatori = [linije[redovi-1][c] for c in range(a, b+1) if linije[redovi-1][c] != " "]
        
        if not operatori:
            raise ValueError(f"Nije pronađen operator u kolonama {a}-{b}")

        op = operatori[0]  # + ili *

        kolone_u_bloku = list(range(a, b+1))
        kolone_u_bloku.reverse()  # čitamo brojeve od desnog ka lijevom

        brojevi = []
        for c in kolone_u_bloku:
            # Uzimamo sve karaktere iznad operatora – prave broj
            cifre = "".join(linije[r][c] for r in range(redovi-1))
            cifre = cifre.strip()

            if cifre == "":
                continue

            brojevi.append(int(cifre))

        if not brojevi:
            continue

        # Izračunavanje bloka
        if op == "+":
            vrijednost = sum(brojevi)
        elif op == "*":
            vrijednost = reduce(mul, brojevi, 1)
        else:
            raise ValueError(f"Nepoznat operator '{op}' u bloku {a}-{b}")

        ukupan_zbir += vrijednost

    return ukupan_zbir

def main():
    putanja = "input.txt"
    try:
        linije = ucitaj_linije(putanja)
    except FileNotFoundError:
        print(f"Ne mogu pronaći '{putanja}'. Stavi ulaz u taj fajl i pokreni program.", file=sys.stderr)
        sys.exit(1)

    if len(linije) < 2:
        print("Ulaz mora imati barem dva reda.", file=sys.stderr)
        sys.exit(1)

    linije, blokovi = podijeli_u_blokove(linije)
    rezultat = parsiraj_i_izracunaj(linije, blokovi)
    print(rezultat)


if __name__ == "__main__":
    main()
