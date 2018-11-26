#! /usr/bin/env
import psycopg2
import time

def retorna_query(query):
    con = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    con.close()

artigos_mais_populares = """
    SELECT title as artigo, count(*) AS acessos
    FROM log, articles
    WHERE replace(log.path, '/article/', '') = articles.slug
    AND log.status LIKE '200%'
    GROUP BY title, path
    ORDER BY acessos desc limit 3;"""
autores_mais_populares = """
    SELECT name as autor, title as artigo, count(*) AS acessos
    FROM log, articles, authors
    WHERE articles.author = authors.id
      AND replace(log.path, '/article/', '') = articles.slug
      AND log.status LIKE '200%'
    GROUP BY title, path, autor
    ORDER BY acessos desc limit 3;"""
dias_com_erros_altos = """
    CREATE VIEW dias_acima_de_um_porcento as
    SELECT erros.dia, erros.erros
    FROM erros, threshold
    WHERE erros.dia = threshold.dia
    AND erros.erros > threshold.um_porcento_do_dia
    ORDER BY erros.dia desc;
"""

retorna_query(dias_com_erros_altos);
