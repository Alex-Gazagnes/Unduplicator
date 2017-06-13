

###############################################################################
###############################################################################
#       MODULE OPTIONS
###############################################################################
###############################################################################




###############################################################################
#       CONSTANTES / VARIABLES
###############################################################################


# Valeurs user input pour True
LISTE_VALEURS_CHOIX_OUI = ["oui", "o", "<Entree>", ""]
NB_DOSSIERS_DOUBLONS_MAX = 3




###############################################################################
#       CLASSES
###############################################################################


class Options : 
	def __init__(self):

		# On instancie un objet par défault
		self.verbose = True
		
		self.cleaner_nom = True
		self.liste_caracteres_cleaner_nom = ["-", " ", ".", "_"]
		
		self.mode_avance = False
		
		self.supprimer_doublons = False
		self.deplacer_doublons = True
		self.deplacer_original = True
		
		self.creer_un_seul_dossier_doublon = True
		
		# On demande une eventuelle MAJ
		self.modifier_options = False
		imprimer_dictionaire_objet(self)
		self.modifier_options = choix_modifier_options()

		# si oui, on MAJ
		if self.modifier_options : 

			self.verbose = choix_verbose()
			
			self.cleaner_nom = choix_cleaner_nom()
			self.liste_caracteres_cleaner_nom = choix_liste_caracteres_cleaner_nom()
			
			self.mode_avance = choix_mode_avance()

			self.supprimer_doublons = choix_supprimer_doublons()
			if self.supprimer_doublons : 
				self.deplacer_doublons = False
				self.deplacer_original = False
			else : 
				self.deplacer_original = choix_deplacer_original()
				self.deplacer_doublons = True
			self.creer_un_seul_dossier_doublon = choix_creer_un_seul_dossier_doublon()

			imprimer_dictionaire_objet(self)




###############################################################################
#       FONCTIONS
###############################################################################


def imprimer_dictionaire_objet(obj):


	print()
	print("*"*12)
	print("  Options  ")
	print("*"*12)
	print()

	if not obj.modifier_options : 
		texte = "Les Options par défaut sont"
	else:
		texte = "Les nouvelles Options sont"

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


def choix_modifier_options():
	texte = "Voulez-vous choisir-vous même les options ?"
	return choix_bool(texte)


def choix_verbose():
	texte = "Voulez-vous utiliser une option verbose qui imprime l'ensemble du detail de l'execution du script ?"
	return choix_bool(texte)


def choix_cleaner_nom():
	texte = "Voulez-vous cleaner et renommer le nom de chaque fichier à traiter? (FORTEMENT CONSEILLé)"
	return choix_bool(texte)


def choix_mode_avance():
	texte = "Voulez-vous faire appel au mode avancé ?"
	return choix_bool(texte)


def choix_liste_caracteres_cleaner_nom():
	return [" ", "-", "_", "."]


def choix_supprimer_doublons():
	texte = "Voulez-vous supprimer les fichiers doublonnés automatiquement ?"
	return choix_bool(texte)


def choix_deplacer_original():
	texte = "Voulez-vous deplacer le fichier original dans le dossier des doublons ?"
	return choix_bool(texte)


def choix_creer_un_seul_dossier_doublon():
	texte = "Voulez-vous creer un seul dossier doublons ?. (ou {}, traiment plus fin mais beaucoup plus lourd)"\
	.format(NB_DOSSIERS_DOUBLONS_MAX)
	return choix_bool(texte)




###############################################################################
#       MAIN
###############################################################################


if __name__ == "__main__" : 
	opt = Options()
