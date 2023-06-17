CREATE TABLE prouni (
	id SERIAL primary key,
  	ANO_CONCESSAO_BOLSA INT,
  	CODIGO_EMEC_IES_BOLSA INT,
  	NOME_IES_BOLSA VARCHAR(255),
  	TIPO_BOLSA VARCHAR(255),
  	MODALIDADE_ENSINO_BOLSA VARCHAR(255),
  	NOME_CURSO_BOLSA VARCHAR(255),
  	NOME_TURNO_CURSO_BOLSA VARCHAR(255),
  	CPF_BENEFICIARIO_BOLSA VARCHAR(255),
  	SEXO_BENEFICIARIO_BOLSA CHAR(1),
  	RACA_BENEFICIARIO_BOLSA VARCHAR(255),
  	DT_NASCIMENTO_BENEFICIARIO DATE,
  	BENEFICIARIO_DEFICIENTE_FISICO VARCHAR(3),
  	REGIAO_BENEFICIARIO_BOLSA VARCHAR(255),
  	SIGLA_UF_BENEFICIARIO_BOLSA CHAR(2),
  	MUNICIPIO_BENEFICIARIO_BOLSA VARCHAR(255),
  	idade FLOAT
);

COPY prouni (
  	ANO_CONCESSAO_BOLSA,
	CODIGO_EMEC_IES_BOLSA,
  	NOME_IES_BOLSA,
  	TIPO_BOLSA,
  	MODALIDADE_ENSINO_BOLSA,
  	NOME_CURSO_BOLSA,
  	NOME_TURNO_CURSO_BOLSA,
  	CPF_BENEFICIARIO_BOLSA,
  	SEXO_BENEFICIARIO_BOLSA,
  	RACA_BENEFICIARIO_BOLSA,
  	DT_NASCIMENTO_BENEFICIARIO,
  	BENEFICIARIO_DEFICIENTE_FISICO,
  	REGIAO_BENEFICIARIO_BOLSA,
  	SIGLA_UF_BENEFICIARIO_BOLSA,
  	MUNICIPIO_BENEFICIARIO_BOLSA,
  	idade
) 
FROM '/var/lib/postgresql/dados/prouni_2005_2019.csv' DELIMITER ',' CSV HEADER;

CREATE TABLE pessoa (
	id SERIAL primary key,
  	CPF_BENEFICIARIO_BOLSA VARCHAR(255),
  	SEXO_BENEFICIARIO_BOLSA CHAR(1),
  	RACA_BENEFICIARIO_BOLSA VARCHAR(255),
  	DT_NASCIMENTO_BENEFICIARIO DATE,
  	BENEFICIARIO_DEFICIENTE_FISICO VARCHAR(3),
  	REGIAO_BENEFICIARIO_BOLSA VARCHAR(255),
  	SIGLA_UF_BENEFICIARIO_BOLSA CHAR(2),
  	MUNICIPIO_BENEFICIARIO_BOLSA VARCHAR(255),
  	idade FLOAT
);

INSERT INTO pessoa (
  	CPF_BENEFICIARIO_BOLSA,
  	SEXO_BENEFICIARIO_BOLSA,
  	RACA_BENEFICIARIO_BOLSA,
  	DT_NASCIMENTO_BENEFICIARIO,
  	BENEFICIARIO_DEFICIENTE_FISICO,
  	REGIAO_BENEFICIARIO_BOLSA,
  	SIGLA_UF_BENEFICIARIO_BOLSA,
  	MUNICIPIO_BENEFICIARIO_BOLSA,
  	idade)
SELECT CPF_BENEFICIARIO_BOLSA,
  	SEXO_BENEFICIARIO_BOLSA,
  	RACA_BENEFICIARIO_BOLSA,
  	DT_NASCIMENTO_BENEFICIARIO,
  	BENEFICIARIO_DEFICIENTE_FISICO,
  	REGIAO_BENEFICIARIO_BOLSA,
  	SIGLA_UF_BENEFICIARIO_BOLSA,
  	MUNICIPIO_BENEFICIARIO_BOLSA,
  	idade
FROM prouni;

CREATE TABLE curso(
  	id SERIAL primary key,
	id_aluno INT,
  	NOME_CURSO_BOLSA VARCHAR(255),
  	NOME_TURNO_CURSO_BOLSA VARCHAR(255),
    FOREIGN KEY (id_aluno) REFERENCES pessoa (id)
);

INSERT INTO curso (NOME_CURSO_BOLSA, NOME_TURNO_CURSO_BOLSA, id_aluno)
SELECT NOME_CURSO_BOLSA, NOME_TURNO_CURSO_BOLSA, id
FROM prouni;

CREATE TABLE universidade (
    id SERIAL PRIMARY KEY,
  	ANO_CONCESSAO_BOLSA INT,
  	CODIGO_EMEC_IES_BOLSA INT,
  	NOME_IES_BOLSA VARCHAR(255),
  	TIPO_BOLSA VARCHAR(255),
  	MODALIDADE_ENSINO_BOLSA VARCHAR(255),
    id_aluno INTEGER,
	id_curso INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES pessoa (id),
	FOREIGN KEY (id_curso) REFERENCES curso (id)
);


INSERT INTO universidade (
	ANO_CONCESSAO_BOLSA, 
	CODIGO_EMEC_IES_BOLSA, 
	NOME_IES_BOLSA, 
	TIPO_BOLSA, 
	MODALIDADE_ENSINO_BOLSA, 
	id_aluno, 
	id_curso)
SELECT 
	ANO_CONCESSAO_BOLSA, 
	CODIGO_EMEC_IES_BOLSA, 
	NOME_IES_BOLSA, 
	TIPO_BOLSA, 
	MODALIDADE_ENSINO_BOLSA, 
	id, 
	id
FROM prouni;

DROP TABLE prouni;

CREATE INDEX index_pessoa ON pessoa(id);

CREATE INDEX index_curso ON curso(id);

CREATE INDEX index_universidade ON universidade(id);