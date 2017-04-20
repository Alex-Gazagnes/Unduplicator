os.path.isfile(path) renvoie True si path désigne un fichier existant

test pour  comaprer cv alexandre GAZAGNES et cv alxandre GAZAGNES :
on veut en valeur de retour 5 et 15 car la 1er partie comporte une suiet  de 5 lettres identifques et la deuxieme une suite de 15
du coup 5 + 15  = 20 --> sur 21 lettres : 100% de changes que ca soit le meme nom ! 
	
	suite_char_conjoint_identique = [5, 15 ]
	suite_char_conjoint_identique.append(nb_char_conjoint_identique )
	
	suite_char_conjoint_identique = list()
	continuer_car_nb_char_conjoint_identique = True
	nb_char_conjoint_identique = 0
	fin_boucle = False
	nb_strat_boucle = 0
	
	if len(fichier_1.nom_sans_extension) > len(fichier_2.nom_sans_extension) :  # on va se baser sur le fichier au nom le plus court
		fichier_de_reference = fichier_2
		fichier_de_comapraison = fichier_1
	else : 
		fichier_de_reference = fichier_1
		fichier_de_comapraison = fichier_2
	
	while not fin de boucle: # boucle générale, on en sort que quand on parsé l'ensemble de Fichier_1.nom_sans extension
		while continuer_car_nb_char_conjoint_identique 	: # tant que il y a char conjoint idem  on balaye le nom_sans_extension 
			for k in range(nb_strat_boucle, len(fichier_de_reference.nom_sans_extension)) :  

			      	if fichier_1.nom_sans_extension[k] == fichier_2.nom_sans_extension[k] : 
				 	nb_char_conjoint_identique+=1 # DEJA aulieu de definir le niveau minimal on aura le socre pour chaque comparaisaon
			       		continuer_car_nb_char_conjoint_identique = True 
			       	else:
			       		continuer_car_nb_char_conjoint_identique = False 
		       			suite_char_conjoint_identique.append(nb_char_conjoint_identique)
			       		nb_char_conjoint_identique=0
		       
				else : #  chercher 1er nouveau coupe de char identique ... du coté de fichier_1 ou du coté de fichier_2
		       	char_sur_lequel_on_bute = fichier_1.nom_sans_extension[k]
		       while : fichier_1.nom_sans_extension[k]




INTRO_TITRE = """

###############################################################
###############################################################

Script de dédoublonnage de fichiers dans un dossier spécifique

###############################################################
###############################################################

v1.0.1
20/04/2017
Alexandre GAZAGNES
v SANS GUI

Description : trop de doublons ? Ras le bol des fichier en 4 exemplaires, d'avoir votre
votre "cv Prenom Nom", "cv Prenom Nom-1" "cv Prenom Nom ok" "cv Prenom Nom (1)"
ou "cv Prenom Nom 2016"

Ce programme est fait pour vous. 

Dans un dossier (mais pas dans ses sous dossiers - en tout cas pas encore), 
il analyse les noms (et non leur contenu) des fichiers et repèr les doublons
avérées ou potentiels.
"""


INTRO_DESCRIPTIF ="""

Pour l'instant, il les deplace fichier source et ses doublons dans
 un dossier spécifique mais demain vous pourez deplacer uniquement les 
 doublons, les supprimer automatiquement, avoir plusieurs niveaux de 
 doublons (doublons sur à 75%, doublons sur à 90%) etc etc
 bref une palette d'option s'ouvre à l'evolution de ce programme. 

 On rajoute qu'il s'agit d'un script brut (et pas tres beau en affichage) et  
 qu'une GUI serait la bien venue.

 Enfin, coté Algorithme, on est  ecore sur du basique. les v1.1 et superieures
 proposerons des ameliorations significatives de se coté: 

 Aujourd'hui : 
 On regarde les la moitié des premiers caracteres, s'ils sont les meme, on regarde s'il y a des (1), (2), 
 ou si 75 à 80 pour 100 de la chaine est la meme. 

 C'est pas mal mais on peut mieux ! 


 Quid des documents "CV Alexandre GAZAGNES" et "CV Alxandre GAZAGNES" ? 
 Une petite coquille qui doit etre repérée par notre algo. ca n'est pas le cas mais  c'est un
 bel axe d'amelioration. 

Et mieux !

Quid du CV de Jean DUPONT ? Il y en a 12 mais ca ne sont pas des doublons en tant que tel
On peut regarder du coté de taille du fichier. Si c'est la meme
c'est un indice criant sinon... comment savoir que ce sont deux personnes différentes?

etc etc 

"""


