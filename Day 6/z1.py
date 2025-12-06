import re


def solve_worksheet(filepath='input.txt'):
   
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Greška: Datoteka '{filepath}' nije pronađena.")
        return None

   
    line_blocks = [line.rstrip('\n') for line in lines]

    if len(line_blocks) != 5:
        print(f"Greška: Očekuje se točno 5 redaka u ulaznoj datoteci, pronađeno {len(line_blocks)}.")
        return None

   
    segments = []
    for block in line_blocks:
       
        current_segments = re.findall(r'[^\s]+', block)
        segments.append(current_segments)

   
    num_problems = len(segments[0])

    if not all(len(s) == num_problems for s in segments):
        print("Greška: Redovi ne sadrže isti broj problema.")
        return None

   
    grand_total = 0

    for i in range(num_problems):
       

       
        num1 = int(segments[0][i])
        num2 = int(segments[1][i])
        num3 = int(segments[2][i])
        num4 = int(segments[3][i])  

       
        operator = segments[4][i]

        result = 0

        if operator == '+':
            result = num1 + num2 + num3 + num4
        elif operator == '*':
            result = num1 * num2 * num3 * num4
        else:
            print(f"Upozorenje: Nepoznati operator '{operator}' u problemu {i + 1}. Preskačem.")
            continue

        grand_total += result

    return grand_total



if __name__ == "__main__":
    final_total = solve_worksheet('input.txt')

    if final_total is not None:
        print("\n*** Rezultat ***")
        print(f"Veliki ukupni iznos (Grand Total) je: **{final_total}**")