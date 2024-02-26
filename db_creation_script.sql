CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    password varchar(255)
);

one-to-many
foreign_key

--CREATE TABLE Orders (id, user_id, name, price, date);

CREATE Table Orders(
    id SERIAL PRIMARY KEY,
    user_id int NOT NULL,
    item varchar(255),
    price int,
    date varchar(255),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);