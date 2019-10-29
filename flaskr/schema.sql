DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;

create table user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username NEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

create table POST(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    FOREIGN KEY
(author_id) REFERENCES
use
(id)
);