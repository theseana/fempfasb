import mysql.connector


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            db='fempschool',
            user='root',
            password='3562!lop',
            host='localhost'    
        )

        self.cursor = self.db.cursor()


class StudentInsert(Database):
    def __init__(self, name, family, idNumber, birthDate, className ):
        Database.__init__(self)
        
        data = (name, family, idNumber, birthDate, className)
        query = """INSERT INTO student
        (name, family, idNumber, birthDate, className)
        VALUES
        (%s, %s, %s, %s, %s)"""

        self.cursor.execute(query, data)
        self.db.commit()

        self.cursor.close()
        self.db.close()


class StudentUpdate(Database):
    def __init__(self, colName, colValue, id):
        Database.__init__(self)
        
        data = (colValue, id)
        query = "UPDATE student SET " + colName + "=%s WHERE id=%s"

        self.cursor.execute(query, data)
        self.db.commit()

        self.cursor.close()
        self.db.close()


class StudentDelete(Database):
    def __init__(self, id):
        Database.__init__(self)

        data = (id,)
        query = "DELETE FROM student WHERE id=%s"

        self.cursor.execute(query, data)
        self.db.commit()

        self.cursor.close()
        self.db.close()


class StudentSelect(Database):
    def __init__(self, full_name):
        Database.__init__(self)

        query = "SELECT * FROM student"

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.row_numbers = []
        for row in result:
            if row[1] in full_name or row[2] in full_name:
                self.row_numbers.append(row)

        self.cursor.close()
        self.db.close()

    def get(self):
        return  self.row_numbers

# StudentInsert('fatemeh', 'nasibipour', '1478521456','2004-01-01', 'Red')