INTRO_FONCTIONNALITES = """
- demander si afficher l'intro
- demander options
- demander le fichier de référence
- demander si on garde les noms de fichiers ou si on les changes
- sortir une liste avec tout le noms de fichiers du dossier selectionné
- voir si il y a deja un dossier doublons
- demander si on garde le nom du dossier doublon ou si on le MAJ
- dire qu'on rentre dans la boucle principale
- afficher la liste et le nombre de fichiers à traiter
- afficher l'avancement du process
- pour chaque fichier dans le dossier, il compare la chaine de caracteres du nom du fichier à l'ensemble des noms des fichiers
- pour  cela : 
	- créer 2 objets spécifiques "Fichier" qui ont des attributs, 'nom', 'doublon' etc etc
	- vérifier d'abord que c'est une extension .pdf ou .doc etc etc
	- verifier que les premieres lettres sont les memes, sinon inutile de continuer 
	- s'assurer que le fichier ne se comparer pas lui meme, et que le fichier n'a pas déja été trouvé, copié et supprimé dans le parours...
	- s'il y a "(1)", "copie", "_(1)" dans le nom du fichier c'est tres probablement une copie, pas bespoin de faire bcp d'effort, on evalue que la moitié du fichier
	- si ce n'est pas le cas alors il faut parcourir au moins 80/100 de la chaine de caractere du nom du  fichier
	- si on estime que les chaine sont suffisement proche alors on a un doublon (on en a meme 2)
	- spécifier qu nos deux objets sont des doublons
	- si pas de dossier de doublon on le crée
	- on copie nos deux fichiers dans le dossier doublon
	- on les supprime du repertoire réel, puis de la liste des fichiers

"""

INTRO_AMELIORATION ="""
Amelioration pour la v1.0.2
- s'assurer de l'ensemble des tabulations dans les boucles "j"
- supprimer les property useless (toutes)
faire des teste avec copie, copy etc etc
faire des test sur des configs CV alexandre GAZAGNES et CV Alexandre GAZAGNES 2017
- QUID des "-1" à la fin
- QUID des copie de copie etc
- Options : 
	1 crtlx ou crtlc + crtlv
	2 traitempent automatique 
	3 garder ou non le fichier source
	idem pour les doublons....
- comme évoqué qui de "cv alexandre gazagnes" et "cv alxandre gazagnes"
	on a pas tout mais on voit que sur les 24 char, on en a un enchainement de 18 similaires
- imaginons qu'on ai "cv alexandre gazagnes" et profil de "mr gazagnes alexandre"
- comment prendre en compte la taille su fichier? -- > os.path.getsize(path) renvoie la taille du fichier path
- quid d'une bonne GUI
- le script se gere til idem sur tous les OS?
		faire des tests sur 10, 150, 500, 1000 fichiers
- proposer un compteur de temps et de vitesse de proc'
- si il y a deux modes d'algo, il faut laisse le choix à user, l'un 
ou l'autre ou les deux
- combien de fichier doublons? de 1 à 3, 90/100, 80/100, 70/100
- evaluer la pertinence des verbose"""




###############################################################################
# 		IMPORT
###############################################################################


import sys
import os, stat
import shutil




###############################################################################
# 		CONSTANTES / VARIABLES
###############################################################################


# Constantes
##################################




LISTE_EXTENSIONS_TEXTE = [".pdf", ".doc", ".docx", ".odt", ".txt", "" ] # DICO_EXTENSIONS = {'.doc': 4, '.docx': 5, '.pdf': 4, ".odt":4, "":0}
LISTE_EXTENSIONS_GLOBALE = ["Créer une liste avec L'ENSEMBLE des extensions existantes"]


"""LISTE_PARENTHESES = ['(0)', '(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(7)', '(8)', '(9)', '(10)', '(11)', '(12)', '(13)', '(14)', '(15)', '(16)', '(17)', '(18)', '(19)', '(20)', '(21)', '(22)', '(23)', '(24)', '(25)', '(26)', '(27)', '(28)', '(29)']"""
NB_LISTE_PARENTHESE_MAX= 15
CHAR_PARENTHESE = ["", " ", "_"]
LISTE_PARENTHESES = list()
LISTE_PARENTHESES + ["copie", "copy"]
for k in CHAR_PARENTHESE:
	LISTE_PARENTHESES += ["{}({})".format(k, str(i)) for i in range(0, NB_LISTE_PARENTHESE_MAX)]


FICHIER_SUPPRIME = "fichier supprimé"


LISTE_VALEURS_CHOIX_OUI = ["oui", "Oui", "Oui", "o", "O", "<Entree>", ""]


# Variables
##################################

dossier_parent = os.getcwd() # ou utiliser dossier_parent = "/home/alex/Avenir/Agea_Conseil/BDD/CVs/script_dedoublonnage"

liste_fichiers = list()
dict_fichiers = dict()

dossier_doublon_existe = False 
dossier_doublon_sans_slash = "Dossier_doublons"
dossier_doublon_avec_slash = "/" + dossier_doublon_sans_slash

fichier_1, fichier_2 = "objet", "objet"

# CI DESSOUS PASSENT DE CONSTNATE à VARIABLE !!!
TAUX_MATCH_ANALYSE_AVEC_PARENTHESES = 0.5
TAUX_MATCH_ANALYSE_SANS_PARENTHESES = 0.8
TAUX_MATCH_PRE_ANALYSE = 0.5

LISTE_EXTENSIONS_TEXTE = [".pdf", ".doc", ".docx", ".odt", ".txt", "" ] # DICO_EXTENSIONS = {'.doc': 4, '.docx': 5, '.pdf': 4, ".odt":4, "":0}


# Options
##################################

