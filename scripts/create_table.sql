create table if not exists product(
    id integer primary key autoincrement,
    product_title varchar(200) unique not null,
    price float(10, 2) not null default 0.0,
    quantity integer not null default 0
)