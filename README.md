# Output da terceira questão
`CREATE VIEW dias_acima_de_um_porcento as  
SELECT erros.dia, erros.erros  
FROM erros, threshold  
WHERE erros.dia = threshold.dia  
 AND erros.erros > threshold.um_porcento_do_dia  
ORDER BY erros.dia desc;`  

# erros
``` CREATE VIEW erros AS  
 SELECT date(time) as dia, count(*) as erros  
 FROM log  
 WHERE status NOT LIKE '200%'  
 GROUP BY dia  
 ORDER BY erros desc;```  

# total
` CREATE VIEW total AS  
 SELECT date(time) as dia, count(*) as total  
 FROM log  
 GROUP BY dia  
 ORDER BY total desc;`  

# % por dia
` CREATE VIEW threshold AS  
SELECT total.dia as dia, (total.total / 100) as um_porcento_do_dia  
FROM total  
ORDER BY um_porcento_do_dia desc;`  
