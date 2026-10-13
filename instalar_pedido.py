import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Pedido (id_pedido PRIMARY KEY, fecha, id_usuario, id_rider, FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario), FOREIGN KEY (id_rider) REFERENCES Rider(id_rider))")

cursor.execute("INSERT INTO Pedido VALUES (1, '2026-10-10 13:45', 1, 1)")
cursor.execute("INSERT INTO Pedido VALUES (2, '2026-10-10 20:30', 2, 2)")
cursor.execute("INSERT INTO Pedido VALUES (3, '2026-10-11 14:10', 3, 3)")
cursor.execute("INSERT INTO Pedido VALUES (4, '2026-10-12 21:05', 5, 1)")
cursor.execute("INSERT INTO Pedido VALUES (5, '2026-10-13 13:20', 4, 2)")

connexion.commit()
connexion.close()
