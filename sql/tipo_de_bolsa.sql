SELECT
    TIPO_BOLSA,
    COUNT(*)
FROM
    public.universidade
GROUP BY 1;