import sqlite3

from decouple import config


class ProductRepository:
    __dbname = config("DBNAME")
    __create_table_ddl = config("CREATE_TABLE")
    __insert_dml = config("INSERT")
    __update_dml = config("UPDATE")
    __upsert_dml = config("UPSERT")
    __delete_dml = config("DELETE")
    __delete_by_name_dml = config("DELETE_BY_NAME")
    __select_all_dml = config("SELECT_ALL")
    __select_by_price_and_quantity = config("SELECT_BY_PRICE_AND_QUANTITY")
    __select_by_title = config("SELECT_BY_TITLE")

    def __init__(self):
        self.__connection = None
        try:
            self.__connection = sqlite3.connect(self.__dbname)
            self.__execute_sql_from_file(self.__create_table_ddl)
        except sqlite3.Error as e:
            print(e)

    def __execute_sql_from_file(self, filename, *args):
        try:
            with open(filename) as file:
                cursor = self.__connection.cursor()
                sql = file.read()
                cursor.execute(sql, args)
                if sql.strip().lower().startswith('select'):
                    return cursor.fetchall()
                else:
                    self.__connection.commit()
        except sqlite3.Error as e:
            print(f"Error in file: {filename} cause: {e}")

    def insert(self, *args):
        self.__execute_sql_from_file(self.__insert_dml, *args)

    def update(self, *args):
        self.__execute_sql_from_file(self.__update_dml, *args)

    def upsert(self, *args):
        self.__execute_sql_from_file(self.__upsert_dml, *args)

    def delete(self, *args):
        self.__execute_sql_from_file(self.__delete_dml, *args)

    def delete_by_name(self, *args):
        self.__execute_sql_from_file(self.__delete_by_name_dml, *args)

    def find_all(self):
        return self.__execute_sql_from_file(self.__select_all_dml)

    def find_by_product_title(self, *args):
        title = "%" + args[0] + "%"
        return self.__execute_sql_from_file(self.__select_by_title, title)

    def find_by_price_and_quantity(self, *args):
        return self.__execute_sql_from_file(self.__select_by_price_and_quantity, *args)