"""
deplacer_fichier_doublon_et_original = "déplacer le fichier orignial et ses doublons dans le fichier {}? (ou que déplacer les doublons)\nPar défault : Oui\n".format(dossier_doublon_sans_slash)
suppr_fichier_original_dans_rep_source = "supprimer le fichier original dans le repetoire source ? (ou le laisser dedans) \nPar défault : Oui\n"
suppr_auto_doublons = "supprimer de facon automatique les doublons ? (ou les laisser dedans)\nPar défault : Non\n"
un_seul_dossier_doublon = "créer un seul dossier {} ? (ou en créer deux)\nPar défault : Oui\n".format(dossier_doublon_sans_slash)

dict_options = {deplacer_fichier_doublon_et_original: True
suppr_fichier_original_dans_rep_source: True,
suppr_auto_doublons : False,
un_seul_dossier_doublon : True }
"""
option_verbose = True





###############################################################################
# 		CLASSES
###############################################################################


# Creation de la classe Fichier
##################################

class Fichier : 
	"""description de classe
	input: -
	output: -"""

	def __init__(self, nom, chemin):
		# attributs d'instances, inchangeable
		self._nom = str(nom)
		self._nom_sans_casse = self._nom.lower()
		self._chemin = str(chemin)
		
		# attributs par défaults, voués à etre modifiés
		# pas besoin de le creer mais c'est juste "pédagocique"
		self._doublon = False
		self._parenthese = False
		self._supprime_dans_liste = False
		self._nom_sans_extension = ""
		self._extension = ""



# Accesseurs, mutateurs, Property
##################################


	# pour bien gere notre fichier et eviter les erreurs on va les passer 
	# en privés ndlr, on va utliser propoerty (assceuers et mutateurs)
	# en fait ils ne sont PAS DU TOUT UTILES, cest juste pour  s'entrainner :) 


	# on ne peut pas modfier le nom
	def _get_nom(self): return self._nom
	def _set_nom(self, nouveau_nom): input("ERREUR, nom fichier non modifiable\n")
	nom = property(_get_nom, _set_nom)


	# On peut modifier le chemin si ce dernier est valide
	def _get_chemin(self): 
		return self._chemin
	def _set_chemin(self, nouveau_chemin): 
		try : 
			os.chdir(nouveau_chemin)
			os.chdir(dossier_parent)
			self._chemin = nouveau_chemin
		except:
			input("Erreur, chemin inconnu\n")
	chemin = property(_get_chemin, _set_chemin)


	# On peut modifier l'attribut doublon si ce dernier est un booléen
	def _get_doublon(self): 
		return self._doublon
	def _set_doublon(self, nouveau_doublon):
		# on s'assure que c'est bien un booléen
		if isinstance(nouveau_doublon, bool) : 
			self._doublon = nouveau_doublon
		else:
			input("ERREUR l'attribut {} n'est pas un booléen\n".format(nouveau_doublon))
	doublon = property(_get_doublon, _set_doublon)


	# On peut modifier l'attribut parenthese si ce dernier est un booléen
	def _get_parenthese(self): 
		return self._parenthese
	def _set_parenthese(self, nouveau_parenthese):
		# on s'assure que c'est bien un booléen
		if isinstance(nouveau_parenthese, bool): 
			self._parenthese = nouveau_parenthese
		else:
			input("ERREUR l'attribut {} n'est pas un booléen".format(nouveau_parenthese))
	parenthese = property(_get_parenthese, _set_parenthese)


	# On peut modifier l'attribut "dans la liste" si ce dernier est un booléen
	def _get_supprime_dans_liste(self): 
		return self._supprime_dans_liste
	def _set_supprime_dans_liste(self, nouveau_supprime_dans_liste):
		# on s'assure que c'est bien un booléen
		if isinstance(nouveau_supprime_dans_liste, bool): 
			self._supprime_dans_liste = nouveau_supprime_dans_liste
		else:
			input("ERREUR l'attribut {} n'est pas un booléen".format(nouveau_supprime_dans_liste))
	supprime_dans_liste = property(_get_supprime_dans_liste, _set_supprime_dans_liste)


