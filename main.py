import pandas as pd
from sqlconnector import SQLConnector


if __name__ == "__main__":
    sqlConnector = SQLConnector('copyManager', '|~qpc,wm*of/=%"$i7h!i; m2~i4vab^')
    conn = sqlConnector.create_connection()
    query = 'select * from MHM$Item'
    df = pd.read_sql(query, conn)
    print(df.head(5))
