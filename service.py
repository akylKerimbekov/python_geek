from decouple import config

from domain import Country, City, Employee
from repository import DBManager, CountryRepository, CityRepository, EmployeeRepository


class Service:

    def __init__(self, dbname: str):
        if dbname is None:
            dbname = config("DBNAME")
        self.__db_manager = DBManager(dbname)

    @property
    def db_manager(self) -> DBManager:
        return self.__db_manager


class CountryService(Service):

    def __init__(self, dbname):
        super().__init__(dbname)
        self.__repository = CountryRepository(self.db_manager)

    def create(self, country: Country) -> None:
        self.__repository.insert(country.title)

    def find_all(self) -> list:
        raw_list = self.__repository.find_all()
        countries = list()
        for item in raw_list:
            countries.append(Country(item[0], item[1]))
        return countries

    def find_by_title(self, title: str) -> Country:
        raw_list = self.__repository.find_by_title(title)
        country = Country(raw_list[0][0], raw_list[0][1])
        return country

    def find_by_id(self, id: int) -> Country:
        raw_list = self.__repository.find_by_id(id)
        country = Country(raw_list[0][0], raw_list[0][1])
        return country

    def delete_by_id(self, id: int) -> None:
        self.__repository.delete(id)

    def delete_all(self) -> None:
        self.__repository.delete_all()


class CityService(Service):

    def __init__(self, dbname):
        super().__init__(dbname)
        self.__repository = CityRepository(self.db_manager)
        self.__country_service = CountryService(dbname)

    def create(self, city: City) -> None:
        self.__repository.insert(city.title, city.area, city.country.id)

    def find_all(self) -> list:
        raw_list = self.__repository.find_all()
        cities = list()
        for item in raw_list:
            country = self.__country_service.find_by_id(item[3])
            cities.append(City(item[0], item[1], item[2], country))
        return cities

    def find_by_title(self, title: str) -> City:
        raw_list = self.__repository.find_by_title(title)
        country = self.__country_service.find_by_id(raw_list[0][3])
        city = City(raw_list[0][0], raw_list[0][1], raw_list[0][2], country)
        return city

    def find_by_id(self, id: int) -> City:
        raw_list = self.__repository.find_by_id(id)
        country = self.__country_service.find_by_id(raw_list[0][3])
        city = City(raw_list[0][0], raw_list[0][1], raw_list[0][2], country)
        return city

    def delete_by_id(self, id: int) -> None:
        self.__repository.delete(id)

    def delete_all(self) -> None:
        self.__repository.delete_all()


class EmployeeService(Service):

    def __init__(self, dbname):
        super().__init__(dbname)
        self.__repository = EmployeeRepository(self.db_manager)
        self.__city_service = CityService(dbname)

    def create(self, employee: Employee) -> None:
        self.__repository.insert(employee.first_name, employee.last_name, employee.city.id)

    def find_all(self) -> list:
        raw_list = self.__repository.find_all()
        employees = list()
        for item in raw_list:
            city = self.__city_service.find_by_id(item[3])
            employees.append(Employee(item[0], item[1], item[2], city))
        return employees

    def find_by_last_name(self, last_name: str) -> Employee:
        raw_list = self.__repository.find_by_last_name(last_name)
        city = self.__city_service.find_by_id(raw_list[0][3])
        employee = Employee(raw_list[0][0], raw_list[0][1], raw_list[0][2], city)
        return employee

    def find_by_city(self, city: City) -> list:
        raw_list = self.__repository.find_by_city_id(city.id)
        employees = list()
        for item in raw_list:
            city = self.__city_service.find_by_id(item[3])
            employees.append(Employee(item[0], item[1], item[2], city))
        return employees

    def delete_by_id(self, id: int) -> None:
        self.__repository.delete(id)

    def delete_all(self) -> None:
        self.__repository.delete_all()
