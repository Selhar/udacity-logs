# 1. Quais são os três artigos mais populares de todos os tempos?
# SELECT title as artigo, count(*) AS acessos
# FROM log, articles
# WHERE replace(log.path, '/article/', '') = articles.slug
#   AND log.status LIKE '200%'
# GROUP BY title, path
# ORDER BY acessos desc limit 3;

# 2. Quem são os autores de artigos mais populares de todos os tempos?
# SELECT name as autor, title as artigo, count(*) AS acessos
# FROM log, articles, authors
# WHERE articles.author = authors.id
#   AND replace(log.path, '/article/', '') = articles.slug
#   AND log.status LIKE '200%'
# GROUP BY title, path, autor
# ORDER BY acessos desc limit 3;

# 3. Em quais dias mais de 1% das requisições resultaram em erros?

erros
# SELECT date(time) as dia, count(*) as erros
# FROM log
# WHERE status NOT LIKE '200%'
# GROUP BY dia
# ORDER BY erros desc;

total
# SELECT date(time) as dia, count(*) as total
# FROM log
# GROUP BY dia
# ORDER BY erros desc;

%
# SELECT erros, total, dia
# FROM total
# GROUP BY dia
# ORDER BY erros desc;
