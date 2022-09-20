import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='KoneRoot',
    autocommit=True)


def getLatLong(icao):
    user = (icao,)
    sql = '''select latitude_deg, longitude_deg
           from airport
           where ident = %s'''
    mycursor = connection.cursor()
    mycursor.execute(sql, user)
    results = mycursor.fetchall()
    return results


print('\nAnna kahden kentän ICAO. Ohjelma laskee kenttien etäisyyden:')

pos = []
for x in range(2):
    user = input('ICAO: ')
    pos.append(getLatLong(user))

print(f'Kenttien välinen etäisyys on: {distance.distance(pos[0],pos[1]).km}km')
