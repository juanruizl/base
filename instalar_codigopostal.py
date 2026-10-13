import sqlite3

connexion = sqlite3.connect("riders_express")
cursor = connexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS CodigoPostal (cp PRIMARY KEY, barrio, distrito)")

cursor.execute("INSERT INTO CodigoPostal VALUES ('28001', 'Salamanca', 'Salamanca')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28004', 'Justicia', 'Centro')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28012', 'Embajadores', 'Centro')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28028', 'Guindalera', 'Salamanca')")
cursor.execute("INSERT INTO CodigoPostal VALUES ('28045', 'Delicias', 'Arganzuela')")

connexion.commit()
connexion.close()
