import sqlite3
from pathlib import Path
from sqlite3 import Error


def create_connection(file: str):
    """Permet de créer une Base de Données du nom de 'file' dans le dossier de travail et un accès à celle-ci."""
    path = str(Path.cwd()) + file
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful ")
    except Error as e:
        print(f"The error '{e}' happened")

    return connection


connexion = create_connection("Database.sqlite")


# Sert d'argument 'connection' dans les fonctions 'execute_(nom)_query'.


def execute_modify_query(query, connection = connexion):
    """Les modify query sont les 'CREATE TABLE' et 'CREATE VALUES'. Permet d'exécuter ce type de requêtes."""
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print(f"Query '{query}' executed successfully")
    except Error as e:
        print(f"The error '{e}' occured")


def execute_read_query(query, connection = connexion):
    """Les read query sont les 'SELECT' et les 'UPDATE'. Permet d'exécuter ce type de requêtes."""
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def create_table(nom: str, attributs, types, key = "") -> str:
    """ Le str nom est le nom de la table à créer. La liste 'attributs' est la liste des noms des colonnes de la
    table. La liste 'types' est la liste des types de chacun des attributs de la table (INTEGER, NULL, etc.).
    Le str facultatif 'key' doit être la requête des opérations suivant la création d'une table.
    Il peut contenir des 'FOREIGN KEY' par exemple."""

    query = "CREATE TABLE IF NOT EXISTS "
    query += nom
    query += " ( \n \t"

    for i in range(len(attributs)):
        query += attributs[i]
        query += " "
        query += types[i]
        if i != len(attributs) - 1:
            query += ", \n \t"

    query += key
    query += ");"
    return query


def create_values(table, attributs, enregistrements):
    """ Le str table est le nom de la table à remplir. La liste 'attributs' est la liste des noms des colonnes de la
    table. La liste 'enregistrements' est la liste des listes des valeurs des attributs d'un enregistrement (Ligne
    puis colonne)."""

    query = "INSERT INTO"
    query += "\n"
    query += table
    query += " ("

    for i in range(len(attributs)):
        query += attributs[i]
        if i != len(attributs) - 1:
            query += ", "

    query += ") \n VALUES \n"

    for i in range(len(enregistrements)):
        query += "\t ("

        for j in range(len(enregistrements[i])):
            query += enregistrements[i][j]
            if j != len(attributs) - 1:
                query += ", "

        if i != len(enregistrements) - 1:
            query += "), \n "
        else:
            query += ");"

    return query


def create_select_query(attributs, tables, conditions = [], operations = []):
    """La liste de str 'attributs' doit contenir les arguments suivant le 'SELECT'.
    De même pour la liste de str 'tables' et le 'FROM'.
    La liste de str facultative 'conditions' doit inclure les préfixes commençant une ligne tels que 'OR'
    ou 'AND'.
    La liste de str facultative 'operations' doit contenir les commandes à ajouter après le trio 'SELECT', 'FROM',
    'WITH' incluant les préfixes. Elle peut donc contenir des 'ORDER BY', 'LIMIT', 'OFFSET', 'FETCH' ou 'FOR' par
    exemple. Elle peut être générée par create_operations_query. """
    # En cas de doute sur les arguments se référer à
    # https://www.i3s.unice.fr/~rueher/Cours/BD/DocPostgresSQL9-5_HTML/sql-select.html

    query = "SELECT \n"

    for i in range(len(attributs)):
        query += attributs[i]
        if i != len(attributs) - 1:
            query += ", \n \t"

    query += "\n FROM \n \t"

    for i in range(len(tables)):
        query += tables[i]
        if i != len(tables) - 1:
            query += ", \n \t"

    if conditions:
        query += "\n WHERE "
        for i in range(len(conditions)):
            query += conditions[i]
            if i != len(conditions) - 1:
                query += ", \n \t"

    if operations:
        query += "\n"
        query += operations  # On suppose que le str operations est déjà mis en forme.

    return query


def create_update_query(table, attributs, valeurs, conditions = []):
    """Le str 'table' doit contenir le nom de la table à modifier.
    La liste de str 'attributs' doit contenir les arguments suivant le 'SET'.
    La liste 'valeurs' doit être de la même longueur que 'attributs' et contient les valeurs à remplacer.
    La liste de str facultative 'conditions' contient les arguments avec préfixes suivant le 'WHERE'."""
    query = "UPDATE \n \t"
    query += table
    query += "\n SET \n \t"

    for i in range(len(attributs)):
        query += attributs[i] + " = " + valeurs[i]
        if i != len(attributs) - 1:
            query += ", \n \t"

    if conditions:
        query += "\n WHERE "
        for i in range(len(conditions)):
            query += conditions[i]
            if i != len(conditions) - 1:
                query += ", \n \t"

    return query


def create_operations_query(types, arguments):
    """La liste de str 'types' contient les appels des opérations à effectuer.
    La liste de listes de str 'arguments' contient les arguments des appels contenus dans 'types'.
    On doit avoir len(types) = len(arguments). """

    operations = ""
    for i in range(len(types)):
        operations += types[i]
        operations += "\n \t"
        for j in range(len(arguments[i])):
            operations += arguments[i][j]
            if i != len(arguments) - 1:
                operations += ", \n \t"
        operations += "\n"

    return operations
