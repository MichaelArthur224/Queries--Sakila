#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import pymysql
pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine


# In[2]:


from sqlalchemy import create_engine


# # Engine

# In[13]:


username = "root"
password = "root" 
db_name = "sakila"
connection = f"mysql+pymysql://{username}:{password}@localhost/{db_name}"


# In[14]:


engine = create_engine(connection)
engine


# 1. What query would you run to get all the customers inside city_id = 312? Your query should return the customers' first name, last name, email, address, and city.

# In[15]:


q = """SELECT customer.first_name, customer.last_name, customer.email, address.address, address.address2, city.city
FROM city
JOIN address ON city.city_id = address.city_id
JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;"""
pd.read_sql(q, engine)


# What query would you run to get all comedy films? Note that the genre is called the category in this schema. Your query should return film title, description, release year, rating, and special features.

# In[16]:


q2 = """SELECT title, release_year, rating, description
FROM category
JOIN film
WHERE name = 'Comedy';"""
pd.read_sql(q2, engine)


# 3. What query would you run to get all the films that Johnny Lollobrigida was in? Your query should return the actor's last name, film title, and release year.

# In[26]:


q3 = """SELECT actor.first_name, actor.last_name, film.title, film.release_year
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE
actor.first_name = 'Johnny' AND actor.last_name = 'Lollobrigida';
"""
pd.read_sql(q3, engine)


# What query would you run to get the first and last names of all the actors in the movie titled "Bingo Talented"?

# In[35]:


q4 = """SELECT actor.first_name, actor.last_name
FROM actor
JOIN film_actor on actor.actor_id = film_actor.actor_id
WHERE film_actor.film_id = (SELECT film_id
FROM film
WHERE film.title = 'Bingo Talented')
;"""
pd.read_sql(q4, engine)


# 5. What query would you run to get the customer_id associated with all payments greater than twice the average payment amount? (HINT: use 2* in your query to get twice the amount). Your result should include the customer id and the amount.

# In[36]:


q5 = """SELECT customer_id, amount
FROM payment
HAVING amount > 2* 4.200667;"""
pd.read_sql(q5, engine)


# What query would you run to list the first and last names of the 5 customers who have the highest number(count) of payments? You can title the number of payments as num_payments.

# In[37]:


q6 = """SELECT SUM(payment_id), c.customer_id
FROM payment as p
LEFT JOIN customer as c ON p.customer_id = c.customer_id
GROUP BY payment_id
LIMIT 5;"""
pd.read_sql(q6, engine)


# In[ ]:




