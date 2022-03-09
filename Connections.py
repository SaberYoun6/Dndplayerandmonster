__authors__ = "Saberina Young"
__copyright__ = "Player and MOnsters 2022, Squid Mythos Hammer Industries"
__name__of_file__ = "Connections.py"
__credits__ = ["Saberina Young"]
__license__ = "GPL 3.0"
__maintianer__ = "Saberina Young"
__email__ = "Saberina.young.103@gmail.com"
__stauts__ = "Aplha"

#depencies 
#import mysql.connector this is for windows machine
import os
import mariadb #this is for fedora machine
import sys
class connnection(object):
    def connection_creation(self):
        try:
            mydb =mariadb.connect(
                    user=os.getenv('DB_USER'),
                    password=os.getenv('DB_PASSWORD'),
                    host=os.getenv('DB_HOST'),
                    database = os.getenv('DB_DATABASE'),
                    port=3306)
            cur = mydb.cursor()
            database=cur.execute("show databases")
            for db in database:
                print(db)
            
            mydb.close()
        except mariadb.Error as e:
            print("Failed to call DATABASE {}".format(e))
            sys.exit(1)


