import sqlite3

from decouple import config


def get_sql_from_file(filename: str) -> str:
    try:
        with open(filename) as file:
            return file.read()
    except IOError as e:
        print(f"Error in file: {filename} cause: {e}")


class DBManager:

    def __init__(self, dbname: str):
        self.__connection = None
        try:
            self.__connection = sqlite3.connect(dbname)
        except sqlite3.Error as e:
            print(e)

    @property
    def connection(self) -> sqlite3.Connection:
        return self.__connection


class Repository:

    def __init__(self, db_manager: DBManager):
        self.__connection = db_manager.connection

    def execute_sql(self, sql, *args):
        try:
            sqlite3.enable_callback_tracebacks(True)
            cursor = self.__connection.cursor()
            cursor.execute(sql, args)
            if sql.strip().lower().startswith('select'):
                return cursor.fetchall()
            else:
                self.__connection.commit()
        except sqlite3.Error as e:
            print(f"Error in file: {sql} cause: {e}")


class CountryRepository(Repository):

    def __init__(self, db_manager: DBManager):
        super().__init__(db_manager)
        self.__create_table_ddl = get_sql_from_file(config("CREATE_TABLE_COUNTRY"))
        self.__insert_dml = get_sql_from_file(config("INSERT_COUNTRY"))
        self.__delete_dml = get_sql_from_file(config("DELETE_COUNTRY"))
        self.__delete_all_dml = get_sql_from_file(config("DELETE_ALL_COUNTRY"))
        self.__select_all_dml = get_sql_from_file(config("SELECT_ALL_COUNTRY"))
        self.__select_by_title_dml = get_sql_from_file(config("SELECT_BY_TITLE_COUNTRY"))
        self.__select_by_id_dml = get_sql_from_file(config("SELECT_BY_ID_COUNTRY"))
        self.execute_sql(self.__create_table_ddl)

    def insert(self, *args):
        self.execute_sql(self.__insert_dml, *args)

    def delete(self, *args):
        self.execute_sql(self.__delete_dml, *args)

    def delete_all(self, *args):
        self.execute_sql(self.__delete_all_dml)

    def find_all(self):
        return self.execute_sql(self.__select_all_dml)

    def find_by_title(self, title: str):
        return self.execute_sql(self.__select_by_title_dml, title)

    def find_by_id(self, id: int):
        return self.execute_sql(self.__select_by_id_dml, id)


class CityRepository(Repository):

    def __init__(self, db_manager: DBManager):
        super().__init__(db_manager)
        self.__create_table_ddl = get_sql_from_file(config("CREATE_TABLE_CITY"))
        self.__insert_dml = get_sql_from_file(config("INSERT_CITY"))
        self.__delete_dml = get_sql_from_file(config("DELETE_CITY"))
        self.__delete_all_dml = get_sql_from_file(config("DELETE_ALL_CITY"))
        self.__select_all_dml = get_sql_from_file(config("SELECT_ALL_CITY"))
        self.__select_by_title_dml = get_sql_from_file(config("SELECT_BY_TITLE_CITY"))
        self.__select_by_id_dml = get_sql_from_file(config("SELECT_BY_ID_CITY"))
        self.execute_sql(self.__create_table_ddl)

    def insert(self, *args):
        self.execute_sql(self.__insert_dml, *args)

    def delete(self, *args):
        self.execute_sql(self.__delete_dml, *args)

    def delete_all(self):
        self.execute_sql(self.__delete_all_dml)

    def find_all(self):
        return self.execute_sql(self.__select_all_dml)

    def find_by_title(self, *args):
        return self.execute_sql(self.__select_by_title_dml, *args)

    def find_by_id(self, id: int):
        return self.execute_sql(self.__select_by_id_dml, id)


class EmployeeRepository(Repository):

    def __init__(self, db_manager: DBManager):
        super().__init__(db_manager)
        self.__create_table_ddl = get_sql_from_file(config("CREATE_TABLE_EMPLOYEE"))
        self.__insert_dml = get_sql_from_file(config("INSERT_EMPLOYEE"))
        self.__delete_dml = get_sql_from_file(config("DELETE_EMPLOYEE"))
        self.__delete_all_dml = get_sql_from_file(config("DELETE_ALL_EMPLOYEE"))
        self.__select_all_dml = get_sql_from_file(config("SELECT_ALL_EMPLOYEE"))
        self.__select_by_last_name_dml = get_sql_from_file(config("SELECT_BY_LAST_NAME_EMPLOYEE"))
        self.__select_by_id_dml = get_sql_from_file(config("SELECT_BY_ID_EMPLOYEE"))
        self.__select_by_city_dml = get_sql_from_file(config("SELECT_BY_CITY_EMPLOYEE"))
        self.execute_sql(self.__create_table_ddl)

    def insert(self, *args):
        self.execute_sql(self.__insert_dml, *args)

    def delete(self, *args):
        self.execute_sql(self.__delete_dml, *args)

    def delete_all(self):
        self.execute_sql(self.__delete_all_dml)

    def find_all(self):
        return self.execute_sql(self.__select_all_dml)

    def find_by_last_name(self, *args):
        return self.execute_sql(self.__select_by_last_name_dml, *args)

    def find_by_city_id(self, *args):
        return self.execute_sql(self.__select_by_city_dml, *args)
