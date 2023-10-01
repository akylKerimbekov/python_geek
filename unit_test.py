import unittest

from domain import Country, City, Employee
from service import CountryService, CityService, EmployeeService


class CountryTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = CountryService("db/test.db")
        self.obj.delete_all()

    def test_insert(self):
        actual_country = Country(0, "Kyrgyzstan")
        self.obj.create(actual_country)
        expect_country = self.obj.find_by_title("Kyrgyzstan")
        self.obj.delete_all()
        self.assertEqual(actual_country.title, expect_country.title)

    def test_delete(self):
        actual_country = Country(0, "Kyrgyzstan")
        self.obj.create(actual_country)
        expect_country = self.obj.find_by_title("Kyrgyzstan")
        self.obj.delete_by_id(expect_country.id)
        self.assertRaises(IndexError, self.obj.find_by_title, "Kyrgyzstan")

    def test_select(self):
        self.obj.create(Country(0, "Kyrgyzstan"))
        self.obj.create(Country(0, "Poland"))
        expected_list = self.obj.find_all()
        self.assertEqual(2, len(expected_list))
        self.obj.delete_all()


class CityTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = CityService("db/test.db")
        self.obj_country = CountryService("db/test.db")
        self.obj.delete_all()
        self.obj_country.delete_all()

    def test_insert(self):
        self.obj_country.create(Country(0, "Kyrgyzstan"))
        country = self.obj_country.find_by_title("Kyrgyzstan")
        actual_city = City(0, "Bishkek", 198.0, country)
        self.obj.create(actual_city)
        expect_city = self.obj.find_by_title("Bishkek")
        self.obj.delete_all()
        self.obj_country.delete_all()
        self.assertEqual(actual_city.title, expect_city.title)

    def test_delete(self):
        self.obj_country.create(Country(0, "Kyrgyzstan"))
        country = self.obj_country.find_by_title("Kyrgyzstan")
        actual_city = City(0, "Bishkek", 198.0, country)
        self.obj.create(actual_city)
        expect_city = self.obj.find_by_title("Bishkek")
        self.obj.delete_by_id(expect_city.id)
        self.obj_country.delete_all()
        self.assertRaises(IndexError, self.obj.find_by_title, "Bishkek")

    def test_select(self):
        self.obj_country.create(Country(0, "Kyrgyzstan"))
        kyrgyzstan = self.obj_country.find_by_title("Kyrgyzstan")
        self.obj_country.create(Country(0, "Poland"))
        poland = self.obj_country.find_by_title("Poland")
        self.obj.create(City(0, "Bishkek", 198.0, kyrgyzstan))
        self.obj.create(City(0, "Warsaw", 1984.0, poland))
        expected_list = self.obj.find_all()
        self.assertEqual(2, len(expected_list))
        self.obj.delete_all()
        self.obj_country.delete_all()


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        dbname = "db/test.db"
        self.obj = EmployeeService(dbname)
        self.obj_city = CityService(dbname)
        self.obj_country = CountryService(dbname)
        self.obj.delete_all()
        self.obj_city.delete_all()
        self.obj_country.delete_all()

    def test_insert(self):
        self.obj_country.create(Country(0, "Kyrgyzstan"))
        country = self.obj_country.find_by_title("Kyrgyzstan")
        self.obj_city.create(City(0, "Bishkek", 198.0, country))
        city = self.obj_city.find_by_title("Bishkek")
        actual_employee = Employee(0, "Ivan", "Ivanov", city)
        self.obj.create(actual_employee)
        expect_employee = self.obj.find_by_last_name("Ivanov")

        self.assertEqual(actual_employee.first_name, expect_employee.first_name)
        self.obj.delete_all()
        self.obj_city.delete_all()
        self.obj_country.delete_all()

    def test_delete(self):
        self.obj_country.create(Country(0, "Kyrgyzstan"))
        country = self.obj_country.find_by_title("Kyrgyzstan")
        self.obj_city.create(City(0, "Bishkek", 198.0, country))
        city = self.obj_city.find_by_title("Bishkek")
        actual_employee = Employee(0, "Ivan", "Ivanov", city)
        self.obj.create(actual_employee)
        expect_employee = self.obj.find_by_last_name("Ivanov")
        self.obj.delete_by_id(expect_employee.id)

        self.assertRaises(IndexError, self.obj.find_by_last_name, "Ivanov")
        self.obj_city.delete_all()
        self.obj_country.delete_all()

    def test_select(self):
        self.obj_country.create(Country(0, "Kyrgyzstan"))
        kyrgyzstan = self.obj_country.find_by_title("Kyrgyzstan")
        self.obj_city.create(City(0, "Bishkek", 198.0, kyrgyzstan))
        bishkek = self.obj_city.find_by_title("Bishkek")
        self.obj.create(Employee(0, "Ivan", "Ivanov", bishkek))

        self.obj_country.create(Country(0, "Poland"))
        poland = self.obj_country.find_by_title("Poland")
        self.obj_city.create(City(0, "Warsaw", 1984.0, poland))
        warsaw = self.obj_city.find_by_title("Bishkek")
        self.obj.create(Employee(0, "Ivan", "Ivanov", warsaw))

        expected_list = self.obj.find_all()
        self.assertEqual(2, len(expected_list))
        self.obj.delete_all()
        self.obj_city.delete_all()
        self.obj_country.delete_all()


if __name__ == '__main__':
    unittest.main()
