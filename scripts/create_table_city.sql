create table if not exists city(
    id integer primary key autoincrement,
    title varchar(200) unique not null,
    area float default 0,
    country_id integer
)