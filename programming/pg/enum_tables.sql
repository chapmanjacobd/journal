CREATE TABLE vet.pet_kind(
    value text not null primary key,
    comment text not null default ''
);

INSERT INTO vet.pet_kind(value, comment)
VALUES 
    ('dog', 'A Canine'),
    ('cat', 'A Feline'),
    ('bird', 'A 50 Year Commitment');

CREATE TABLE vet.pet(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    owner_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    kind text not null references vet.pet_kind(value)
                on update restrict
                on delete restrict
);
