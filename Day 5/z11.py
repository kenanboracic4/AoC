def spoji_raspore(rasponi):
    """
    Sortira raspone i spaja one koji se preklapaju ili dodiruju.
    Ovo rješava problem prevelikih raspona jer radi samo s granicama.

    Args:
        rasponi (list): Popis parova (pocetak, kraj).

    Returns:
        list: Popis spojenih, nepreklapajućih raspona.
    """
    if not rasponi:
        return []

    # Sortiranje po početku raspona
    rasponi.sort(key=lambda x: x[0])

    spojeni = []
    trenutni_pocetak, trenutni_kraj = rasponi[0]

    # Prolazimo kroz ostale raspone
    for sljedeci_pocetak, sljedeci_kraj in rasponi[1:]:

        # Ako se rasponi preklapaju ili dodiruju (kraj + 1 >= sljedeci_pocetak)
        # Npr. (3, 5) i (6, 10) se dodiruju. (3, 5) i (5, 10) se preklapaju
        if trenutni_kraj >= sljedeci_pocetak - 1:
            # Spajanje: produžujemo trenutni kraj na maksimum oba kraja
            trenutni_kraj = max(trenutni_kraj, sljedeci_kraj)
        else:
            # Ne preklapaju se, spremamo trenutni i započinjemo novi
            spojeni.append((trenutni_pocetak, trenutni_kraj))
            trenutni_pocetak, trenutni_kraj = sljedeci_pocetak, sljedeci_kraj

    # Dodajemo posljednji spojeni raspon
    spojeni.append((trenutni_pocetak, trenutni_kraj))
    return spojeni


def prebroji_ukupno_svjeze_id_optimizirano(ulazni_tekst):
    """
    Računa ukupan broj jedinstvenih svježih ID-ova koristeći spajanje intervala.
    """

    tekst_normaliziran = ulazni_tekst.replace('\r\n', '\n').replace('\r', '\n')
    dijelovi = tekst_normaliziran.strip().split('\n\n')

    if not dijelovi: return 0

    rasponi_linije = dijelovi[0].strip().split('\n')
    svjezi_rasponi = []

    # 1. Parsiranje raspona
    for linija in rasponi_linije:
        linija = linija.strip()
        if not linija or '-' not in linija: continue

        try:
            pocetak, kraj = map(int, linija.split('-'))
            # Normalizacija: uvijek (manji, veći)
            svjezi_rasponi.append((min(pocetak, kraj), max(pocetak, kraj)))
        except ValueError:
            continue

    # 2. Spajanje preklapajućih raspona
    spojeni_rasponi = spoji_raspore(svjezi_rasponi)

    # 3. Zbrajanje duljina spojenih raspona
    ukupan_broj_svjezih = 0
    for pocetak, kraj in spojeni_rasponi:
        # Broj ID-ova u rasponu [pocetak, kraj] je (kraj - pocetak + 1)
        ukupan_broj_svjezih += (kraj - pocetak + 1)

    return ukupan_broj_svjezih


def main():
    IME_DATOTEKE = "input.txt"
    try:
        with open(IME_DATOTEKE, 'r', encoding='utf-8') as f:
            ulazni_tekst = f.read()

        rezultat = prebroji_ukupno_svjeze_id_optimizirano(ulazni_tekst)

        print(f"✅ UKUPAN BROJ JEDINSTVENIH SVJEŽIH ID-OVA JE (optimizirano): {rezultat}")

    except FileNotFoundError:
        print(f"❌ Greška: Datoteka '{IME_DATOTEKE}' nije pronađena.")
    except Exception as e:
        print(f"❌ Dogodila se neočekivana greška: {e}")


if __name__ == "__main__":
    main()