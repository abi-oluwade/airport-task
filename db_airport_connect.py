import pyodbc

server = 'localhost,1433'
database = 'Airports'
username = 'SA'
password = 'Passw0rd2018'

docker_Airports = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+''
';UID='+username+';PWD='+ password)

cursor = docker_Airports.cursor()

cursor.execute("SELECT * FROM flight_class WHERE origin = 'New York'")

row = cursor.fetchone()
print(row)
print(cursor.fetchone())
