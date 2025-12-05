def prebroj_svjeze_sastojke(ulazni_tekst):
    """
    Obrada ulaza i brojanje svježih sastojaka.
    """

    # 1. Priprema ulaza: Dijelimo tekst na dva dijela
    try:
        # Dijeli cijeli tekst na dva dijela: (rasponi) i (dostupni ID-ovi)
        rasponi_tekst, dostupni_id_tekst = ulazni_tekst.strip().split('\n\n')
    except ValueError:
        print("Greška: Ulaz nije ispravno podijeljen praznim retkom.")
        return 0

    # 2. Pretvaranje raspona u brojeve
    svjezi_rasponi = []
    for linija_raspona in rasponi_tekst.strip().splitlines():
        if '-' in linija_raspona:
            pocetak_str, kraj_str = linija_raspona.split('-')
            # Spremanje raspona kao par brojeva (početak, kraj)
            svjezi_rasponi.append((int(pocetak_str), int(kraj_str)))

    # 3. Pretvaranje dostupnih ID-ova u brojeve
    dostupni_id = []
    for linija_id in dostupni_id_tekst.strip().splitlines():
        # Svaki redak je jedan ID sastojka
        dostupni_id.append(int(linija_id.strip()))

    # 4. Glavno brojanje
    brojac_svjezih = 0

    # KORAK A: Prolazimo kroz SVAKI sastojak koji imamo (ID)
    for ID_sastojka in dostupni_id:

        je_svjez = False  # Krećemo od pretpostavke da NIJE svjež

        # KORAK B: Za taj sastojak, provjeravamo SVE raspone svježine
        for pocetak, kraj in svjezi_rasponi:

            # PROVJERA: Je li ID sastojka unutar raspona?
            # (pocetak <= ID_sastojka <= kraj)
            if pocetak <= ID_sastojka <= kraj:
                je_svjez = True  # Pronašli smo da je svjež!
                break  # Prekidamo provjeru za ovaj ID i prelazimo na sljedeći

        # KORAK C: Ako je provjera potvrdila da je svjež, brojimo ga
        if je_svjez:
            brojac_svjezih += 1

    return brojac_svjezih


# Dio za čitanje iz datoteke i ispis
def main():
    IME_DATOTEKE = "input.txt"
    try:
        with open(IME_DATOTEKE, 'r') as f:
            ulazni_tekst = f.read()

        rezultat = prebroj_svjeze_sastojke(ulazni_tekst)

        print(f"👉 Čestitam! Broj svježih sastojaka je: {rezultat}")

    except FileNotFoundError:
        print(f"⚠️ Greška: Datoteka '{IME_DATOTEKE}' nije pronađena.")


if __name__ == "__main__":
    main()