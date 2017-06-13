

###############################################################################
###############################################################################
#       MAIN
###############################################################################
###############################################################################




###############################################################################
#       IMPORT
###############################################################################


from Options import * 
from Parametres import * 
from ListeFichiers import * 
from Fichier import *
from Comparer_deux_fichiers import * 
from Copier_coller_fichiers import * 
from Textes import *
import os




###############################################################################
#       MAIN
###############################################################################


# Inputs, options et parametres
o = Options()
p = Parametres()


# Creation d'une liste avec tous nous fichiers
liste_fichiers = ListeFichiers(p.rep_parent, \
	p.rep_doublon_existe, \
	p.rep_doublon_avec_slash, \
	o.cleaner_nom, \
	o.liste_caracteres_cleaner_nom)

# Identifier les doublons
for i in range(len(liste_fichiers.traitee)):
	fichier_1 = Fichier(i, \
		liste_fichiers.traitee[i],\
		p.rep_parent,\
		p.liste_extensions, \
		p.liste_parentheses)

	if (fichier_1.extension in p.liste_extensions) \
		and (liste_fichiers.doublons[i] == False): 

		print("\t{} est à comparer car son ext est valide!  \n".format(fichier_1.nom))

		for j in range(i, len(liste_fichiers.traitee)) : 
			fichier_2 = Fichier(j, \
				liste_fichiers.traitee[j],\
				p.rep_parent,\
				p.liste_extensions,\
				p.liste_parentheses)

			if fichier_2.extension in p.liste_extensions \
				and (j>i) \
				and (liste_fichiers.doublons[j] == False):

				print("\t\t{} est à comparer avec {}!  \n".format(fichier_2.nom ,fichier_1.nom))

				comparer_deux_fichiers(fichier_1, 
					fichier_2, \
					liste_fichiers, \
					o,\
					p)

				print("apres comparaison de {} et {}, on a donné comme valeur doublon {} et {} ".format(fichier_1.nom , fichier_2.nom, fichier_1.doublon, fichier_2.doublon))
				input()


print(liste_fichiers.traitee)
input()

print(liste_fichiers.doublons)
input()


# Traiter les doublons
if True in liste_fichiers.doublons : 
	if not dossier_doublons_existe :
		creer_dossier_doublons()
	else fichier_doublon = p.fichier_doublon
	traiter_fichiers(liste_fichiers, o, p)


