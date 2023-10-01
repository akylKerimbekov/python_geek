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

# procedural style
sql = """
select emp.first_name, emp.last_name, cntr.title as country_name, ct.title as city_name, ct.area
from employee emp
inner join city ct on ct.id = emp.city_id
inner join country cntr on cntr.id = ct.country_id
where emp.city_id = ?  
"""
ddl_country = """
create table if not exists country(
    id integer primary key autoincrement,
    title varchar(200) unique not null
)"""
ddl_city = """create table if not exists city(
    id integer primary key autoincrement,
    title varchar(200) unique not null,
    area float default 0,
    country_id integer
);"""
ddl_employee = """create table if not exists employee(
    id integer primary key autoincrement,
    first_name varchar(200) not null,
    last_name varchar(200) not null,
    city_id integer
);
"""
populate_country = """
insert into country(id, title)
select 1 as id, 'Kazakhstan' as title union all
select 2, 'Russia' union all
select 3, 'Kyrgyzstan';
"""
populate_city = """
insert into city
select 1 as id, 'Almaty' as title, 1 as area, 1 as country_id union all
select 2, 'Astana', 1, 1 union all
select 3, 'Moscow', 1, 2 union all
select 4, 'Saint-Petersburg', 1, 2 union all
select 5, 'Bishkek', 1, 3 union all
select 6, 'Osh', 1, 3;
"""
populate_employee = """
insert into employee
select 1 as id, 'Ivan' as first_name, 'Ivanov' as last_name, 4 as city_id  union all
select 2, 'Petr', 'Petrov', 3 union all
select 3, 'Asan', 'Asanov', 5 union all
select 4, 'Uson', 'Usonov', 6 union all
select 5, 'Daurenov', 'Daurenov', 1 union all
select 6, 'Berik', 'Berikov', 2;
"""

try:
    connection = sqlite3.connect("old.db")
    cursor = connection.cursor()
    cursor.execute("drop table country")
    cursor.execute("drop table city")
    cursor.execute("drop table employee")
    cursor.execute(ddl_country)
    cursor.execute(ddl_city)
    cursor.execute(ddl_employee)
    cursor.execute(populate_country)
    cursor.execute(populate_city)
    cursor.execute(populate_employee)
    connection.commit()

    cursor.execute(sql, [6])
    result = cursor.fetchall()
    for item in result:
        print(f"{item[0]} {item[1]} {item[2]} {item[3]} {item[4]}")
        print()

except:
    print(f"Error")

