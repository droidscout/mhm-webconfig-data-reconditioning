import pyodbc

class SQLConnector:
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password
        self.connectionString = 'DRIVER={SQL SERVER};Server=smhmsql03;DATABASE=MHM_110;' + 'USER={user};PWD={pwd}'.format(user=self.user, pwd=self.password)
    
    def create_connection(self):
        return pyodbc.connect(self.connectionString)

    def create_cursor(self):
        return self.create_connection().cursor()

    def execute_query(self, queryString):
        cursor = self.__create_cursor()
        return cursor.execute(queryString).fetchone()

if __name__ == "__main__":
    sqlConnector = SQLConnector('copyManager', '|~qpc,wm*of/=%"$i7h!i; m2~i4vab^')
    results = sqlConnector.execute_query('select * from dbo.MHM$Item')
    print(results)