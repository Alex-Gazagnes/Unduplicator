

###############################################################################
###############################################################################
#       MODULE COMPARER_DEUX_FICHIERS
###############################################################################
###############################################################################




###############################################################################
#       IMPORT
###############################################################################


import os




###############################################################################
#       CONSTANTES / VARIABLES
###############################################################################




###############################################################################
#       CLASSES
###############################################################################




###############################################################################
#       FONCTIONS
###############################################################################


def comparer_deux_fichiers(fi1, fi2, liste, option, parametre): 


	if option.mode_avance == False :
		if fi2.doublon == False:
			algo_normal(fi1, fi2, liste, option, parametre)

	else : 
		if fi2.doublon == False: 
			algo_de_ratrappage(fi1, fi2, liste, option, parametre)

	maj_liste(liste, fi1, fi2)



def algo_normal(fi1, fi2, liste, option, parametre):

	if (fi1.taille_oct == fi2.taille_oct) and fi1.taille_oct >0 and \
		(fi1.nom_sans_extension[0:int(fi1.taille_nom_sans_ext * parametre.match_taille_idem)] \
		== fi2.nom_sans_extension[0:int(fi1.taille_nom_sans_ext * parametre.match_taille_idem)]) :
		fi1.doublon,fi2.doublon = True, True

	if fi2.doublon == False:
		if (fi1.parentheses or fi1.parentheses) and \
			(fi1.nom_sans_extension[0:int(fi1.taille_nom_sans_ext * parametre.match_avec_parentheses)] \
			== fi2.nom_sans_extension[0:int(fi1.taille_nom_sans_ext * parametre.match_avec_parentheses)]) :
			fi1.doublon,fi2.doublon = True, True

	if fi2.doublon == False:
		if (fi1.nom_sans_extension[0: int(fi1.taille_nom_sans_ext * parametre.match_sans_parentheses)] \
			== fi2.nom_sans_extension[0:int(fi1.taille_nom_sans_ext * parametre.match_sans_parentheses)]) :
			fi1.doublon,fi2.doublon = True, True


def algo_de_ratrappage(fi1, fi2, liste, option, parametre):
	liste_char_conjoint_identique = [0]
	continuer_car_nb_char_conjoint_identique = True
	nb_char_conjoint_identique = 0
	fin_boucle = False
	nb_strat_boucle = 0
	nb_revalider_boucle = 4
	decalage_de_comp = 0
	declage_de_ref = 0


	if len(fi1.nom_sans_extension) > len(fi2.nom_sans_extension) :  # on va se baser sur le fichier au nom le plus court
		fichier_de_reference = fi2
		fichier_de_comapraison = fi1
	else : 
		fichier_de_reference = fi1
		fichier_de_comapraison = fi2

	"""boucle générale, on en sort que quand on parsé l'ensemble de fichier de reference .nom sans extension"""
	"""siily a char conjoint idem  on balaye le nom_sans_extension """		
	while (not fin_de_boucle) : 
		while continuer_car_nb_char_conjoint_identique and (not fin_de_boucle) : 
			for k in range(nb_strat_boucle, len(fichier_de_reference.nom_sans_extension) - math.abs(declage_de_ref -decalage_de_comp) ) :  

				if fichier_de_reference.nom_sans_extension[k + declage_de_ref] == fichier_de_comapraison.nom_sans_extension[k + decalage_de_comp] : 
					nb_char_conjoint_identique+=1 # DEJA aulieu de definir le niveau minimal on aura le socre pour chaque comparaisaon
						 
					if k == len(fichier_de_reference.nom_sans_extension) -1 : 
						fin_de_boucle = True # si on a fini de parser il faut sortir de la boucle principale
						continuer_car_nb_char_conjoint_identique = False 
						liste_char_conjoint_identique.append(nb_char_conjoint_identique)                
						
				else:
						continuer_car_nb_char_conjoint_identique = False 
						liste_char_conjoint_identique.append(nb_char_conjoint_identique)
						nb_char_conjoint_identique=0
						"""char_sur_lequel_on_bute = (fichier_de_reference.nom_sans_extension[k], k)"""
						
						if k == len(fichier_de_reference.nom_sans_extension) -1 :
							fin_de_boucle = True
				   
		while (not continuer_car_nb_char_conjoint_identique ) and (not fin_de_boucle) : #  chercher 1er nouveau coupe de char identique ... du coté de fichier_1 ou du coté de fichier_2
			for m in range(k, len(fichier_de_reference.nom_sans_extension) - (nb_revalider_boucle +1)) :
		
				if fichier_de_comapraison.nom_sans_extension[k:k+nb_revalider_boucle] == fichier_de_reference.nom_sans_extension[m:m+nb_revalider_boucle] : # on va parser le reste du mot à la recherche de 3 char conjoints identiques 
					decalage_de_comp +=  m-k
					continuer_car_nb_char_conjoint_identique = True 
					nb_strat_boucle
					break
						
				if not continuer_car_nb_char_conjoint_identique :  # si on a pas trouvé en parsant dans un sens.... 
							
					for m in range(k, len(fichier_de_reference.nom_sans_extension)- (nb_revalider_boucle +1)) :
						if fichier_de_comapraison.nom_sans_extension[m:m+nb_revalider_boucle] == fichier_de_reference.nom_sans_extension[k:k+nb_revalider_boucle]: # on va parser le reste du mot à la recherche de 3 char conjoints identiques 

							decalage_de_ref += m -k
							continuer_car_nb_char_conjoint_identique = True 
							nb_strat_boucle = k
								
							if m == len(fichier_de_reference.nom_sans_extension) - 1: 
								fin_de_boucle = True
							break
					break
	nb_match_1er_sequence = liste_char_conjoint_identique[0]
	nb_match_global = 0
	for n in liste_char_conjoint_identique:
		nb_match_global +=int(n)
	return nb_match_1er_sequence, nb_match_global
		

def maj_liste(liste, fi1, fi2 ): 

	if fi1.doublon == True : 
		if liste.doublons[fi1.numero] == False : liste.doublons[fi1.numero] = list()
		liste.doublons[fi1.numero].append(fi2)

	if fi2.doublon == True : 
		liste.doublons[fi2.numero] =True

""" A RETRAVAILLER"""
