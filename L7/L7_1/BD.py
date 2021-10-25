from getpass import getpass
import mysql.connector


class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    def connect(self):
        if self.connection is None:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="animalsdb")
        return self.connection

    def get_animals(self):
        sql = '''SELECT Animalcode, Name
                FROM Animal;'''

        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def get_xoz(self):
        sql = '''SELECT Xozcode, fioxoz, telxoz
                FROM XOZ;'''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    

    def get_animalxoz(self):
        sql = '''Select Animal.Animalcode, Name, xoz.Xozcode, xoz.fioxoz, xoz.telxoz
                from Animal,xoz
                WHERE Animal.getxozcode = xoz.Xozcode
                GROUP BY Animalcode;'''
        cursor = self.connection.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def delete_animal(self, Animalcode):
        sql = 'DELETE FROM Animal where Animalcode = (%s)'
        cursor = self.connection.cursor()
        cursor.execute(sql, (Animalcode,))
        self.connection.commit()
        return cursor

    def insert_animal(self, Animalcode, Name, getxozcode):
        sql = '''INSERT INTO Animal (
                    Animalcode, Name, getxozcode
                )
                VALUES (%s, %s, %s);'''

        cursor = self.connection.cursor()
        cursor.execute(sql, (Animalcode, Name, getxozcode))
        self.connection.commit()

    def insert_xoz(self,Xozcode, fioxoz, telxoz):
        sql = '''INSERT INTO XOZ (
                    Xozcode,fioxoz,telxoz
                )
                VALUES (%s, %s, %s);'''

        cursor = self.connection.cursor()
        cursor.execute(sql, (Xozcode, fioxoz, telxoz))
        self.connection.commit()

        return cursor

    def close_connection(self):
        self.connection.close()