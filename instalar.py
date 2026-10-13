import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CodigoPostal (cp PRIMARY KEY, barrio, distrito)")

cursor.execute("INSERT INTO CodigoPostal VALUES ('28001', 'Salamanca', 'Salamanca')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28004', 'Justicia', 'Centro')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28012', 'Embajadores', 'Centro')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28028', 'Guindalera', 'Salamanca')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28045', 'Delicias', 'Arganzuela')")

cursor.execute("CREATE TABLE IF NOT EXISTS Usuario (id_usuario PRIMARY KEY, nombre, saldo, cp, FOREIGN KEY (cp) REFERENCES CodigoPostal(cp))")

cursor.execute("INSERT INTO Usuario VALUES (1, 'Lucía Fernández', 25.5, '28001')")
cursor.execute("INSERT INTO Usuario VALUES (2, 'Carlos Gómez', 10.0, '28004')")
cursor.execute("INSERT INTO Usuario VALUES (3, 'María López', 42.75, '28012')")
cursor.execute("INSERT INTO Usuario VALUES (4, 'Javier Ruiz', 0.0, '28028')")
cursor.execute("INSERT INTO Usuario VALUES (5, 'Ana Martín', 15.2, '28045')")

cursor.execute("CREATE TABLE IF NOT EXISTS Restaurante (id_restaurante PRIMARY KEY, nombre, cp, FOREIGN KEY (cp) REFERENCES CodigoPostal(cp))")

cursor.execute("INSERT INTO Restaurante VALUES (1, 'Pizzería Napoli', '28004')")
cursor.execute("INSERT INTO Restaurante VALUES (2, 'Sushi Madrid', '28001')")
cursor.execute("INSERT INTO Restaurante VALUES (3, 'Burger House', '28012')")
cursor.execute("INSERT INTO Restaurante VALUES (4, 'Taquería El Güero', '28045')")

cursor.execute("CREATE TABLE IF NOT EXISTS Plato (id_plato PRIMARY KEY, nombre, categoria, precio, id_restaurante, FOREIGN KEY (id_restaurante) REFERENCES Restaurante(id_restaurante))")

cursor.execute("INSERT INTO Plato VALUES (1, 'Pizza Margarita', 'Pizza', 9.5, 1)")
cursor.execute("INSERT INTO Plato VALUES (2, 'Pizza Cuatro Quesos', 'Pizza', 11.0, 1)")
cursor.execute("INSERT INTO Plato VALUES (3, 'Nigiri Salmón', 'Sushi', 6.5, 2)")
cursor.execute("INSERT INTO Plato VALUES (4, 'Maki Atún', 'Sushi', 7.8, 2)")
cursor.execute("INSERT INTO Plato VALUES (5, 'Hamburguesa Clásica', 'Hamburguesa', 8.9, 3)")
cursor.execute("INSERT INTO Plato VALUES (6, 'Hamburguesa BBQ', 'Hamburguesa', 10.5, 3)")
cursor.execute("INSERT INTO Plato VALUES (7, 'Tacos al Pastor', 'Mexicana', 8.0, 4)")
cursor.execute("INSERT INTO Plato VALUES (8, 'Burrito de Pollo', 'Mexicana', 7.5, 4)")

cursor.execute("CREATE TABLE IF NOT EXISTS Rider (id_rider PRIMARY KEY, nombre)")

cursor.execute("INSERT INTO Rider VALUES (1, 'Pablo Sánchez')")
cursor.execute("INSERT INTO Rider VALUES (2, 'Elena Torres')")
cursor.execute("INSERT INTO Rider VALUES (3, 'Diego Navarro')")

cursor.execute("CREATE TABLE IF NOT EXISTS Vehiculo (matricula PRIMARY KEY, tipo, marca, id_rider, FOREIGN KEY (id_rider) REFERENCES Rider(id_rider))")

cursor.execute("INSERT INTO Vehiculo VALUES ('1234ABC', 'Moto', 'Honda', 1)")
cursor.execute("INSERT INTO Vehiculo VALUES ('5678DEF', 'Bicicleta', 'Orbea', 2)")
cursor.execute("INSERT INTO Vehiculo VALUES ('9012GHI', 'Moto', 'Yamaha', 3)")

cursor.execute("CREATE TABLE IF NOT EXISTS Pedido (id_pedido PRIMARY KEY, fecha, id_usuario, id_rider, FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario), FOREIGN KEY (id_rider) REFERENCES Rider(id_rider))")

cursor.execute("INSERT INTO Pedido VALUES (1, '2026-10-10 13:45', 1, 1)")
cursor.execute("INSERT INTO Pedido VALUES (2, '2026-10-10 20:30', 2, 2)")
cursor.execute("INSERT INTO Pedido VALUES (3, '2026-10-11 14:10', 3, 3)")
cursor.execute("INSERT INTO Pedido VALUES (4, '2026-10-12 21:05', 5, 1)")
cursor.execute("INSERT INTO Pedido VALUES (5, '2026-10-13 13:20', 4, 2)")

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
