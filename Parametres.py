

###############################################################################
###############################################################################
#       MODULE PARAMETRES
###############################################################################
###############################################################################




###############################################################################
#       IMPORT
###############################################################################


import os




###############################################################################
#       CONSTANTES / VARIABLES
###############################################################################


# Constantes
##################################

# Listes globales trouvées sur internet
LISTE_GLOBALE_PRENOMS = ["Alexandre", "Jean", "Eric", "Alban", "Philippe", "Anais", "Eleonor"]
LISTE_GLOBALE_EXTENSIONS = ["Créer une liste avec L'ENSEMBLE des extensions existantes"]

LISTE_VALEURS_CHOIX_OUI = ["oui", "o", "<Entree>", ""]


NB_LISTE_PARENTHESES_MIN = 1
NB_LISTE_PARENTHESES_MAX = 100

FICHIER_SUPPRIME = "fichier supprimé"



###############################################################################
#       CLASSES
###############################################################################


class Parametres:

	def __init__(self): 

		# Taux de match
		self.match_avec_parentheses = 0.65
		self.match_sans_parentheses = 0.85
		self.match_pre_pre_analyse = 0.15 # (non utilisé pour le moment)
		self.match_pre_analyse = 0.50
		self.match_taille_idem = 0.65

		# rep_parent
		self.rep_parent = os.getcwd()

		# Dossier doublons
		self.rep_doublon_sans_slash = "Dossier_doublons"
		self.rep_doublon_avec_slash = "/" + self.rep_doublon_sans_slash
		self.rep_doublon_existe = regarder_rep_doublon_existe(self.rep_parent, self.rep_doublon_avec_slash) 

		# Extensions à prendre en compte
		self.liste_extensions = [".pdf", ".doc", ".docx", ".odt", ".txt", ".rtf" ] # DICO_EXTENSIONS = {'.doc': 4, '.docx': 5, '.pdf': 4, ".odt":4, "":0}

		# liste_parentheses = ['(0)','(1)','(2)','(3)','(4)','(5)'...]
		self.nb_liste_parenthese_max = 21
		self.char_parenthese = ["", " ", "_", "-", "."]
		self.char_parenthese_ajout = ["copie", "copy"]
		liste_parentheses = list()
		liste_parentheses += ["copie", "copy"]
		for k in self.char_parenthese:
			liste_parentheses += ["{}({})".format(k, str(i)) for i in range(0, self.nb_liste_parenthese_max)]
			liste_parentheses += ["{}(0{})".format(k, str(i)) for i in range(0, self.nb_liste_parenthese_max)]
			liste_parentheses += ["{}(00{})".format(k, str(i)) for i in range(0, self.nb_liste_parenthese_max)]
				# ALLO ALLO T'UTLISE PAS LES REGEX, MAIS ALLO!!!!
		self.liste_parentheses = liste_parentheses


		self.modifier_parametres = False
		imprimer_dictionaire_objet(self)
		self.modifier_parametres = choix_modifier_parametres()


		if self.modifier_parametres:

			self.match_avec_parentheses = choix_match_avec_parentheses(self.match_avec_parentheses)
			self.match_sans_parentheses = choix_match_sans_parentheses(self.match_sans_parentheses)
			self.match_pre_pre_analyse = choix_match_pre_pre_analyse(self.match_pre_pre_analyse)
			self.match_pre_analyse = choix_match_pre_analyse(self.match_pre_analyse)
			self.match_taille_idem = choix_match_taille_idem(self.match_taille_idem)

			self.rep_parent = choix_rep_parent(self.rep_parent) 

			self.rep_doublon_sans_slash = choix_rep_doublon_sans_slash(self.rep_doublon_sans_slash)
			self.rep_doublon_avec_slash = "/" + self.rep_doublon_sans_slash
			self.rep_doublon_existe = regarder_rep_doublon_existe(self.rep_parent, self.rep_doublon_avec_slash)

			self.liste_extensions = choix_liste_extensions(self.liste_extensions ) # DICO_EXTENSIONS = {'.doc': 4, '.docx': 5, '.pdf': 4, ".odt":4, "":0}

			self.nb_liste_parenthese_max = choix_nb_liste_parenthese_max(self.nb_liste_parenthese_max)
			self.char_parenthese = choix_char_parenthese(self.char_parenthese)
			self.char_parenthese_ajout = choix_char_parenthese_ajout(self.char_parenthese_ajout)

			imprimer_dictionaire_objet(self)




###############################################################################
#       FONCTIONS
###############################################################################


def imprimer_dictionaire_objet(obj):

	print()
	print("*"*12)
	print("  Parametres  ")
	print("*"*12)
	print()

	if not obj.modifier_parametres : 
		texte = "Les Parametres par défaut sont"
	else:
		texte = "Les Nouveaux Parametres sont"

	print("{}, pour info : \n".format(texte))

	for cle, val in obj.__dict__.items(): 
		print("{} : {}".format(cle.replace("_", " ").capitalize(), str(val).replace("True", "Oui").replace("False", "Non")))

	print()
	print("*"*12)
	print()
	print()



def choix_bool(texte):
	rep = input("{}\nTappez {} pour Oui (majuscule ou minuscule), autre touche pour Non\n "\
		.format(texte, LISTE_VALEURS_CHOIX_OUI))

	if rep.lower() in LISTE_VALEURS_CHOIX_OUI:
		rep = True
	else :
		rep = False
	return rep


