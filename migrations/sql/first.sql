BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> c056ef9b223e

CREATE TABLE auth."user" (
    id SERIAL NOT NULL, 
    key VARCHAR(8) NOT NULL, 
    email VARCHAR(100) NOT NULL, 
    password VARCHAR(200) NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
    updated_at TIMESTAMP WITHOUT TIME ZONE, 
    PRIMARY KEY (id), 
    UNIQUE (email)
);

CREATE UNIQUE INDEX ix_auth_user_key ON auth."user" (key);

INSERT INTO alembic_version (version_num) VALUES ('c056ef9b223e');

COMMIT;

