import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Plato (id_plato PRIMARY KEY, nombre, categoria, precio, id_restaurante, FOREIGN KEY (id_restaurante) REFERENCES Restaurante(id_restaurante))")

cursor.execute("INSERT INTO Plato VALUES (1, 'Pizza Margarita', 'Pizza', 9.5, 1)")
cursor.execute("INSERT INTO Plato VALUES (2, 'Pizza Cuatro Quesos', 'Pizza', 11.0, 1)")
cursor.execute("INSERT INTO Plato VALUES (3, 'Nigiri Salmón', 'Sushi', 6.5, 2)")
cursor.execute("INSERT INTO Plato VALUES (4, 'Maki Atún', 'Sushi', 7.8, 2)")
cursor.execute("INSERT INTO Plato VALUES (5, 'Hamburguesa Clásica', 'Hamburguesa', 8.9, 3)")
cursor.execute("INSERT INTO Plato VALUES (6, 'Hamburguesa BBQ', 'Hamburguesa', 10.5, 3)")
cursor.execute("INSERT INTO Plato VALUES (7, 'Tacos al Pastor', 'Mexicana', 8.0, 4)")
cursor.execute("INSERT INTO Plato VALUES (8, 'Burrito de Pollo', 'Mexicana', 7.5, 4)")

connexion.commit()
connexion.close()
