-- Active: 1788283805588@@127.0.0.1@5432@catalogo_filmes
CREATE TABLE IF NOT EXISTS "usuarios" (
	"id" SERIAL NOT NULL,
	"nome" VARCHAR(150) NOT NULL,
	"email" VARCHAR(150) NOT NULL UNIQUE,
	"senha" VARCHAR(50) NOT NULL,
	"criado_em" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"atualizado_em" TIMESTAMP,
	PRIMARY KEY("id")
);

CREATE TABLE IF NOT EXISTS "filmes" (
	"id" SERIAL NOT NULL,
	"usuario_id" INTEGER NOT NULL,
	"titulo" VARCHAR(200) NOT NULL,
	"ano_lancamento" DATE NOT NULL,
	"genero" VARCHAR(100) NOT NULL,
	"nota" DECIMAL,
	"capa_url" TEXT,
	"criado_em" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"atualizado_em" TIMESTAMP,
	PRIMARY KEY("id")
);

ALTER TABLE "usuarios"
DROP CONSTRAINT usuarios_pkey;

ALTER TABLE "usuarios"
ADD PRIMARY KEY ("id");