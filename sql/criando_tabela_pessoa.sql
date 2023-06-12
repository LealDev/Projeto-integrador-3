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
