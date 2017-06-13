

###############################################################################
###############################################################################
#       MODULE LISTEFICHIERS
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


class ListeFichiers:
	
	def  __init__(self, dossier, dossier_doublon_existe, dossier_doublon_sans_slash, renommer_fichier,liste_caracteres) :

		self.originale = os.listdir(dossier)

		self.traitee = sorted(self.originale)
		if dossier_doublon_existe : self.traitee.remove(dossier_doublon_sans_slash)

		self.doublons = list()
		for i in self.traitee : 
			self.doublons.append(False)
		
		somme_tailles = 0
		for i in self.traitee : 
			somme_tailles += len(str(i))
		self.moyenne_taille_nom= round(somme_tailles / len(self.traitee),2)


		if renommer_fichier : 
			print("Option renomer_fichier = True, donc on va MAJ le nom des fichiers")
			maj_renommer_fichier(self, liste_caracteres)


		imprimer_dictionaire_objet(self)




###############################################################################
#       FONCTIONS
###############################################################################


def maj_renommer_fichier(obj, liste):
		# On peut renommer les fichier mais
		# attention, le "." a une signification particuliere, il ne faut pas
		# le supprimer s'il s'agit de l'extension

	if "." not in liste : 
		for i in range(len(obj.traitee)):

			for j in liste : 
				os.rename(obj.traitee[i], obj.traitee[i].replace(j,"_"))
				obj.traitee[i] = \
				obj.traitee[i].replace(j, "_")

	else : 
		for i in range(len(obj.traitee)) : 

			if "." not in obj.traitee[i][-5:]: 

				for j in liste : 
					os.rename(obj.traitee[i], obj.traitee[i].replace(j,"_"))
					obj.traitee[i] = \
					obj.traitee[i].replace(j, "_")
				
			else :
				for j in liste :
					os.rename(obj.traitee[i], str( \
						obj.traitee[i][:len(obj.traitee[i])-5].replace(j,"_")) \
						+ obj.traitee[i][-5:])
					
					obj.traitee[i] = str(\
						obj.traitee[i][:len(obj.traitee[i])-5].replace(j, "_") \
						+obj.traitee[i][-5:])



def imprimer_dictionaire_objet(obj):

	texte = "Les attributs de la ListeFichier sont"

	texte_dictionnaire = str(obj.__dict__)
	texte_dictionnaire = texte_dictionnaire.replace("True","Oui")
	texte_dictionnaire = texte_dictionnaire.replace("False","Non")
	texte_dictionnaire = texte_dictionnaire.replace("_"," ")

	print("{}, pour info : {}\n".format(texte, texte_dictionnaire))




###############################################################################
#       MAIN
###############################################################################



if __name__ == "__main__" : 
	liste_fichier = ListeFichiers(os.getcwd(),\
	False, \
	"dossier doublons", \
	True,\
	[".","-"," ","  ",";","_"])
