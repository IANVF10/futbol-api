#FUTBOL API

##By Ian Vidriales Fidalgo

###==CEV== 

-**First quarter class project**
-*This is an api with python about futbol*
->I have used the Planet Scale database

[API MER](api-mer.png)

`mycursor.execute("CREATE TABLE IF NOT EXISTS Equipos (Equipos_nombre VARCHAR(50) PRIMARY KEY, Presidente VARCHAR(50), Trofeos INT(3))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Jugadores (Jugador_nombre VARCHAR(50) PRIMARY KEY, Equipos_nombre VARCHAR(50), Trofeos INT(3), Sueldo INT(9))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Ranking_jugadores (Top INT AUTO_INCREMENT PRIMARY KEY, Jugador_nombre VARCHAR(50), Trofeos INT(3))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Ranking_equipos (Top INT AUTO_INCREMENT PRIMARY KEY, Equipos_nombre VARCHAR(50), Trofeos INT(3))")

mycursor.execute("CREATE TABLE IF NOT EXISTS Trofeos (Id INT AUTO_INCREMENT PRIMARY KEY, Trofeo VARCHAR(50), Jugador_nombre VARCHAR(50))")
`

[Link of my GitHub accout] (https://github.com/IANVF10)
