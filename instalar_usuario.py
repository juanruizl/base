import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Usuario (id_usuario PRIMARY KEY, nombre, saldo, cp, FOREIGN KEY (cp) REFERENCES CodigoPostal(cp))")

cursor.execute("INSERT INTO Usuario VALUES (1, 'Lucía Fernández', 25.5, '28001')")
cursor.execute("INSERT INTO Usuario VALUES (2, 'Carlos Gómez', 10.0, '28004')")
cursor.execute("INSERT INTO Usuario VALUES (3, 'María López', 42.75, '28012')")
cursor.execute("INSERT INTO Usuario VALUES (4, 'Javier Ruiz', 0.0, '28028')")
cursor.execute("INSERT INTO Usuario VALUES (5, 'Ana Martín', 15.2, '28045')")

connexion.commit()
connexion.close()
