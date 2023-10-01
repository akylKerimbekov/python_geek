class Country:
    def __init__(self, id: int, title: str):
        self.__id = id
        self.__title = title

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, value: int):
        self.__id = value

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    def __str__(self):
        return f"Country id: {self.__id}, title: {self.__title}"

    def __eq__(self, other):
        return self.__id == other.id and self.__title == other.title

    def __ne__(self, other):
        return self.__id != other.id and self.__title != other.title


class City:
    def __init__(self, id, title, area, country):
        self.__id = id
        self.__title = title
        self.__area = area
        self.__country = country

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    def __str__(self):
        return f"City id: {self.__id}, title: {self.__title}"


class Employee:
    def __init__(self, id, first_name, last_name, city):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__city = city

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    def __str__(self):
        return (f"Employee: "
                f"first name - {self.__first_name}, last name - {self.__last_name}, "
                f"from country: {self.__city.country.title}, "
                f"from city {self.__city.title} with area: {self.__city.area}")
