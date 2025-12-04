import sys
import os


def provjeri_dostupnost(grid, r, c, visina, sirina):
    
    smjerovi = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    susjedne_role = 0

    for dr, dc in smjerovi:
        nr, nc = r + dr, c + dc

       
        if 0 <= nr < visina and 0 <= nc < sirina:
           
            if grid[nr][nc] == '@':
                susjedne_role += 1

    
    return susjedne_role < 4


def iterativno_ukloni_role(ulazni_fajl):
   
    try:
        with open(ulazni_fajl, 'r') as f:
            redovi = f.read().strip().split('\n')
    except FileNotFoundError:
        print(f"Greška: Datoteka '{ulazni_fajl}' nije pronađena.")
        sys.exit(1)

    

  
    grid = [list(red) for red in redovi]
    visina = len(grid)
    sirina = len(grid[0])
    ukupno_uklonjeno = 0

   
    while True:
        dostupne_za_uklanjanje = []

       
        for r in range(visina):
            for c in range(sirina):
                if grid[r][c] == '@':
                    if provjeri_dostupnost(grid, r, c, visina, sirina):
                       
                        dostupne_za_uklanjanje.append((r, c))

        if not dostupne_za_uklanjanje:
            break

       
        for r, c in dostupne_za_uklanjanje:
            grid[r][c] = '.'  

        broj_uklonjenih_u_krugu = len(dostupne_za_uklanjanje)
        ukupno_uklonjeno += broj_uklonjenih_u_krugu
        

    return ukupno_uklonjeno



ime_datoteke = 'input.txt'


if not os.path.exists(ime_datoteke):
    print(f"Greška: Datoteka '{ime_datoteke}' nije pronađena ")
    sys.exit(1)


rezultat = iterativno_ukloni_role(ime_datoteke)


print(f" **{rezultat}**")