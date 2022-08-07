# Benötigte Module einbinden
import itertools

# Gibt von einer Liste alle möglichen Kombinationen der einzelnen Elemente aus; braucht import itertools
def mogl_combs_combs(zelle):
    mogl_combs = [''.join(map(str, comb)) for comb in itertools.combinations(zelle, anzahl_betrachtete_merkmale)]
    mogl_combs = [n for n in mogl_combs if len(set(n.lower())) == len(n.lower())]
    return mogl_combs

# Sortert Liste nach abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
def sort_list(zelle):
    zelle_sorted = []
    abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    for let in abc:
        if let in zelle:
            anzahl_allele = zelle.count(let)
            for i in range(anzahl_allele):
                zelle_sorted.append(let)
    return zelle_sorted

# Sortiert String nach abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
def sort_string(zelle):
    zelle = list(zelle)
    zelle_sorted = []
    final = ""
    abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    for let in abc:
        if let in zelle:
            anzahl_allele = zelle.count(let)
            for i in range(anzahl_allele):
                zelle_sorted.append(let)
    for n in zelle_sorted:
        final = final + n
    return final

# Zählt die Häufigkeit von Elementen in einer Liste; Output = ["element1", "count1", "element2", ...]
def counter(list):
    output_list = []
    for dot in sorted(set(list), key=list.index):
        output_list.append(dot)
        output_list.append(list.count(dot))
    return output_list

# Zählt die Großbuchstaben in einem String (wird nur unten zum sortieren gebraucht)
def capital_count(sub):
    return len([ele for ele in sub if ele.isupper()])

# Anzahl der betrachteten Allele eingeben
anzahl_betrachtete_merkmale = int(input("Anzahl der betrachteten Merkmale: "))

# Allele eingeben und zusammen mit Buchstaben in Liste
betrachtete_merkmale = []
betrachtete_Allele = []
merkmal_count = 1
allel_count = 1
for merkmal in range(anzahl_betrachtete_merkmale):
    betrachtete_merkmale.append(input(f"Merkmal {merkmal_count}: "))
    for allel in range(2):
        betrachtete_Allele.append(input(f"Allel {allel_count}: "))
        betrachtete_Allele.append(input(f"Allel {allel_count} Buchstabe: "))
        allel_count += 1
    allel_count = 1
    merkmal_count += 1

# Zellen als Buchstaben eingeben
zelle_1 = input("Zelle 1: ")
zelle_2 = input("Zelle 2: ")

# Sortiert Zellen mit der Funktion oben nach abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
zelle_1_sorted = sort_list(zelle_1)
zelle_2_sorted = sort_list(zelle_2)

# Gibt mit der Funktione oben von einer Liste alle möglichen Kombinationen der einzelnen Elemente aus; braucht import itertools
mogl_combs_zelle_1 = mogl_combs_combs(zelle_1_sorted)
mogl_combs_zelle_2 = mogl_combs_combs(zelle_2_sorted)

# Berechnet die Anzahl der möglichen Kombinationen
mogl_combs_count = 2**anzahl_betrachtete_merkmale

# Fusioniert die Möglichkeiten reihenweise; Form = [["element1"], ["element2"], ...]
fuselist = []
for k in mogl_combs_zelle_2:
    for i in mogl_combs_zelle_1:
        fuselist.append([k+i])

# Bringt die Liste in die Form von matplotlib
finaldata = []
for m in range(len(fuselist))[::mogl_combs_count]:
    save = []
    for n in range(mogl_combs_count):
        save += fuselist[m+n] 
    finaldata.append(save)

# Sortiert mit der Funktion oben die einzelnen Elemente nach abc = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
for p in range(len(finaldata)):
    finaldata[p] = [sort_string(f) for f in finaldata[p]]

# Bringt die Liste eine bessere Form; Form = ["element1", "element2", ...]
countlist = []
for p in finaldata:
    for o in p:
        countlist.append(o)
geno_numberlist = counter(countlist)