# Methodes de Fichier
##################################


	# voici desormais 5 methodes TRES IMPORTANTES
	# pour info jai choisi de travailler sur les _attributs et non sur les attributs
	# pourquoi? car il s'agit de methodes appelées dans la classes
	# elle sont docn "sures"...


	def maj_avec_et_sans_extension(self):
		""" metdode de Fichier qui ajoute 2 attributs 
		input: juste l'objet avec notamment son attribut nom
		output: Rien mais creation de deux new attributs: 
			objet.extension
			objet.nom_sans_extension"""
		
		liste_extensions = list(LISTE_EXTENSIONS_TEXTE)
		"""liste_extensions.remove("")"""
		
		for i in liste_extensions: 
			
			if i in self.nom : # si une extension connue est deja dans le nom du fichier
				ext = str(i)
				nom_sans_ext = self.nom[:len(self.nom) - len(ext)]
				break

			elif (  # sinon, on regarde si ca finit en .py ou .mp3 ou .ogg etc etc
				(self.nom[-1].isalnum()) \
				and (self.nom[-2].isalnum() or self.nom[-2] == ".") \
				and (self.nom[-3].isalnum() or self.nom[-3] == ".") \
				and (self.nom[-4].isalnum() or self.nom[-4] == ".") \
				and (self.nom[-5].isalnum() or self.nom[-5] == ".") \
				) : 
				# sous sujet, si c'est un doc de type 13445.134445.132 aie
				if self.nom[-2].isnumeric() and self.nom[-1].isnumeric():
					nom_sans_ext = self.nom
					ext = "" # on exclus donc les exetensions en 3 chiffres
				else : 
					# sinon on traite l'extension
					nb = str(self.nom).find(".", len(self.nom)-5)
					nom_sans_ext = self.nom[:nb]
					ext = self.nom[nb:]
			# si pas de points, pas dextension!
			elif "." not in self.nom: 
				nom_sans_ext = self.nom
				ext = ""
			# sinon pas d'extension non plus! 
			else : 
				nom_sans_ext = self.nom
				ext = ""

		self.extension = self._extension = str(ext.lower())
		self._nom_sans_extension = self.nom_sans_extension = str(nom_sans_ext.lower())


	def maj_parenthese(self):
		""" metdode de Fichier qui ajoute 1 attributs 
		il detecte s'il y a des '(1)' ou '(2)' ou ' (1)' ou '_(1) dans le nom
		input: juste l'objet avec notamment son attribut nom
		output: Rien mais creation d'un attribut: objet._parenthese """

		if ("copie" or "copy") in self._nom: 
			self._parenthese = True

		else : 
			if ("(" in self._nom) and (")" in self._nom) :
				for element in LISTE_PARENTHESES :
					if (element) in self._nom : 
						self._parenthese = True
						break


	def maj_fichier(self):
		"""methode qui appelle deux autres methodes (pas tres utile, certes) 
		input: juste l'objet
		output: rien mais creation/maj objet.extension, objet.nom et objet.parenthese"""

		self.maj_avec_et_sans_extension()
		self.maj_parenthese()


	def copier_fichier_dans_dossier(self, dossier=str(dossier_parent + dossier_doublon_avec_slash)):
		"""methode de Fichier qui copie_colle le fichier dans un dossier
		input: objet, et le dossier dans lequel on va le copier
		output: rien, juste deux prints de controles, (à verboser à terme?) """

		try : 
			shutil.copy2(self._nom, str(dossier + "/" + self._nom))
			print("copie OK : i = {}, j = {}, fichier = {}".format(i,j,self._nom))
		except:
			input("probleme CRTLC/V : i = {}, j = {} fichier = {}".format(i,j,self._nom))


	def supprimer_fichier_dans_dossier(self,dossier=str(dossier_parent)): 
		"""methode de Fichier qui supprime le fichier dans un dossier
		input: objet, et le dossier dans lequel on va le copier
		output: rien, juste deux prints de controles, (à verboser à terme?) """
		
		try :
			os.remove(dossier+"/"+self._nom)
			print("suppression OK: i = {}, j = {} fichier = {}\n".format(i,j,self._nom))
		except:
			input("probleme suppression: i = {}, j = {} fichier = {}\n".format(i,j,self._nom))





###############################################################################
# 		FONCTIONS
###############################################################################


# Fonctions d'input et d'intro
##################################

def demander_print_intro(texte = INTRO_TITRE): 
	"""fonction qui demande si user veut afficher l'inro
	input: le texte d'intro
	output: rien, juste un print du texte d'intro"""

	rep = input("Afficher intro? pour répondre oui, tappez {}\n".format(LISTE_VALEURS_CHOIX_OUI))
	if rep in LISTE_VALEURS_CHOIX_OUI:
		print(texte)
	else:
		print("Dommage...\n")
		
def demander_option_verbose(): 
	"""
	"""
	
	rep = input("Voulez vous utiliser le mode 'verbose' qui propose d'afficher toute les etapes du process?\nPour Oui, tappez {}\n"\
		    .format(LISTE_VALEURS_CHOIX_OUI))
	if rep :
		return True
	else :
		return False
	
def demander_taux_match(pre_ana = TAUX_MATCH_PRE_ANALYSE, avec_para = TAUX_MATCH_ANALYSE_AVEC_PARENTHESES, sans_para = TAUX_MATCH_ANALYSE_SANS_PARENTHESES): 
	"""
	"""
	
	rep = input("""Voulez vous utiliser les valeurs par défault des valeurs de taux de match?
	pré-analyse = {}, avec parentheses = {} et sans parentheses = {}
	Pour Oui, tappez {}\n"""\
		    .format(LISTE_VALEURS_CHOIX_OUI, pre_ana, avec_para, sans_para))
	if rep :
		return pre_ana, avec_para, sans_para
	else :
		return False, False, False
	

def demader_liste_extensions(liste_ext = LISTE_EXTENSIONS_TEXTE):
	"""
	"""
	
	rep = input("""Voulez vous utiliser les extensions validées par défault ?
	{}
	Pour Oui, tappez {}\n"""\
		    .format(LISTE_VALEURS_CHOIX_OUI, liste_ext))
	if rep :
		return liste_ext
	else :
		return 	
	
	
