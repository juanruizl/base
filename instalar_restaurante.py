import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Restaurante (id_restaurante PRIMARY KEY, nombre, cp, FOREIGN KEY (cp) REFERENCES CodigoPostal(cp))")

cursor.execute("INSERT INTO Restaurante VALUES (1, 'Pizzería Napoli', '28004')")
cursor.execute("INSERT INTO Restaurante VALUES (2, 'Sushi Madrid', '28001')")
cursor.execute("INSERT INTO Restaurante VALUES (3, 'Burger House', '28012')")
cursor.execute("INSERT INTO Restaurante VALUES (4, 'Taquería El Güero', '28045')")

connexion.commit()
connexion.close()
