import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='KoneRoot',
    autocommit=True
)


def haeTyypit():
    sql = 'select distinct type from airport;'
    kursori = yhteys.cursor()
    kursori.execute(sql,)
    tulos = kursori.fetchall()
    return tulos

def haeKenttienLkm(maakoodi, tyyppi):
    sql = '''select count(type) from airport
    where iso_country = %s
    and type = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi, tyyppi))
    tulos = kursori.fetchone()
    return tulos

maakoodi = input('Anna maakoodi: ')

tyypit = haeTyypit()

for tyyppi in tyypit:
    lkm = haeKenttienLkm(maakoodi, tyyppi[0])
    print(f'{tyyppi[0]} lukumäärä: {lkm[0]}')
