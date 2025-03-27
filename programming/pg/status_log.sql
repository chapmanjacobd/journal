CREATE TABLE vet.adoption_approval_status(
    value text not null primary key
);

INSERT INTO vet.adoption_approval_status(value)
VALUES ('submitted'), ('in_review'), ('rejected'), ('approved');

CREATE TABLE vet.adoption_approval(
    id uuid not null default gen_random_uuid() primary key,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now(),
    person_id uuid not null references vet.person(id)
                on update restrict
                on delete restrict,
    status text not null references vet.adoption_approval_status(value)
                on update restrict
                on delete restrict,
    valid_at timestamptz not null
);

CREATE INDEX ON vet.adoption_approval(person_id, valid_at DESC);