# Wählen zwischen dominant und rezessiv - Ersetzt beide Buchstaben mit Großbuchstabe wenn dominant und Kleinbuchstabe wenn rezessiv
phanolist = []
for element in countlist:
    splitted = [element[i:i + 2] for i in range(0, len(element), 2)]
    new_tile = ""
    for tile in splitted:
        upper = 0
        for letter in tile:
            if letter.isupper():
                upper += 1
        if upper != 0:
            new_tile += tile.replace(tile, list(tile)[0].upper())
        else:
            new_tile += tile.replace(tile, list(tile)[0].lower())
    phanolist.append(new_tile)

# Phänotypen sortiert in Listen speichern
phano_numberlist = counter(phanolist) # Liste Phänotyp + Anzahl | Beispiel: ["ABC", "27", "AbC", "9", ...]
phano_blick = [] # Liste Phänotyp | Beispiel: ["ABC", "AbC", ...]
phano_zahl = [] # Anzahl der Phänotypen als Liste | Beispiel: ["27", "9", ...]
for u in phano_numberlist[::2]:
    phano_blick.append(u)
for u in phano_numberlist[1::2]:
    phano_zahl.append(u)
phano_blick.sort(key=capital_count, reverse=True)
phano_zahl.sort(reverse=True)

# Allelbuchstaben mit Allelen ersetzten
verbessert = []
for i in phano_blick:
    saver = []
    for m in i:    
        m = m.replace(betrachtete_Allele[betrachtete_Allele.index(m)], betrachtete_Allele[betrachtete_Allele.index(m)-1])
        saver.append(m)
    saver = ", ".join(saver)
    verbessert.append(saver)

#importieren der module für die tabelle
import matplotlib.pyplot as plt
import os

# Erstellen der Tabelle
def draw_table():
    the_table = plt.table(cellText=finaldata,
                        colWidths=[0.1] * mogl_combs_count,
                        rowLabels=mogl_combs_zelle_2,
                        colLabels=mogl_combs_zelle_1,
                        loc='center')
    the_table.set_fontsize(mogl_combs_count*5)
    the_table.scale(mogl_combs_count, mogl_combs_count)

# koordinatensystem entfernen
def rem_kords():
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.tick_params(axis='y', which='both', right=False, left=False, labelleft=False)
    for pos in ['right','top','bottom','left']:
        plt.gca().spines[pos].set_visible(False)
    plt.savefig('matplotlib-table.png', bbox_inches='tight', pad_inches=0.05)

# Funktionen rufen
draw_table()
rem_kords()

# Erstellung und Gestaltung der Text-File
user = os.getlogin()
file = open(f"C:/Users/{user}/Desktop/file.txt","w")

file.write(f"Betrachteten Merkmale ({anzahl_betrachtete_merkmale}): \n")
for i in range(len(betrachtete_Allele))[::4]:
    file.write(f"{betrachtete_merkmale[int(i/4)]}: {betrachtete_Allele[i]} ({betrachtete_Allele[i+1]}), {betrachtete_Allele[i+2]} ({betrachtete_Allele[i+3]})\n")
file.write("\n")
for h in zelle_1_sorted:
    file.write(h)
file.write(" x ")
for r in zelle_2_sorted:
    file.write(r)
file.write("\n")
file.write("Verhältnisse: \n")
file.write("Genotypenverhältnis: \n")
for j in range(len(geno_numberlist))[::2]:
    genotypenverhältnis = geno_numberlist[j] + ": " + str(geno_numberlist[j+1]) + "/"+ str(mogl_combs_count**2)
    file.write(f"{genotypenverhältnis}\n")
file.write("\n")
file.write("Phänotypenverhältnis: \n")
for c in range(len(verbessert)):
    phänotypenverhältnis = verbessert[c] + ": " + str(phano_zahl[c]) + "/" + str(mogl_combs_count**2)
    file.write(f"{phänotypenverhältnis}\n")

file.close()

# Tabelle auf dem Desktop anstatt von in user speichern
os.replace(f"C:/Users/{user}/matplotlib-table.png", f"C:/Users/{user}/Desktop/matplotlib-table.png")

##########################################
# Made by Welf Baumann and Ole Ahrenhold #
##########################################