create table if not exists country(
    id integer primary key autoincrement,
    title varchar(200) unique not null
)