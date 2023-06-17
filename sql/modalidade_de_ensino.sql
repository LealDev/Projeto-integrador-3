SELECT
    MODALIDADE_ENSINO_BOLSA,
    COUNT(*) AS total_linhas
FROM
    public.universidade
GROUP BY 1;