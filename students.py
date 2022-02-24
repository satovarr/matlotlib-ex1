import pymysql

names = []
marks = []


class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',  # ip
            user='root',
            password='password',
            db='py_students'
        )
        self.cursor = self.connection.cursor()
        print("Connection succeed")

    def select_user(self, id):
        sql = 'SELECT name, marks FROM students WHERE id = {}'.format(id)

        try:
            self.cursor.execute(sql)
            user = self.cursor.fetchone()
            return [user[0], user[1]]

        except Exception as e:
            raise


database = DataBase()
# database.select_user(1)

for i in range(1, 7):
    user_data = database.select_user(i)
    names.append(user_data[0])
    marks.append(user_data[1])

print(names, marks)
