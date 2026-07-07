import pymysql

config = {'host': 'ich-db.edu.itcareerhub.de',
    'user': 'ich1',
    'password': 'password',
    'database': 'hr',
    }

connection = pymysql.connect(**config) # распаковка словаря как аргументы

if connection.open:
    print("Connection successful!")

connection.close()