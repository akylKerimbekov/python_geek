from repository import ProductRepository


def populate(repository: ProductRepository):
    with open("scripts/populate.csv", mode="r") as file:
        for line in file:
            row = line.strip().split(";")
            repository.upsert(*row)


def print_result(rows: list):
    print()
    for row in rows:
        print(f"id: {row[0]}; name of product: {row[1]}; price: {row[2]}; quantity: {row[3]}")


repo = ProductRepository()
populate(repo)
result = repo.find_all()
print_result(result)
result = repo.find_by_product_title("apple")
print_result(result)
repo.delete(1)
result = repo.find_all()
print_result(result)