def demander_maj_dossier_parent(dossier=dossier_parent) :
	"""demander à user si on garde le dossier parent inital, ou tapper un répertoire/dossier de
	son choix, en validant qu'il existe bien...
	input: une chaie représentant un chemin vers le repertoire/dossier parent intialisé en général os.getcwd()
	output: le dossier selectionné par user, maj ou non, à recupérer dans dossier_parent en sortie de fct"""
	
	valid = False
	while not valid:
		rep = input("Nous sommes actuellement dans le dossier {}, cela vous convient-il?\npour répondre oui, tappez {}".format(dossier, LISTE_VALEURS_CHOIX_OUI))
		if rep in LISTE_VALEURS_CHOIX_OUI:
			print("OK, on reste dans {}".format(dossier))
			valid = True
			return dossier

		else:
			rep = input("OK, on change, entrez un chemin, sinon tappez {} pour utiliser {}".format(LISTE_VALEURS_CHOIX_OUI, dossier))
			try:
				os.chdir(rep)
				valid=True
				return rep
			except:
				if rep not in LISTE_VALEURS_CHOIX_OUI:
					print("Dossier {} n'est pas valable".format(rep))


def creer_liste_fichiers(dossier=dossier_parent): 
	"""creer automatiquement une liste contenant l'ensemble de chianes des noms de dossier, 
	par ordre alphanumérique
	fonction appelée en sortie de demander_renommer_fichiers()
	input: une chaine représentant un chemin vers le repertoire/dossier parent intialisé avec demander_maj_dossier_parent()
	output: la liste créée contenant l'ensemble de chianes des noms de dossierà recupérer en sortie de fonction"""

	try : 
		liste_fichiers = os.listdir(dossier)
		liste_fichiers.sort()
		print(liste_fichiers)
		print("Il y a {} fichiers dans le dossier\n".format(len(liste_fichiers)))
	except: 
		input("Problème dans la creation de la liste des fichiers\n")
		liste_fichiers = 0

	return liste_fichiers 


def demander_renommer_fichiers(dossier= dossier_parent, val_old = " ", val_new = "_"):
	"""demander si au sein des noms du fichier, on veut automatiquement modifier un char par un autre.
	typiquement, on peut remplacer ' ' par des '_'
	peu utile à Premiere vue MAIS peut servir quand meme :)

	ATTENTION il peut y avoir un pb sur le renomage des fichiers... Il faut utiliser os.chmod(), mais en mode root...
	bref à creuser  // ce probleme peut se retrouver en autorisation de  copier colle supprimer deplacer des fichiers...

	input: une chaine représentant un chemin vers le repertoire/dossier parent intialisé avec demander_maj_dossier_parent()
	la valeur à remplacer, la nouvelle valeur
	output: la liste créée contenant l'ensemble de chianes des noms de dossierà recupérer en sortie de fonction
	idem creer_liste_fichiers()"""

	reponse = input ("Voulez vous supprimer les {} et les remplacer par {}? \n tappez {} pour Oui \n".format(val_old, val_new, LISTE_VALEURS_CHOIX_OUI))
	if reponse in LISTE_VALEURS_CHOIX_OUI:
		for i in creer_liste_fichiers() :
			try : 
				"""os.chmod(str(i), stat.S_IRWXO)
				os.chmod(str(i), stat.S_IRWXG)
				os.chmod(str(i), stat.S_IRWXU) 
				AU BESOIN IL FAUDRA CHANGER LES AUTORISATIONS DU FICHIER..."""
				os.rename(i, i.replace(val_old, val_new))
			except : 
				input("Probleme dans le renommage du fichier {}, permission non accordée\n".format(i))
	else:
		print("OK, on ne rennome pas!\n")			

	return creer_liste_fichiers()


def demander_options():
	"""A mettre à jour dans une 2e version, il existe de nombreuses options : 
	deplacer ou copoier coller, ou couper coller etc etc
	creer un ou 2 ou 3 fichier doublon : "doublons 100%", "doublons 75%"
	supprimer automatiquement les doublons etc etc 
	changer le nom de dossier doublon etc etc
	
	input: - 
	output: - """

	option = input("Niveau de Traitemrnt de l'algortyme?\n")
	""" à implémenter plus tard"""
	return option


def voir_si_dossier_doublon_existe(dossier=dossier_parent):
	"""fonction qui regarde si le dossier doublon existe deja en essayant de ce mettre dans ce repertoire, si
	c'est possible de ce mettre dedans alors cela veut dire que le fichier existe
	pas besoin de le créer, on modifiera ainsi la valeur de doublon_existe en sortie
	input: une chaine représentant un chemin vers le repertoire/dossier parent intialisé avec demander_maj_dossier_parent()
	output: un bool : True si le dossier doublon existe deja, False sinon, à recupérer en sortie de fonction"""

	try: 
		os.chdir(str(dossier + dossier_doublon_avec_slash))
		os.chdir(dossier)
		print("il y a deja un dossier {}, pas besoin de le créer\n".format(dossier_doublon_sans_slash))
		return True
	except	:
		print("il n'y a pas de {}, il faudra le créer\n".format(dossier_doublon_sans_slash))
		return False


