import datetime
import pymysql
import pandas as pd
from sqlalchemy import create_engine #sqlalchemy helped convert strings to dates seamlessly


#  This Works
# cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='3rdSemExam')  

# cursor = cnx.cursor()

# query = ("SELECT firstname, lastname, id FROM DRIVER")

# # hire_start = datetime.date(1960, 1, 1)
# # hire_end = datetime.date(2004, 12, 31)

# # cursor.execute(query, (hire_start, hire_end))
# cursor.execute(query)

# for (firstname, lastname, id) in cursor:
#   print("Name {} {} ---- ID {}".format(firstname, lastname, id))

# cursor.close()
# cnx.close()

#  This Works
# cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='pythonTest')

# cursor = cnx.cursor()

# query = ("SELECT firstname, lastname, startdate, enddate, salary FROM pythondemo WHERE startdate BETWEEN %s AND %s")

# hire_start = datetime.date(1960, 1, 1)
# hire_end = datetime.date(2004, 12, 31)

# cursor.execute(query, (hire_start, hire_end))

# for (firstname, lastname, startdate, enddate, salary) in cursor:
#     print("{} {} hired from {} to {} is paid: {} DKR pr month".format(firstname, lastname, startdate, enddate, salary))

# cursor.close()
# cnx.close()

# ---------------------------------------------------------------------------------------------------------------------
cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='pythonTest')
cursor = cnx.cursor()
myDict = {"personId": 111, "firstName": "John", "lastName": "Johnson"}

def persist_data(connector, dictionary, table_name):
    """persist data from dictionary into table of same structure"""
    columns = ', '.join(dictionary.keys())
    vals = tuple(dictionary.values())
    insert_str = 'INSERT INTO {table} ({cols}) values{vals}'.format(table=table_name, cols=columns, vals=vals)
    cursor = connector.cursor()
    cursor.execute(insert_str)
    id = cursor.lastrowid
    connector.commit()
    cursor.close()
    return id

print(persist_data(cnx, myDict, 'person'))
# -----------------------------------------------------------------------------------------------------


# #cnx = pymysql.connect(user='dev', password='ax2',host='127.0.0.1',port=3307,db='test') 
# con_str = 'mysql+pymysql://dev:ax2@localhost:3307/pythonTest'
# engine = create_engine(con_str)
# # df = pd.DataFrame({'firstname' : ['Ulrik', 'Ulla', 'Ulfred'],
# #                   'lastname':['Volborg','Willman','Valberg'],
# #                   'startdate':['2003-03-03','2001-05-04','2001-01-04'],
# #                   'enddate':['2005-08-20','2005-12-24','2006-10-30'],
# #                   'salary':['21000', '32000', '43000']})
# df = pd.read_csv('cars.csv')
# df.to_sql('cars2',con=engine, if_exists='append', index = False)