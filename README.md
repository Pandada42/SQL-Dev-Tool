# SQL-Dev-Tool
Outil pour créer, modifier et lire des databases SQL en python à l'aide de la librairie SQLite 3.

# Ce programme a été créé par Matthieu Boyer.


# Ce programme "automatise" partiellement la création de l'une des requêtes/query SQL et permet leur exécution via
# Python et le module SQLite 3. Pour cela, il créé une base de données à partir de la commande ligne 28. L'argument
# est le nom du fichier souhaité.

# Dans toute la suite, sauf précisé dans la signature ou l'aide de la fonction, les arguments sont des listes de str.
# Ce programme est voué à être modifié pour faciliter son utilisation. Si une valeur est assignée à un argument lors
# de l'appel d'une fonction, celui-ci est facultatif (l'aide de la fonction l'indique). Pour ajouter une valeur à
# l'argument facultatif x, appelez la fonction avec f(a, b, c, x = valeur).

# Pour utiliser ce programme, déposez le dans votre dossier de travail et importez le avec la commande : "import SQL"
# Il suffira alors d'appeler ses fonctions avec le préfixe "SQL.".

# Les fonctions "execute_(nom)_query" permettent d'exécuter des requêtes. Les fonctions "create_(nom)_query"
# permettent de les assembler à partir de listes python. Référez vous aux aides/commentaires dans la fonction pour
# plus d'informations.

# Prévenez moi si vous trouvez un bug. Ce programme a pour but de tester des requêtes.
# Il ne sert en aucun cas de preuve.

# Tendresse, Chocolat, J'vous aime putain.
