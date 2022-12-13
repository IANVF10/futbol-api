import mysql.connector

MYSQLhost = "aws-eu-west-2.connect.psdb.cloud"
MYSQLuser = "24bfbu5jk7thyvkjx6rx"
#MYSQLport = ""
MYSQLpassword = "pscale_pw_ovmO902pfSJ6oD2gXmhKlnxVp1v5xNDnvzZ3rv3ehwd"
MYSQLdatabase = "ian-api"

mydb = mysql.connector.connect(
  host = MYSQLhost,
  user = MYSQLuser,
  #port = MYSQLport,
  password = MYSQLpassword,
  database = MYSQLdatabase
)
print(mydb)


mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Equipos (Equipos_nombre VARCHAR(50) PRIMARY KEY, Presidente VARCHAR(50), Trofeos INT(3))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Jugadores (Jugador_nombre VARCHAR(50) PRIMARY KEY, Equipos_nombre VARCHAR(50), Trofeos INT(3), Sueldo INT(9))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Ranking_jugadores (Top INT AUTO_INCREMENT PRIMARY KEY, Jugador_nombre VARCHAR(50), Trofeos INT(3))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Ranking_equipos (Top INT AUTO_INCREMENT PRIMARY KEY, Equipos_nombre VARCHAR(50), Trofeos INT(3))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Trofeos (Id INT AUTO_INCREMENT PRIMARY KEY, Trofeo VARCHAR(50), Jugador_nombre VARCHAR(50))")

