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


INSERT INTO universidade (ANO_CONCESSAO_BOLSA, CODIGO_EMEC_IES_BOLSA, NOME_IES_BOLSA, TIPO_BOLSA, MODALIDADE_ENSINO_BOLSA, id_aluno, id_curso)
SELECT ANO_CONCESSAO_BOLSA, CODIGO_EMEC_IES_BOLSA, NOME_IES_BOLSA, TIPO_BOLSA, MODALIDADE_ENSINO_BOLSA, id, id
FROM prouni;

