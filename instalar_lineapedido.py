import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS LineaPedido (id_pedido, id_plato, cantidad, PRIMARY KEY (id_pedido, id_plato), FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido), FOREIGN KEY (id_plato) REFERENCES Plato(id_plato))")

cursor.execute("INSERT INTO LineaPedido VALUES (1, 3, 2)")
cursor.execute("INSERT INTO LineaPedido VALUES (1, 4, 1)")
cursor.execute("INSERT INTO LineaPedido VALUES (2, 1, 1)")
cursor.execute("INSERT INTO LineaPedido VALUES (2, 2, 1)")
cursor.execute("INSERT INTO LineaPedido VALUES (3, 5, 2)")
cursor.execute("INSERT INTO LineaPedido VALUES (3, 6, 1)")
cursor.execute("INSERT INTO LineaPedido VALUES (4, 7, 3)")
cursor.execute("INSERT INTO LineaPedido VALUES (5, 8, 2)")

connexion.commit()
connexion.close()
