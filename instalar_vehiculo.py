import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Vehiculo (matricula PRIMARY KEY, tipo, marca, id_rider, FOREIGN KEY (id_rider) REFERENCES Rider(id_rider))")

cursor.execute("INSERT INTO Vehiculo VALUES ('1234ABC', 'Moto', 'Honda', 1)")
cursor.execute("INSERT INTO Vehiculo VALUES ('5678DEF', 'Bicicleta', 'Orbea', 2)")
cursor.execute("INSERT INTO Vehiculo VALUES ('9012GHI', 'Moto', 'Yamaha', 3)")

connexion.commit()
connexion.close()
