
###############################################################################
###############################################################################
#       MODULE TEXTES
###############################################################################
###############################################################################




###############################################################################
#       VARIABLES
###############################################################################




INTRO_TITRE = """
###############################################################
###############################################################
Script de dédoublonnage de fichiers dans un dossier spécifique
###############################################################
###############################################################


v1.0.2
21/04/2017
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
faire des teste avec copie, copy etc etc
faire des test sur des configs CV alexandre GAZAGNES et CV Alexandre GAZAGNES 2017
- QUID des "-1" à la fin
- Utliser les REGEX !!!! 
- utiliser getsize
- Opltoin que dans le dossier ou dans l'ensemble des sous dossiers..
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
- evaluer la pertinence des verbose

--- ALLO !!!! s'il y a un choix à faire entre deux fichier, il faudra forcément suppriler le plus ancien!!!!"""


INTRO_TEST = """

"cv alexandre gazagnes (3)" et "cv alexandre gazagnes -1" et "cv alexandre gazagnes" et "cv alexandre gazagnes (copie de copie)" # classique

"cv alexandre gazagnes" et "cv Alexandre GAZAGNES" # casse

"cv alxandre gazagnes" et "cv alexandre gazagnes" # une coquille

"cv alexandre gazagnes oct 2017 v2.3" et "cv alexandre gazagnes" # différentiel tres long

"cv gazagnes alexandre" et "cv alexandre gazagnes" # memes mots ordre différent

"cv.alexandre.gazagnes" et "cvalexandregazagnes" et "cv gazagnes alexandre" # wtf

"cvalexandregazagnes" et "cv20.11.2017demrgazagnesalexandre" et "cv gazagnes alexandre" # wtf

"""





###############################################################################
#       MAIN
###############################################################################



if __name__ == "__main__" : 
	print(INTRO_TITRE)
	input()

	print(INTRO_DESCRIPTIF)
	input()

	print(INTRO_FONCTIONNALITES)
	input()

	print(INTRO_AMELIORATION)
	input()

	print(INTRO_TEST)
	input()
