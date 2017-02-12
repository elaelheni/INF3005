# coding: utf8
import random

print "Nouvelle partie de HILO"
mystery_number = random.randint(1, 100)

tries = 10
found = False
while tries > 0 and found is False:
    print "Entrer un nombre entre 1 et 100"
    user_entree = int(raw_input())
    if user_entree > mystery_number:
        print "Trop grand"
    elif user_entree < mystery_number:
        print "Trop petit"
    else:
        print "Vous avez gagné!"
        found = True
    tries -= 1
if tries == 0 and found is False:
    print "Vous avez perdu!"
