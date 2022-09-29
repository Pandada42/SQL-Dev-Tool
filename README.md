# SQL-Dev-Tool
Outil pour créer, modifier et lire des databases SQL en python à l'aide de la librairie SQLite 3.

Ce programme a été créé par Matthieu Boyer | MP* au Lycée La Martinière Monplaisir.

Pour assurer son fonctionnement, veillez à avoir toutes les librairies intégrées à Python installées, en particulier pathlib et sqlite3. 

Ce programme permet l'automatisation partielle de la création de requêtes/query SQL et permet leur exécution via Python et le module SQLite 3. Pour cela, il créé une base de données. 

Dans toute le programme, sauf précisé dans la signature ou l'aide de la fonction, les arguments sont des listes de string.
Ce programme est voué à être modifié pour faciliter son utilisation. Si une valeur est assignée à un argument lors de l'appel d'une fonction, celui-ci est facultatif (l'aide de la fonction l'indique). Pour ajouter une valeur à l'argument facultatif x, appelez la fonction avec f(a, b, c, x = valeur).
Pour utiliser ce programme, déposez le dans votre dossier de travail et importez le avec la commande : "import SQL"
Il suffira alors d'appeler ses fonctions avec le préfixe "SQL.".

Les fonctions "execute_(nom)_ query" permettent d'exécuter des requêtes. Les fonctions "create_(nom)_ query" permettent de les assembler à partir de listes python. Référez vous aux aides/commentaires dans la fonction pour plus d'informations.

Prévenez moi si vous trouvez un bug en postant une Issue sur ce repo ou en m'envoyant directement un message.
Ce programme a pour but de tester des requêtes. Il ne sert en aucun cas de preuve.





PS : En cas de bug, vous pouvez court-circuiter les fonctions "create_(nom)_ query" en entrant dans l'argument 'query' des fonctions "execute_(nom)_ query" un string contenant votre requête. Tout ce que les fonctions "create_(nom)_ query" font est en effet de synthétiser à partir de listes une requête SQL. 