"""
sqlEquipos = "INSERT INTO Equipos (Equipos_nombre, Presidente, Trofeos) VALUES (%s, %s, %s)"
valEquipos = [
  ('Palmeiras', 'Leila Mejdalani Pereira', '23'),
  ('SSC Napoli', 'Aurelio De Laurentiis​', '13'),
  ('Manchester City', 'Ferran Soriano', '29'),
  ('Flamengo', 'Rodolfo Landim​', '19'),
  ('Tottenham Hotspur', 'Daniel Levy', '26'),
  ('AC Milan', 'Ivan Gazidis', '52'),
  ('Ajax Amsterdam', 'Edwin van der Sar', '76'),
  ('Arsenal', 'Vinai Venkatesham', '47'),
  ('Sporting', 'Alejandro Irarragorri', '50'),
  ('Atlanta', 'Darren Eales', '7'),
  ('Chelsea FC', 'Todd Boehly', '34'),
  ('Real Madrid', 'Florentino Perez Rodriguez', '127'),
  ('Villareal', 'Fernando Roig Alfonso', '1'),
  ('Bayern Munich', 'Herbert Hainer', '77'),
  ('Inter Milan', 'Steven Zhang', '42'),
  ('Barcelona', 'Joan Laporta Estruch', '90'),
  ('París Saint-Germain FC', 'Nasser Al-Khelaïfi', '45'),
  ('Benfica', 'Rui Costa', '80'),
  ('Liverpool FC', 'Tom Werner', '70'),
  ('Atlético Madrid', 'Enrique Cerezo', '32')
]
mycursor.executemany(sqlEquipos, valEquipos)

mydb.commit()


sqlJugadores = "INSERT INTO Jugadores (Jugador_nombre, Equipos_nombre, Trofeos, Sueldo) VALUES (%s, %s, %s, %s)"
valJugadores = [
  ('Romelu Lukaku', 'Inter de Milán', '10', '70000000'),
  ('Harry Kane', 'Tottenham Hotspur', '11', '90000000'),
  ('Paul Pogba', 'Juventus de Turín', '15', '48000000'),
  ('Joshua Kimmich', 'Bayern Múnich', '21', '80000000'),
  ('Gianluigi Donnarumma', 'París Saint-Germain FC', '5', '50000000'),
  ('Luis Suarez', 'Club Nacional', '27', '8000000'),
  ('Edouard Mendy', 'Chelsea FC', '5', '25000000'),
  ('Mohamed Salah', 'Liverpool FC', '20', '80000000'),
  ('Cristiano Ronaldo', 'Manchester United', '83', '20000000'),
  ('Kevin De Bruyne', 'Manchester City', '22', '80000000'),
  ('N’Golo Kante', 'Chelsea FC', '11', '30000000'),
  ('Robert Lewandowski', 'FC Barcelona', '61', '45000000'),
  ('Angel Di Maria', 'Juventus de Turín', '32', '12000000'),
  ('Neymar', 'París Saint-Germain FC', '33', '75000000'),
  ('Karim Benzema', 'Real Madrid', '61', '35000000'),
  ('Erling Haaland', 'Manchester City', '10', '170000000'),
  ('Lionel Messi', 'París Saint-Germain FC', '89', '50000000'),
  ('Son Heung-min', 'Tottenham Hotspur', '12', '70000000'),
  ('Bruno Fernandes', 'Manchester United', '10', '75000000'),
  ('Kylian Mbappe', 'París Saint-Germain FC', '31', '160000000')
]
mycursor.executemany(sqlJugadores, valJugadores)

mydb.commit()


sqlRankJugadores = "INSERT INTO Ranking_jugadores (Jugador_nombre, Trofeos) VALUES (%s, %s)"
valRankJugadores = [
  ('Lionel Messi', '89'),
  ('Cristiano Ronaldo', '83'),
  ('Robert Lewandowski', '61'),
  ('Mohamed Salah', '20'),
  ('Kylian Mbappe', '31'),
  ('Erling Haaland', '10'),
  ('Karim Benzema', '61'),
  ('N’Golo Kante', '11'),
  ('Kevin De Bruyne', '22'),
  ('Neymar', '33'),
  ('Luis Suarez', '27'),
  ('Romelu Lukaku', '10'),
  ('Angel Di Maria', '32'),
  ('Bruno Fernandes', '10'),
  ('Joshua Kimmich', '21'),
  ('Paul Pogba', '15'),
  ('Son Heung-min', '12'),
  ('Harry Kane', '11'),
  ('Gianluigi Donnarumma', '5'),
  ('Edouard Mendy', '5')
]
mycursor.executemany(sqlRankJugadores, valRankJugadores)

mydb.commit()


sqlRankEquipos = "INSERT INTO Ranking_equipos (Equipos_nombre, Trofeos) VALUES (%s, %s)"
valRankEquipos = [
  ('Real Madrid', '127'),
  ('Manchester City', '29'),
  ('Bayern Munich', '77'),
  ('Liverpool FC', '70'),
  ('SSC Napoli', '13'),
  ('París Saint-Germain FC', '45'),
  ('Barcelona', '90'),
  ('AC Milan', '52'),
  ('Ajax Amsterdam', '76'),
  ('Arsenal', '47'),
  ('Atlético Madrid', '32'),
  ('Benfica', '80'),
  ('Tottenham Hotspur', '26'),
  ('Villareal', '1'),
  ('Inter Milan', '42'),
  ('Flamengo', '19'),
  ('Chelsea FC', '34'),
  ('Palmeiras', '23'),
  ('Sporting', '50'),
  ('Atlanta', '7')
]
mycursor.executemany(sqlRankEquipos, valRankEquipos)

mydb.commit()


sqlTrofeos = "INSERT INTO Trofeos (Trofeo, Jugador_nombre) VALUES (%s, %s)"
valTrofeos = [
  ('The Best', 'Lionel Messi'),
  ('Balon de Oro', 'Lionel Messi'),
  ('Bota de Oro', 'Lionel Messi'),
  ('The Best', 'Cristiano Ronaldo'),
  ('Balon de Oro', 'Cristiano Ronaldo'),
  ('Bota de Oro', 'Cristiano Ronaldo'),
  ('The Best', 'Robert Lewandowski'),
  ('Bota de Oro', 'Robert Lewandowski'),
  ('Bota de Oro', 'Mohamed Salah'),
  ('Mundial', 'Kylian Mbappé'), 
  ('Balon de Oro', 'Karim Benzema'),
  ('Mundial', "N'Golo Kanté"),
  ('Bota de Oro', 'Luis Suárez'),
  ('Mundial', 'Paul Pogba'),
  ('Bota de Oro', 'Heung-min Son'),
  ('Bota de Oro', 'Harry Kane'),
]
mycursor.executemany(sqlTrofeos, valTrofeos)

mydb.commit()
"""

