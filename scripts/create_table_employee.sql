create table if not exists employee(
    id integer primary key autoincrement,
    first_name varchar(200) not null,
    last_name varchar(200) not null,
    city_id integer
)