def demander_maj_dossier_doubon(doss_doubl =  dossier_doublon_sans_slash):
	"""demander à user si on garde le nom du dossier doublon original ou tapper un répertoire/dossier de
	son choix...
	input: une chaie représentant un chemin vers le repertoire/dossier parent intialisé en général os.getcwd()
	output: le dossier selectionné par user, maj ou non, à recupérer dans dossier_parent en sortie de fct"""

	valid = False
	while not valid:
		rep = input("Le Dossier de Doublon s'appelle actuellement '{}', cela vous convient-il?\npour répondre oui, tappez {}".format(doss_doubl, LISTE_VALEURS_CHOIX_OUI))
		if rep in LISTE_VALEURS_CHOIX_OUI:
			print("OK, on garde le nom '{}'".format(doss_doubl))
			valid = True
			return doss_doubl

		else:
			rep = input("OK, on change, entrez un chemin, sinon tappez {} pour utiliser {}".format(LISTE_VALEURS_CHOIX_OUI, dossier))
			if rep not in LISTE_VALEURS_CHOIX_OUI:
				valid=True
				return rep


# Fonctions d'Algorithme
##################################

def calculer_nb_char_min(fifty=True, fi1=fichier_1, fi2=fichier_2):
	"""calcule un nombre entier qui serviera de nombre butoir dans le slicing des chaines de caracteres de noms de fichiers  à comparer
	si c'est la pré- analyse, on ne regarde que le début, juste pour s'assurer que c'est pas des noms de fichiers RADICALEMENT
	différents l'un de l'autre, sinon l'analyse est plus corése.
	idem si il y a des parentheses dans les deux fichiers, pas besoin de trop pousser la recherche, en revanche sans parentheses, il va 
	falloir pousser un peu à 70, 80 voire 90%
	input: un booléen pour savoir si c'est la pré-analyse (que 50%), ou la vraie analyse (à 70, 80 ou 90%) et les 2 objets fichiers à comparer
	output: un entier qui servira de butoir dans l'analyse de char des noms des fichiers, à recupérer en sortie de fonction"""

	if fifty :
		return int((min(len(fi1.nom_sans_extension), len(fi2.nom_sans_extension)) * TAUX_MATCH_PRE_ANALYSE)-1)
	else:
		if ((fi1.parenthese) or (fi2.parenthese)) or (("copie" or "copy") in fi1.nom) or (("copie" or "copy") in fi2.nom): 
			return int((TAUX_MATCH_ANALYSE_AVEC_PARENTHESES * min(len(fi1.nom_sans_extension),len(fi2.nom_sans_extension)))-1)
		else : 
			return int((TAUX_MATCH_ANALYSE_SANS_PARENTHESES * min(len(fi1.nom_sans_extension),len(fi2.nom_sans_extension)))-1)


def creer_dossier_doublon_si_besoin(dossier=dossier_parent):
	"""fonction qui crée un dossier doublon sur la base de la constante DOSSIER_DOUBLON_AVEC_SLASH
	rien de tres compliqué à ce stade : ) peut etre envoyer les prints dans une fonction verbose
	input: une chaine correspondant au dossier_parent
	output: un booléen True si on a réussi à creer le dossier doublon, False sinon, à capturer en sortie de fonction"""

	try : 
		os.mkdir(str(dossier + dossier_doublon_avec_slash))
		print("Creation du fichier {}\n".format(dossier_doublon_sans_slash))
		return True
	except:
		input("Probleme creation du fichier {}\n".format(dossier_doublon_sans_slash))
		return False


def traiter_doublon(fi1=fichier_2, fi2=fichier_1, boucle="", val=0 , dossier=dossier_parent):
	"""fonction qui régit le coeur du programme, elle effectue les actions principales une fois qu'on 
	a identifié et validé les deux doublons. en fonction de la boouche elle s'effectue sur un objet différent
	dans l'ordre, elle copie le fichier, le supprime et MAJ l'attribut objet.supprime_dans la liste.
	enfin elle MAJ effectivement la liste qui est passée en global pour s'assurer de sa bonne MAJ

	il sera utile de la verboser, car on y trouve du texte et de l'action, pas clair...

	input: le fichier à traiter, le fichier de comparaison, la boucle dans laquelle on est 
	sa valeur et le dossier dans lequel on travaille
	output: Rien, quelques print() mais à  verboser"""

	global liste_fichiers

	if boucle == "j": char = "\t"
	else : char = ""
	
	print(char + "{} est un doublon avec le fichier {}\n".format(fi1.nom,fi2.nom))
	
	# On effectue le CRTLC+V + Suppr du fichier en question
	fi1.copier_fichier_dans_dossier()
	fi1.supprimer_fichier_dans_dossier()
	fi1.supprime_dans_liste = True
	
	# On MAJ la liste_fichier
	if boucle == "i" : 
		liste_fichiers[val] = FICHIER_SUPPRIME
	elif boucle == "j" : 
		liste_fichiers[val] = FICHIER_SUPPRIME
	else:
		input(char + "Erreur dans MAJ liste_fichiers\n")


# Fonctions de Verbose
##################################

def definir_char(val): 
	""" fonction qui définit le decalage du texte ou pas
	si on est dans une bouche "i", pas de decalage, sinon une "\t"
	input: une val, en général "i" ou "j"
	output : char = "" ou "\t" """

	if val == "j": char = "\t"
	else : char = ""
	return char


