# import psycopg2
#
# conn = psycopg2.connect \
#         (
#         database="linehaul_dev",
#         user="linehauluser",
#         password="LH@1234",
#         host="192.168.0.38", port="5432")
# print("Database Connected....")
import pypyodbc

con = pypyodbc.connect("Driver={SQL Server};"
                       "Database=app_test;"
                       "uid=web_merge_ec;pwd=w3bm3rg33c")
print("Database Connected....")
