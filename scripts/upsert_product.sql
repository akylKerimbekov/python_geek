insert into product(product_title, price, quantity)
values (?, ?, ?)
on conflict(product_title)
do update set price = excluded.price, quantity=excluded.quantity