

###############################################################################
###############################################################################
#       MODULE COPIER_COLLER_FICHIERS
###############################################################################
###############################################################################




###############################################################################
#       IMPORT
###############################################################################


import os
import shutil




###############################################################################
#       CONSTANTES / VARIABLES
###############################################################################




###############################################################################
#       CLASSES
###############################################################################




###############################################################################
#       FONCTIONS
###############################################################################

 
def creer_dossier_doublons(source, dossier):
	os.mkdir(source + "/" + dossier)


def copier_fichier(fi, source, dest):
		shutil.copy2(fi, str(source + "/" + dest))


def supprimer_fichier(fi, source):
	os.remove(source+"/"+fi)


def traiter_fichiers(liste, o, p):

	for i in range(len(liste.traitee)):

		if liste.doublons[i] != False : 

			if o.supprimer_doublons  : 
				if liste.doublons[i] == True : 
					supprimer_fichier(liste[i], repertoire_source)

			else :
				if o.deplacer_orginal and o.deplacer_doublons : 			 
						copier_fichier(fichier, repertoire_source, repertoire_destination)
						supprimer_fichier(fichier, repertoire_source)
				
				elif o.deplacer_doublons and not o.deplacer_original:
					if liste.doublons[i] == True : 
						copier_fichier(fichier, repertoire_source, repertoire_destination)
						supprimer_fichier(fichier, repertoire_source)
				
				else:
					input("probleme")
