import unittest

from repository import ProductRepository


def populate(repository: ProductRepository):
    with open("scripts/populate.csv", mode="r") as file:
        for line in file:
            row = line.strip().split(";")
            repository.upsert(*row)


class RepositoryTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = ProductRepository()

    def test_insert(self):
        args = ("test fruit", 100.0, 100)

        self.obj.insert(*args)

        result = self.obj.find_by_product_title("test fruit")
        self.assertEqual(result[0][1], "test fruit")
        self.assertEqual(result[0][2], 100.0)
        self.assertEqual(result[0][3], 100)

        self.obj.delete_by_name("test fruit")

    def test_update(self):
        args = ("test fruit", 100.0, 100)
        self.obj.insert(*args)
        result = self.obj.find_by_product_title("test fruit")
        args = ("test fruit", 100.0, 200, result[0][0])
        self.obj.update(*args)

        result = self.obj.find_by_product_title("test fruit")
        self.assertEqual(result[0][1], "test fruit")
        self.assertEqual(result[0][2], 100.0)
        self.assertEqual(result[0][3], 200)

        self.obj.delete_by_name("test fruit")

    def test_upsert(self):
        args = ("test fruit", 100.0, 100)
        self.obj.insert(*args)
        args = ("test fruit", 100.0, 200)
        self.obj.upsert(*args)

        result = self.obj.find_by_product_title("test fruit")
        self.assertEqual(result[0][1], "test fruit")
        self.assertEqual(result[0][2], 100.0)
        self.assertEqual(result[0][3], 200)

        self.obj.delete_by_name("test fruit")

    def test_delete(self):
        args = ("test fruit", 100.0, 100)
        self.obj.insert(*args)
        result = self.obj.find_by_product_title("test fruit")
        self.obj.delete(result[0][0])

        result = self.obj.find_by_product_title("test fruit")

        self.assertEqual(len(result), 0)
        self.obj.delete_by_name("test fruit")

    def test_select_by_title(self):
        args = ("test fruit", 100.0, 100)
        self.obj.insert(*args)

        result = self.obj.find_by_product_title("test fruit")

        self.assertEqual(len(result), 1)
        self.obj.delete_by_name("test fruit")


if __name__ == '__main__':
    unittest.main()
