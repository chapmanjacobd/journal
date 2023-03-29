CREATE EXTENSION btree_gist;
CREATE TABLE rooms (
    room int,
    period tstzrange,
    EXCLUDE USING gist (room WITH =, period WITH &&)
);
