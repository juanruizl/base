import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Rider (id_rider PRIMARY KEY, nombre)")

cursor.execute("INSERT INTO Rider VALUES (1, 'Pablo Sánchez')")
cursor.execute("INSERT INTO Rider VALUES (2, 'Elena Torres')")
cursor.execute("INSERT INTO Rider VALUES (3, 'Diego Navarro')")

connexion.commit()
connexion.close()