while True:

  print("Estas son las tablas de la API: ")

  print("1: Equipos")
  print("2: Jugadores")
  print("3: Ranking de los Jugadores")
  print("4: Ranking de los Equipos")
  print("5: Trofeos")


  print("Puedes hacer lo siguiete: ")

  print("1: Ver una tabla")
  print("2: Insertar datos en una tabla")
  print("3: Borrar datos de una tabla")
  print("4: Modificar un dato de una tabla")
  print("5: Crear una tabla")
  print("6: Borrar una tabla")
  print("7: Salir")

  accion = int(input("¿Qué vas a hacer? "))

  if accion == 1:

    print("1: Equipos")
    print("2: Jugadores")
    print("3: Ranking de los Jugadores")
    print("4: Ranking de los Equipos")
    print("5: Trofeos")

    verTabla = int(input("¿Qué tabla quieres ver? "))

    if verTabla == 1:
      mycursor.execute("SELECT * FROM Equipos")
      print(mycursor.fetchall())

    elif verTabla == 2:
      mycursor.execute("SELECT * FROM Jugadores")
      print(mycursor.fetchall())

    elif verTabla == 3:
      mycursor.execute("SELECT * FROM Ranking_jugadores")
      print(mycursor.fetchall())

    elif verTabla == 4:
      mycursor.execute("SELECT * FROM Ranking_equipos")
      print(mycursor.fetchall())

    elif verTabla == 5:
      mycursor.execute("SELECT * FROM Trofeos")
      print(mycursor.fetchall())

  elif accion == 2:

    print("1: Equipos")
    print("2: Jugadores")
    print("3: Ranking de los Jugadores")
    print("4: Ranking de los Equipos")
    print("5: Trofeos")

    nuevoDato = int(input("¿En que tabla quieres insertar un nuevo dato? "))

    if nuevoDato == 1:
      nuevoEquipo = input("¿Cual es el nombre del equipo? ")
      nuevoPresidente = input("¿Como se llama el presidente? ")
      nuevoTrofeosEquipo = int(input("¿Cuantos trofeos tiene? "))
      sqlEquipos = "INSERT INTO Equipos (Equipos_nombre, Presidente, Trofeos) VALUES (%s, %s, %s)"
      valEquipos = (nuevoEquipo, nuevoPresidente, nuevoTrofeosEquipo)
      mycursor.execute(sqlEquipos, valEquipos)
      mydb.commit()

    elif nuevoDato == 2:
      nuevoJugador = input("¿Cual es el nombre del jugador? ")
      nuevoEquipoJugador = input("¿En que equipo juega? ")
      nuevoTrofeosJugador = int(input("¿Cuantos trofeos tiene? "))
      nuevoSueldo = int(input("¿Cuanto gana al año? "))
      sqlJugadores = "INSERT INTO Jugadores (Jugador_nombre, Equipos_nombre, Trofeos, Sueldo) VALUES (%s, %s, %s, %s)"
      valJugadores = (nuevoJugador, nuevoEquipoJugador, nuevoTrofeosJugador, nuevoSueldo)
      mycursor.execute(sqlJugadores, valJugadores)
      mydb.commit()

    elif nuevoDato == 3:
      nuevoJugadorRanking = input("¿Cual es el nombre del jugador? ")
      nuevoTrofeoRankingJugadores = int(input("¿Cuantos trofeos tiene? "))
      sqlRankJugadores = "INSERT INTO Ranking_jugadores (Jugador_nombre, Trofeos) VALUES (%s, %s)"
      valRankJugadores = (nuevoJugadorRanking, nuevoTrofeoRankingJugadores)
      mycursor.execute(sqlRankJugadores, valRankJugadores)
      mydb.commit()
    
    elif nuevoDato == 4:
      nuevoEquipoRanking = input("¿Cual es el nombre del equipo? ")
      nuevoTrofeoRankingEquipos = int(input("¿Cuantos trofeos tiene? "))
      sqlRankEquipos = "INSERT INTO Ranking_equipos (Equipos_nombre, Trofeos) VALUES (%s, %s)"
      valRankEquipos = (nuevoEquipoRanking, nuevoTrofeoRankingEquipos)
      mycursor.execute(sqlRankEquipos, valRankEquipos)
      mydb.commit()

    elif nuevoDato == 5:
      nuevoTrofeo = input("¿Cual es el nombre del trofeo? ")
      nuevoJugadorNombre = input("¿Como se llama el jugador? ")
      sqlTrofeos = "INSERT INTO Trofeos (Trofeo, Jugador_nombre) VALUES (%s, %s)"
      valTrofeos = (nuevoTrofeo, nuevoJugadorNombre)
      mycursor.execute(sqlTrofeos, valTrofeos)
      mydb.commit()

  elif accion == 3:

    print("1: Equipos")
    print("2: Jugadores")
    print("3: Ranking de los Jugadores")
    print("4: Ranking de los Equipos")
    print("5: Trofeos")

    eliminarDato = int(input("¿De que tabla quieres eliminar un dato? "))

    if eliminarDato == 1:

      mycursor.execute("SELECT * FROM Equipos")
      print(mycursor.fetchall())
      eliminarEquipo = input("¿Qué equipo quieres eliminar? ")

      sqlEquipos = f"DELETE FROM Equipos WHERE Equipos_nombre = '{eliminarEquipo}'"
      mycursor.execute(sqlEquipos)
      mydb.commit()
    
    elif eliminarDato == 2:

      mycursor.execute("SELECT * FROM Jugadores")
      print(mycursor.fetchall())
      eliminarJugador = input("¿Qué jugador quieres eliminar? ")

      sqlJugadores = f"DELETE FROM Jugadores WHERE Jugador_nombre = '{eliminarJugador}'"
      mycursor.execute(sqlJugadores)
      mydb.commit()

    elif eliminarDato == 3:

      mycursor.execute("SELECT * FROM Ranking_jugadores")
      print(mycursor.fetchall())
      eliminarJugadorRank = input("¿Qué jugador quieres eliminar? ")

      sqlRankJugadores = f"DELETE FROM Ranking_jugadores WHERE Jugador_nombre = '{eliminarJugadorRank}'"
      mycursor.execute(sqlRankJugadores)
      mydb.commit()

    elif eliminarDato == 4:

      mycursor.execute("SELECT * FROM Ranking_equipos")
      print(mycursor.fetchall())
      eliminarEquipoRank = input("¿Qué equipo quieres eliminar? ")

      sqlRankEquipos = f"DELETE FROM Ranking_equipos WHERE Equipo_nombre = '{eliminarEquipoRank}'"
      mycursor.execute(sqlRankEquipos)
      mydb.commit()

    elif eliminarDato == 5:

      mycursor.execute("SELECT * FROM Trofeos")
      print(mycursor.fetchall())
      eliminarTrofeo = input("¿Qué trofeo quieres eliminar? ")

      sqlTrofeos = f"DELETE FROM Trofeos WHERE Trofeo = '{eliminarTrofeo}'"
      mycursor.execute(sqlTrofeos)
      mydb.commit()

  elif accion == 4:

    print("1: Equipos")
    print("2: Jugadores")
    print("3: Ranking de los Jugadores")
    print("4: Ranking de los Equipos")
    print("5: Trofeos")

    modificarDato = int(input("¿De que tabla quieres modificar un dato? "))

    if modificarDato == 1:

      mycursor.execute("SELECT * FROM Equipos")
      print(mycursor.fetchall())
      modificarEquipoQuitar = input("¿Qué equipo quieres modificar? ")
      modificarEquipoPoner = input("¿Qué equipo quieres poner? ")

      sqlEquipos = f"UPDATE Equipos SET Equipos_nombre = '{modificarEquipoPoner}' WHERE Equipos_nombre = '{modificarEquipoQuitar}'"
      mycursor.execute(sqlEquipos)
      mydb.commit()  

    elif modificarDato == 2:

      mycursor.execute("SELECT * FROM Jugadores")
      print(mycursor.fetchall())
      modificarJugadorQuitar = input("¿Qué jugador quieres modificar? ")
      modificarJugadorPoner = input("¿Qué jugador quieres poner? ")

      sqlJugadores = f"UPDATE Equipos SET Jugador_nombre = '{modificarJugadorPoner}' WHERE Jugador_nombre = '{modificarJugadorQuitar}'"
      mycursor.execute(sqlJugadores)
      mydb.commit() 

    elif modificarDato == 3:

      mycursor.execute("SELECT * FROM Ranking_jugadores")
      print(mycursor.fetchall())
      modificarJugadorRankQuitar = input("¿Qué jugador quieres modificar? ")
      modificarJugadorRankPoner = input("¿Qué jugador quieres poner? ")

      sqlRankJugadores = f"UPDATE Equipos SET Ranking_jugadores = '{modificarJugadorRankPoner}' WHERE Ranking_jugadores = '{modificarJugadorRankQuitar}'"
      mycursor.execute(sqlRankJugadores)
      mydb.commit() 

    elif modificarDato == 4:

      mycursor.execute("SELECT * FROM Ranking_equipos")
      print(mycursor.fetchall())
      modificarEquipoRankQuitar = input("¿Qué equipo quieres modificar? ")
      modificarEquipoRankPoner = input("¿Qué equipo quieres poner? ")

      sqlRankEquipos = f"UPDATE Equipos SET Ranking_equipos = '{modificarEquipoRankPoner}' WHERE Ranking_equipos = '{modificarEquipoRankQuitar}'"
      mycursor.execute(sqlRankEquipos)
      mydb.commit() 

    elif modificarDato == 5:

      mycursor.execute("SELECT * FROM Trofeos")
      print(mycursor.fetchall())
      modificarTrofeoQuitar = input("¿Qué trofeo quieres modificar? ")
      modificarTrofeoPoner = input("¿Qué trofeo quieres poner? ")

      sqlTrofeos = f"UPDATE Trofeos SET Trofeo = '{modificarTrofeoPoner}' WHERE Trofeo = '{modificarTrofeoQuitar}'"
      mycursor.execute(sqlTrofeos)
      mydb.commit() 
    
  if accion == 5:
    nombreTabla = input("¿Cómo quieres llamar a la tabla? ")
    numeroCampos = int(input("¿Cuántos campos quieres añadir? "))
    sqlNuevaTabla = f"CREATE TABLE IF NOT EXISTS {nombreTabla} ("

    for x in range(numeroCampos):

      nombreCampo = input("¿Cómo quieres llamar al campo? ")
      tipoCampo = input("¿Qué tipo de dato quieres que sea el campo? ")
      primaryKey = input("¿Es PRIMARY KEY? ")
      autoIncrement = input("¿Es AUTO_INCREMENT? ")
      sqlNuevaTabla = sqlNuevaTabla + nombreCampo + " " + tipoCampo

      if primaryKey == "si":
        sqlNuevaTabla = sqlNuevaTabla + " PRIMARY KEY"
      if autoIncrement == "si":
        sqlNuevaTabla = sqlNuevaTabla + " AUTO_INCREMENT"
      if x < numeroCampos - 1:
        sqlNuevaTabla = sqlNuevaTabla + ", "

    sqlNuevaTabla = sqlNuevaTabla + ")"

    print(sqlNuevaTabla)

    mycursor.execute(sqlNuevaTabla)
  
  if accion == 6:

    borrarTabla = (input("¿Cuál es el nombre de la tabla que quieres borrar? "))

    sqlBorrarTabla = f"DROP TABLE {borrarTabla}"
    mycursor.execute(sqlBorrarTabla)

  if accion == 7:
    break