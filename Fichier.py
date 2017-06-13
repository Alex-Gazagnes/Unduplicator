
###############################################################################
###############################################################################
#       MODULE FICHIER
###############################################################################
###############################################################################




###############################################################################
#       IMPORT
###############################################################################


import os
from ListeFichiers import * 




###############################################################################
#       CONSTANTES / VARIABLES
###############################################################################




###############################################################################
#       CLASSES
###############################################################################



class Fichier : 
	def __init__(self, numero, nom, chemin, liste_extensions, liste_parentheses):
		# attributs d'instances, inchangeable
		self.nom = str(nom)
		self.numero = int(numero)
		self.nom_sans_casse = self.nom.lower()
		self.nom_sans_extension, self.extension = split_nom_extension(self.nom_sans_casse, liste_extensions)

		self.chemin = chemin

		self.taille_oct = os.path.getsize(str(str(chemin) + "/" + str(nom)))
		self.taille_nom_sans_ext = len(self.nom_sans_extension)
		
		self.doublon = False
		self.taux_doublons = list()
		self.supprime_dans_liste = False

		self.parentheses = identifier_parentheses(self.nom_sans_extension, liste_parentheses)

		self.liste_mots_supposes = split_mots_supposes(self.nom_sans_extension)

		imprimer_dictionaire_objet(self)




###############################################################################
#       FONCTIONS
###############################################################################


def imprimer_dictionaire_objet(obj):

	texte = "Les attributs du Fichier {} sont".format(obj.nom)

	texte_dictionnaire = str(obj.__dict__)
	texte_dictionnaire = texte_dictionnaire.replace("True","Oui")
	texte_dictionnaire = texte_dictionnaire.replace("False","Non")
	texte_dictionnaire = texte_dictionnaire.replace("_"," ")

	print("{}, pour info : {}\n".format(texte, texte_dictionnaire))


def split_nom_extension(attribut, liste_extensions):
	
	for i in liste_extensions: 
		if i.lower() in attribut[-6:] : # si une extension connue est deja dans le nom du fichier
			# encore faut il qu'il y soit dans les 5 derniers char, disons 6 pour etre confort ! 
			ext = str(i)
			nom_sans_ext = attribut[:len(attribut) - len(ext)]
			return nom_sans_ext, ext

	if "." not in attribut : 
		nom_sans_ext = attribut
		ext = ""
		return nom_sans_ext, ext


	if "." in attribut[-6:]:
		if ((attribut[-1].isalnum()) \
			and (attribut[-2].isalnum() or attribut[-2] == ".") \
			and (attribut[-3].isalnum() or attribut[-3] == ".") \
			and (attribut[-4].isalnum() or attribut[-4] == ".") \
			and (attribut[-5].isalnum() or attribut[-5] == ".")) : 

			# sous sujet, si c'est un doc de type 13445.134445.132 aie
			if attribut[-2].isnumeric() and attribut[-1].isnumeric():
				nom_sans_ext = attribut
				ext = "" # on exclus donc les exetensions en 3 chiffres
				return nom_sans_ext, ext
			else : 
				# sinon on traite l'extension
				nb = str(attribut).find(".", len(attribut)-5)
				nom_sans_ext = attribut[:nb]
				ext = attribut[nb:]
				return nom_sans_ext, ext

	else : 
		nom_sans_ext = attribut
		ext = ""
		print("par dépit, on ne met pas d'ext...")
		return nom_sans_ext, ext


def identifier_parentheses(attribut, liste_parentheses):

	if ("(" in attribut) and (")" in attribut) :
		for element in liste_parentheses :
			if element in attribut : 
				return True
					

def split_mots_supposes(attribut):
	return False 




###############################################################################
#       MAIN
###############################################################################



if __name__ == "__main__" : 

	nom_test = "blabla-car 12.dj"

	open(nom_test, "w").close()

	liste_fichier = ListeFichiers(
		os.getcwd(),\
		False, \
		"dossier doublons", \
		True,\
		[".","-"," ","  ",";","_"])

	fichier = Fichier(
		0,  \
		liste_fichier.traitee[0], \
		os.getcwd(), \
		[".doc",".pdf",".docx",".odt",".rtf", ""], \
	 	["(1)","(2)","(3)","(4)","(5)","(6)","(7)","(8)","(9)"])
