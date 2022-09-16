import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='KoneRoot',
    autocommit=True
)


def find_airport(icao):
    tuple = (icao,)
    sql = '''select name, municipality 
    from airport 
    where ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos


user = input('Anna ICAO: ')
kentta = find_airport(user)
if kentta is not None:
    print(f'Nimi: {kentta[0]}, kunta: {kentta[1]}')
