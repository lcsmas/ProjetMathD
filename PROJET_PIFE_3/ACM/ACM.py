import csv

#On attribue arbitrairement des valeurs quantitatives aux notations qualitatives
eval = {
    "AR" : 0,
    "I" : 1,
    "P" : 2,
    "AB" : 3,
    "B" : 4,
    "TB" : 5
}

#Renvoi la note sous forme numérique que i a donné à j
def compute_note(i, j, notes):
    return eval.get(notes[i][j]) ;

#Indique si un individu appartient déjà à un groupe
def is_grouped(i):
    return i in grouped;

#Enregistre des données au format .csv dans le répertoire courant
def registerAsCSV(fileName, data):
    f = open(fileName +'.csv', '+w');
    csv_writer = csv.writer(f);
    for row in data:
        csv_writer.writerow(row);

#Récupération des données, début de l'algo
eleves = [];
notes = [];
groupes = [];
meilleurs_groupes = []
csvfile = open('../DONNEES/preferencesIG4MD.csv');
iterator = csv.reader(csvfile, delimiter=',');

#Construction de la matrice des élèves
for data in iterator :
    for el in data :
        eleves.append(el);
    break
eleves.pop(0);

#Construction de la matrice des notes
for note in iterator:
    note.pop(0);
    #On fait un uppercase pour corriger les erreurs de saisie
    note = list(map(lambda x : str.upper(x), note))
    notes.append(note);

#Construction de tous les groupes possibles de deux individus
#avec la note que chacun a donné à l'autre,
#leur score qui est leurs notes cumulées ainsi
#que l'écart entre les notes au carré
for i in range(0,len(eleves)):
    for j in range(0,len(eleves)):
        if(i!=j):
            note_i_j = compute_note(i, j, notes);
            note_j_i = compute_note(j, i, notes);
            score = note_i_j + note_j_i;
            ecart = (note_i_j - note_j_i) ** 2;
            groupes.append(
                [
                    eleves[i],
                    eleves[j],
                    note_i_j,
                    note_j_i,
                    score,
                    ecart
                ]);
groupes_sorted = \
    sorted(groupes, key=lambda x : x[4], reverse=True); #tri les groupes par score

#Construction de la matrice des meilleurs groupes
grouped = [];
while len(groupes_sorted) != 0:
    meilleurs_groupes.append(groupes_sorted.pop(0))
    grouped.append(meilleurs_groupes[len(meilleurs_groupes)-1][0]);
    grouped.append(meilleurs_groupes[len(meilleurs_groupes)-1][1]);
    groupes_sorted = list(filter(lambda x: not is_grouped(x[0]), groupes_sorted))
    groupes_sorted = list(filter(lambda x: not is_grouped(x[1]), groupes_sorted))

#Mise en forme des données pour une meilleure compréhension puis enregistrement
meilleurs_groupes.insert(0,['Elève 1','Elève 2',"Note attribué à l'élève 2 par l'élève 1", "Note attribué à l'élève 1 par l'élève 2", 'Notes cumulées', 'Ecart au carré']);
registerAsCSV('ACM', meilleurs_groupes);
