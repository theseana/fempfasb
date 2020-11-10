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
    def __init__(self, name, family, idNumber, birthDate, className, id):
        Database.__init__(self)
        
        data = (name, family, idNumber, birthDate, className, id)
        query = """UPDATE student
        SET name=%s, family=%s, idNumber=%s, birthDate=%s, className=%s
        WHERE id=%s"""

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
        self.result = self.cursor.fetchall()
        self.row_numbers = []
        for row in self.result:
            if row[1] in full_name or row[2] in full_name:
                self.row_numbers.append(row)

        self.cursor.close()
        self.db.close()

    def get(self):
        return  self.row_numbers


class GradeInsert(Database):
    def __init__(self, math, history, physics, chemistry, programming, id):
        Database.__init__(self)
        
        data = (math, history, physics, chemistry, programming, id)
        query = """INSERT INTO grade
        (math, history, physics, chemistry, programming, studentId)
        VALUES
        (%s, %s, %s, %s, %s, %s)"""

        self.cursor.execute(query, data)
        self.db.commit()

        self.cursor.close()
        self.db.close()


class GradeSelect(Database):
    def __init__(self, id):
        Database.__init__(self)

        query = "SELECT * FROM grade WHERE studentId=%s" % id

        self.cursor.execute(query)
        self.result = self.cursor.fetchall()

        self.cursor.close()
        self.db.close()
print(GradeSelect(8).result)