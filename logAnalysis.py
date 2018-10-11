#!/usr/bin/env python

import psycopg2


DBNAME = "news"


# problem #1 - fetch and return 3 most popular articles
def fetchTopArticles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = '''
        SELECT A.title, COUNT(*) AS numView
        FROM articles AS A
        INNER JOIN log as L ON L.path ILIKE '%' || A.slug
        GROUP BY A.title
        ORDER BY numView DESC
        LIMIT 3
    '''
    c.execute(query)
    db.commit()
    return c.fetchall()
    db.close()


# problem #1 - print the top 3 articles in a formatted manner
def printTopArticles():
    articles = fetchTopArticles()
    print("Top 3 Articles by number of views: ")
    for article in articles:
        print(article[0] + " -- " + str(article[1]) + " views")


# problem #2 - fetch and return 3 most popular authors of all time
def fetchTopAuthors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = '''
        SELECT authors.name, COUNT(*) AS numView
        FROM articles
        INNER JOIN log ON log.path ILIKE '%' || articles.slug
        INNER JOIN authors ON authors.id = articles.author
        GROUP BY authors.name
        ORDER BY numView DESC
        LIMIT 3
    '''
    c.execute(query)
    db.commit()
    return c.fetchall()
    db.close()


# problem #2 - print the top 3 authors in a formatted manner
def printTopAuthors():
    authors = fetchTopAuthors()
    print("Top 3 Authors by number of views: ")
    for author in authors:
        print(author[0] + " -- " + str(author[1]) + " views")


# problem #3 - returns the days on which more than 1% of requests led to errors
def fetchDays():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = '''
        SELECT date_trunc('day', time) AS day,
        (CAST((COUNT(errors.status)) AS decimal) / CAST((COUNT(log.status))
        AS decimal) * 100) AS errorrate
        FROM log
        LEFT OUTER JOIN (SELECT id, status FROM log
        WHERE (left(status, 1) = '4' OR left(status, 1) = '5'))
        AS errors ON log.id = errors.id
        GROUP BY day
        HAVING (CAST((COUNT(errors.status))
        AS decimal) / CAST((COUNT(log.status)) AS decimal) * 100) > 1.0
    '''
    c.execute(query)
    db.commit()
    return c.fetchall()
    db.close()


# problem #3 - print the on which more than 1% of requests led to errors
def printDays():
    days = fetchDays()
    print("Days with an error rate above one percent: ")
    for day in days:
        print(str(day[0])[:10] + " -- " + str(round(day[1], 2)) + "% errors")


# print answers to three problems above
def main():
    printTopArticles()
    print("")
    printTopAuthors()
    print("")
    printDays()


# run main
main()