def verbose_avancement_algo(tour, nombre_fichiers_a_traiter, boucle):
	"""fonction qui print un avancement du programme. en fonction de si on est dans une boucle i ou j, il calcule et 
	donne une représentation de l'avancement de notre algorithme
	input: ne n* du tour  dans la boucle, le nombre de fichier à traiater (l'un sur l'autre donne le % d'ancement)
	et la boucle pour le decallage possible
	output: Rien on print juste l'avancement"""

	char = definir_char(boucle)

	avancement = int(((tour+1)/ nombre_fichiers_a_traiter)*20)
	print(char + "AVANCEMENT [{}{}] / fichier {} sur {}".format(avancement*"I", (20-avancement)*" ", tour+1,  nombre_fichiers_a_traiter))


def verbose_conditions_principales(succes, fichier, boucle, val):
	""" Explique les test principaux sur la présence du fichier dans la liste MAJ
	la validtité de son extension
	input :  succes : utilisation de la verbose si ca a marché ou pas (booléen)
	le fichier (class Fichier), le nom de la boucle dans laquelle on est "i" ou "j"
	et sa valeur
	output : Rien, c'est une routine elle est la pour print...
	"""

	char = definir_char(boucle)

	if succes:
		print(char + "on étudie le fichier {}, {} = {}, il a l'extension {} qui est valable, il n'a pas été deja traité, on entre dans la boucle"\
			.format(fichier.nom, boucle, val, fichier.extension))

	else : 
		if (fichier.nom == FICHIER_SUPPRIME):
			print(char +"On ne traite pas car le fichier {} a déja été traité".format(fichier.nom))
		if fichier.extension not in LISTE_EXTENSIONS_TEXTE:
			print(char +"On ne traite pas car le fichier {}  a une extension non conforme".format(fichier.nom))
		if fichier.extension != "":
			print(char +"On ne traite pas car le fichier {}  a une extension non conforme".format(fichier.nom))
		"""print(char + "En tout cas, on entre pas dans la boucle {}  et on ne traite pas le fichier {} \n" \
			.format(char , fichier.nom))"""


def verbose_extensions(succes, fichier, boucle, val):
	""" Explique les tests sur les extenion d'un fichier
	input :  succes : utilisation de la verbose si ca a marché ou pas (booléen)
	le fichier (class Fichier), le nom de la boucle dans laquelle on est "i" ou "j"
	et sa valeur
	output : Rien, c'est une routine elle est la pour print...
	"""

	char = definir_char(boucle)

	if succes :  
		print("pour {} = {} {} a une extension de type {}".format(boucle, val, fichier.nom, fichier.extension))

	else : 
		pass


def verbose_fichier_nb_char_idem(succes, fichier, fichier2, boucle, val, nb):
	""" Explique les nb_char premiers caracteres du nom des deux fichiers 
	comparés sont les memes
	input :  succes : utilisation de la verbose si ca a marché ou pas (booléen)
	les fichiers (class Fichier) à comaperer, le nom de la boucle dans laquelle on est "i" ou "j"
	sa valeur, et ne nb_char à considerer...
	output : Rien, c'est une routine elle est la pour print...
	"""

	char = definir_char(boucle)

	if succes:
		print(char + "Le fichier {} et le fichier {} idem à {} %".format(fichier.nom, fichier2.nom, int(100* nb/len(fichier.nom))))
	else : 
		print(char + "Le fichier {} et le fichier {} idem à {} %".format(fichier.nom, fichier2.nom, int(100* nb/len(fichier.nom))))


def verbose_valider_conditions_avant_traitement(succes, fichier, boucle, val):
	""" Explique les derniers tests avant action: si le fichier est bien un class Fichier,
	s'il a bien été considéré comme un doublon; si la boucle est bien valable
	et si le fichier n'a pas déja été traité ét supprimé dans la liste...
	input :  succes : utilisation de la verbose si ca a marché ou pas (booléen)
	le fichier (class Fichier) à étudier, le nom de la boucle dans laquelle on est "i" ou "j"
	sa valeur..
	output : Rien, c'est une routine elle est la pour print..."""

	char = definir_char(boucle)

	if succes:
		print(char + "conditions avant action réunies, on traite le {} dans la boucle {}: {} !"\
			.format(fichier.nom, boucle, val))
		
	else:
		if not isinstance(fichier, Fichier):
			print(char + "Probleme avec la variable {} qui n'est pas un Fichier")
		if not fichier.doublon :
			print(char + "Probleme avec la variable {} qui n'a pas dattribut doublon = True")
		if not boucle in ["i", "j"] :
			print(char + "Probleme avec la variable boucle {} qui n'a pas de valeur 'i' ou 'j' ")
		if  fichier.supprime_dans_liste:
			print(char + "{} a déja été traité car {}.supprime_dans_liste vaut {} ".format(fichier.nom, fichier.supprime_dans_liste))
		else : 
			print(char + "Probleme inconnu!!!")
		print(char + "conditions avant action non réunies, on continue sans traiter...")




###############################################################################
# 		MAIN
###############################################################################


# Inputs de base
##################################

