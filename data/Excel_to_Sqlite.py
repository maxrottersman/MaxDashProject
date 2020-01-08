import sqlite3
import pandas as pd
from pathlib import Path
#if csv file
# df = pd.read_csv('ourfile.csv')

# assume script in root of our project
ScriptPath = Path.cwd()
# assume our database in folder /sqlite_db
dbPath = ScriptPath / 'data'
# get system neutral (win/unix) path and convert to string
dbPathandFileStr = str(dbPath / 'ETFdata.sqlite')
xlPathandFileStr = str(dbPath / 'data.xlsx')

conn = sqlite3.connect(dbPathandFileStr)

#Excel file
# Tables: (case matters!)
lstTables = ["Data_ETFs", "Data_ETFs_UniqueManagers", "Data_ETFs_UniqueCategories"]
# We explicity say which table to put in database.

for tbl in lstTables:
    sqldrop = "DROP TABLE IF EXISTS " + tbl
    cursor = conn.cursor()
    cursor.execute(sqldrop)
    df = pd.read_excel(xlPathandFileStr,sheet_name=tbl)
    # df if_exists isn't working so manually dropping above
    df.to_sql(name=tbl, con=conn, if_exists='replace')
    conn.commit()
    

#dfs = pd.read_excel(xlPathandFileStr, sheet_name=None)
# this wasn't working? but if want to use sheet names figure out
#for table, df in dfs.items():
#    df.to_sql(name=table, if_exists='replace',con=conn)
#    conn.commit()
# this worked
# replace means drop first
#for tbl in lstTables:
#    df.to_sql(name=tbl,  if_exists='replace',con=conn)
#    conn.commit()

# test
# cur = conn.cursor()
# sqlstr = 'Select * from ' + lstTables[1]
# cur.execute(sqlstr)
# for row in cur:
#     print(row)

conn.close()