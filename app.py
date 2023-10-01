import sqlite3

from domain import Country, City, Employee
from repository import DBManager
from service import CountryService, CityService, EmployeeService
from decouple import config

dbname = config("DBNAME")
country_service = CountryService(dbname)
city_service = CityService(dbname)
employee_service = EmployeeService(dbname)

employee_service.delete_all()
city_service.delete_all()
country_service.delete_all()

country_service.create(Country(0, "Kyrgyzstan"))
country_service.create(Country(0, "Poland"))
country_service.create(Country(0, "Canada"))

kg = country_service.find_by_title("Kyrgyzstan")
pl = country_service.find_by_title("Poland")
ca = country_service.find_by_title("Canada")

city_service.create(City(0, "Bishkek", 129.89, kg))
city_service.create(City(0, "Osh", 12.0, kg))
city_service.create(City(0, "Warsaw", 434.65, pl))
city_service.create(City(0, "Krakow", 432.9, pl))
city_service.create(City(0, "Toronto", 75.7, ca))
city_service.create(City(0, "Montreal", 233.4, ca))
city_service.create(City(0, "Vancouver", 6565.7, ca))

bishkek = city_service.find_by_title("Bishkek")
osh = city_service.find_by_title("Osh")
warsaw = city_service.find_by_title("Warsaw")
krakow = city_service.find_by_title("Krakow")
toronto = city_service.find_by_title("Toronto")
montreal = city_service.find_by_title("Montreal")
vancouver = city_service.find_by_title("Vancouver")

employee_service.create(Employee(0, "Ivan", "Ivanov", bishkek))
employee_service.create(Employee(0, "Petr", "Petrov", bishkek))
employee_service.create(Employee(0, "Azamat", "Azamatov", bishkek))
employee_service.create(Employee(0, "Asan", "Asanov", osh))
employee_service.create(Employee(0, "Uson", "Usonov", osh))
employee_service.create(Employee(0, "Grzegorz", "Brzęczyszczykiewicz", warsaw))
employee_service.create(Employee(0, "Bartosz", "Narwik", warsaw))
employee_service.create(Employee(0, "Andrzejek", "Błażek", krakow))
employee_service.create(Employee(0, "Fredyk", "Boleczek", krakow))
employee_service.create(Employee(0, "Aaron", "Smith", toronto))
employee_service.create(Employee(0, "Blake", "Chuck", toronto))
employee_service.create(Employee(0, "Brandon", "Booth", montreal))
employee_service.create(Employee(0, "Clayton", "Trump", montreal))
employee_service.create(Employee(0, "Bernie", "Clinton", vancouver))
employee_service.create(Employee(0, "John", "Depp", vancouver))


def print_list(raw_list: list):
    for item in raw_list:
        print(item)
    print()


cities = city_service.find_all()
while True:
    print_list(cities)
    city_id = int(input("Вы можете отобразить список сотрудников по выбранному id "
                        "города из перечня городов, для выхода из программы введите 0: "))
    if city_id == 0:
        break
    city = city_service.find_by_id(city_id)
    employees_by_city = employee_service.find_by_city(city)
    print_list(employees_by_city)

    sql = """
    select emp.first_name, emp.last_name, cntr.title as country_name, ct.title as city_name, ct.area
    from employee emp
    inner join city ct on ct.id = emp.city_id
    inner join country cntr on cntr.id = ct.country_id
    where emp.city_id = ?  
    """

    # procedural style
    try:
        connection = sqlite3.connect(dbname)
        cursor = connection.cursor()
        cursor.execute(sql, [city_id])
        result = cursor.fetchall()
        for item in result:
            print(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}")
    except:
        print(f"Error")