demander_print_intro() # savoir si on print l'intro

option_verbose = demander_option_verbose()

TAUX_MATCH_PRE_ANALYSE, TAUX_MATCH_ANALYSE_AVEC_PARENTHESES, TAUX_MATCH_ANALYSE_SANS_PARENTHESES  = demander_taux_match()

LISTE_EXTENSIONS_TEXTE = demader_liste_extensions()

dossier_parent = demander_maj_dossier_parent() # savoir quel dossier parent on utilise

liste_fichiers = demander_renommer_fichiers() # creation de la liste des fichiers dedans

"""
# A IMPLEMMENTER PLUS TARD :)
options = demander_options()
"""

dossier_doublon_existe = voir_si_dossier_doublon_existe() # On regarde si il y a deja un dossier doublon

if dossier_doublon_existe : 
	dossier_doublon_sans_slash = demander_maj_dossier_doubon()
	dossier_doublon_avec_slash = "/"+ dossier_doublon_sans_slash


# Algorithme principal
##################################

if liste_fichiers: 

	if option_verbose: print("On lance l'algoritme, on lance la boucle 1er\n")

	# on va travailler sur les fichiers eux meme, on manipule donc
	# un index et pas le fichier lui meme ;), d'ou range(len(liste)) 
	for i in range(len(liste_fichiers)):

		# on instancie notre objet Fichier qui a pour attributs .nom, .extension etc etc
		fichier_1 = Fichier(liste_fichiers[i], dossier_parent)
		fichier_1.maj_fichier() # On maj parenthese, nom_sans_extension et extension

		verbose_avancement_algo(i, len(liste_fichiers), "i") # On affiche l'avancement

		# on ne traite que les fichiers dont l'enstension nous interesse
		if (fichier_1.nom != FICHIER_SUPPRIME) and ((fichier_1.extension in LISTE_EXTENSIONS_TEXTE) or (fichier_1.extension == "")) :
		
			if option_verbose : verbose_conditions_principales(True, fichier_1, "i",i)

			# on compare notre fichier_1 à l'ensemble des autres  fichiers
			for j in range(i, len(liste_fichiers)):
							
				fichier_2 = Fichier(liste_fichiers[j], dossier_parent) #idem boucle 1	
				fichier_2.maj_fichier()

				"""verbose_avancement_algo(j, int(len(liste_fichiers)-i), "j")"""

				if ((fichier_2.extension in LISTE_EXTENSIONS_TEXTE) or (fichier_2.extension == "")) and (j>i) and (fichier_2.nom != FICHIER_SUPPRIME) : #idem boucle 1	

					if option_verbose : verbose_conditions_principales(True, fichier_2, "j",j)

					# si les noms commencent pareil ndlr, inutile de comaper "CV Alex" et "1234" 
					nb_char_min = calculer_nb_char_min(True, fichier_1, fichier_2) 
					if (fichier_1.nom[0:nb_char_min] == fichier_2.nom[0:nb_char_min]) : 

						if option_verbose : verbose_fichier_nb_char_idem(True, fichier_2, fichier_1, "j",j,nb_char_min)

						nb_char_min = calculer_nb_char_min(False, fichier_1, fichier_2)
						if fichier_1.nom[:nb_char_min] == fichier_2.nom[:nb_char_min]:
								
							if option_verbose: verbose_fichier_nb_char_idem(True, fichier_2,fichier_1, "j",j,nb_char_min)

							fichier_1.doublon, fichier_2.doublon = True, True

							# si on a pas détecté de fichier doublon, on le crée...
							if not dossier_doublon_existe : dossier_doublon_existe = creer_dossier_doublon_si_besoin(dossier_parent)

							# on valide une derniere série de conditions, si True on "agit" 
							if (fichier_2.supprime_dans_liste == False) and isinstance(fichier_2, Fichier) and fichier_2.doublon  : 

								if option_verbose : verbose_valider_conditions_avant_traitement(True, fichier_2, "j", j)
								traiter_doublon(fichier_2, fichier_1, "j", j)
							else : 
								if option_verbose : verbose_valider_conditions_avant_traitement(False, fichier_2, "j", j)	
						else : 
							if option_verbose : verbose_fichier_nb_char_idem(False, fichier_2, fichier_1, "j",j,nb_char_min)
					else : 
						if option_verbose: verbose_fichier_nb_char_idem(False, fichier_2,fichier_1, "j",j,nb_char_min)
				else :
					if j == i : pass
					else : 
						if option_verbose : verbose_conditions_principales(False, fichier_2, "j", j)

			if (fichier_1.supprime_dans_liste == False) and isinstance(fichier_1, Fichier) and fichier_1.doublon  : 

				if option_verbose : verbose_valider_conditions_avant_traitement(True, fichier_1, "i", i)
				traiter_doublon(fichier_1, fichier_2, "i", i)			
			else : 
				if option_verbose : verbose_valider_conditions_avant_traitement(False, fichier_1, "i", i)
			print("Liste de fichier MAJ =" + str( liste_fichiers))
		else : 
			if option_verbose : verbose_conditions_principales(False, fichier_1, "i",i)
else : 
	input("Désolé fail du script avant la 1ere boucle! \n") # A verboser?
