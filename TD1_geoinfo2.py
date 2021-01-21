import random
import os
import webbrowser
Length = 4
nombredecoups = 3
Index = (["0","1", "2", "3", "4", "5", "6", "7", "8", "9"])
b = [" " + str(x) for x in range(Length)]
Random = []
List_index = []
j = 0
count = 1

def randomselection():
    a = (random.choices(Index, k=Length))
    a_Index = [x + " " + str(a.index(x)) for x in a]
    c = [x + y for x, y in zip(a, b)]
    return c

def fonctioncaractère():
    i = 0
    while i < 1:
        Input = str(input("Entrez votre guess à 4 caractères : "))
        List = [x for x in str(Input)]
        check = all(item in Index for item in List)
        if check is False:
            print("Les caractères sélectionnés ne sont pas contenus dans la liste")
            i = 0
        else:
            if len(Input) == Length:
                Liste_a = [x + y for x, y in zip(List, b)]
                i +=1
            elif len(Input) < Length:
                print("Le nombre de caractères est insuffisant ")
                i = 0
            else :
                print("Le nombre de caractères dépasse la limite ")
                i = 0
    return Liste_a

Random = randomselection()
print (Random)
while j == 0:
    List_index = fonctioncaractère()
    l3 = [x for x in Random if x not in List_index]
    Misplaced = str((len(l3)))
    Wellplaced = str(Length - len(l3))

    if len(l3) == 0:
        print("count : %c" % str(count))
        print("%a bien placés, %a mal placé" % (Wellplaced, Misplaced))
        os.system("say 'Félicitation vous avez remporté la partie en %a essaies'" % (count))
        j += 1

    elif len(l3) < 4 and len(l3) > 1:
        print("count : %c" % str(count))
        print("%a bien placés, %a mal placés" % (Wellplaced, Misplaced))
        j = 0
        count += 1

    elif count < (nombredecoups):
        print("count : %c" % str(count))
        print("%a bien placé, %a mal placés" % (Wellplaced, Misplaced))
        j = 0
        count += 1

    else:
        os.system("say 'Félicitation vous êtes un gros cave comme Benoit'")
        webbrowser.open('https://www.facebook.com/photo?fbid=1978429362193193&set=a.145388685497279', new=2)

        j += 1