def choix_0_1(texte, attribut):
	valide = False
	choix = choix_bool(texte)

	while not valide:
		if choix : 
			nombre = input("Quel taux voulez-vous appliquer ? (C'est un pourcentage, donc un nombre entre 0 et 1)\n")
			try : 
				nombre = round(float(nombre),2)
				if nombre>0 and nombre<1:
					valide = True
					return nombre
				else : 
					print("Le nombre doit etre compris entre 0 et 1\n")
			except:
				print("Il nous faut un nombre\n")
		else:
			valide = True
			return attribut


def choix_modifier_parametres():
	texte = "Voulez-vous choisir vous meme les parametres ?"
	return choix_bool(texte)


def choix_match_avec_parentheses(attribut):
	texte ="Voulez-vous changer le taux de match pour un fichier comportant des parentheses ?"
	return choix_0_1(texte, attribut)


def choix_match_sans_parentheses(attribut):
	texte ="Voulez-vous changer le taux de match pour un fichier ne comportant pas de parentheses ?"
	return choix_0_1(texte, attribut)


def choix_match_pre_pre_analyse(attribut):
	texte ="Voulez-vous changer le taux de match pour une pré-pré analyse ?"
	return choix_0_1(texte, attribut)


def choix_match_pre_analyse(attribut):
	texte ="Voulez-vous changer le taux de match pour une pré analyse ?"
	return choix_0_1(texte, attribut)


def choix_match_taille_idem(attribut):
	texte ="Voulez-vous changer le taux de match deux fichiers de meme taille ?"
	return choix_0_1(texte, attribut)


def choix_rep_parent(attribut):
	texte = "Nous sommes actuellement dans le dossier {}, voulez vous le changer ?".format(attribut)
	choix = choix_bool(texte)

	if choix:
		valide = False
		while not valide:
			dossier = input("Veuillez entrer un chemin de dossier : '/home/Fred/Documents...' \n")
			try : 
				os.chdir(dossier)
				valide=True
				return dossier
			except : 
				print("Chemin incorrect\n")
	else : 
		valide = True
		return attribut


def choix_rep_doublon_sans_slash(attribut):
	texte = "Le dossier de doublon s'appelle actuellement {}, voulez vous le changer ?".format(attribut)
	choix = choix_bool(texte)

	if choix: 
		dossier = input("Veuillez entrer un nom de dossier, par exemple 'dossier doublons' \n")
		return dossier
	else:
		return attribut


def choix_liste_extensions(attribut):
	texte = "Les extensions autorisée sont actuellement {}, voulez vous les changer ?".format(attribut)
	choix = choix_bool(texte)

	if choix: 
		valide = False 
		while not valide:
			liste = input("Veuillez entrer une liste d'extension par exemple ['.pdf', '.doc'...]\n")
			try: 
				liste = eval(liste)
				
				if isinstance(liste, list) : 
					if (".pdf" or ".doc" or ".docx" or ".txt") in liste:
						valide = True
						return liste
					else:
						print("désolé, pas d'extension connus dedans\n")
				else:
					print("désolé, ca n'est pas une liste\n")
			except:
				print("désolé, ca n'est pas une liste\n")
	else:
		return attribut


def choix_nb_liste_parenthese_max(attribut):
	texte = "Au sein de nos parentheses, on monte jusqu'au chiffre {}, voulez vous le changer ?".format(attribut)
	choix = choix_bool(texte)

	if choix: 
		valide = False 
		while not valide:
			nb = input("choisissez un nombre entre {} et {}.\n".format(NB_LISTE_PARENTHESES_MIN, NB_LISTE_PARENTHESES_MAX))
			try :
				nb = int(nb)
				if nb>1 and nb<100:
					valide = True
					return nb
				else : 
					print("Désolé ton nombre est trop grand ou trop petit, ou les deux.\n")
			except:
				print("Désolé ton nombre n'est pas un nombre!\n")
	else:
		return attribut


def choix_char_parenthese(attribut):
	texte = "Les séparateurs précédents les parenthes sont actuellement {}, voulez vous les changer ?".format(attribut)
	choix = choix_bool(texte)

	if choix: 
		valide = False 
		while not valide:
			liste = input("Veuillez entrer une liste de séparateurs par exemple ['_', '-', '.'...]\n")
			try:	
				liste = eval(liste)
				
				if isinstance(liste, list) : 
					if ("." or "_" or "-" or " ") in liste:
						valide = True
						return liste
					else:
						print("désolé, pas de séparateurs connus dedans\n")
				else:
					print("désolé, ca n'est pas une liste\n")
			except:
				print("désolé, ca n'est pas une liste\n")
	else:
		return attribut


def choix_char_parenthese_ajout(attribut):
	texte = "Les parametres comme copie ou copy son de tres bons indicateurs d'un doublon, on a actuellement choisi \
	{}, voulez vous en changer ?".format(attribut)
	choix = choix_bool(texte)

	if choix: 
		valide = False 
		while not valide:
			liste = input("Veuillez entrer une liste de mots clés par exemple ['copie', 'copie']\n")
			try: 
				liste = eval(liste)
				if isinstance(liste, list) : 
					if ("copie" or "copy") in liste:
						valide = True
						return liste
					else:
						print("désolé, pas de mots clés connus dedans\n")
				else:
					print("désolé, ca n'est pas une liste\n")
			except:
				print("désolé, ca n'est pas une liste\n")
	else:
		return attribut


def regarder_rep_doublon_existe(doss_par, doss_doubl):

	if os.path.isdir(str(doss_par + doss_doubl)) : 
		print("Il y a deja un dossier {}, pas besoin de le créer\n".format(doss_doubl))
		return True
	else : 
		print("Il n'y a pas de dossier {}, il faudra le créer\n".format(doss_doubl))
		return False




###############################################################################
#       MAIN
###############################################################################


if __name__ == "__main__" : 
	para = Parametres()
