"""
This is where you should write your code and this is what you need to upload to Gradescope for autograding.

You must NOT change the function definitions (names, arguments).

You can run the functions you define in this file by using test.py (python test.py)
Please do not add any additional code underneath these functions.
"""

import sqlite3


def customer_tickets(conn, customer_id):
    """
    Return a list of tuples:
    (film_title, screen, price)

    Include only tickets purchased by the given customer_id.
    Order results by film title alphabetically.
    """
    query = """
    SELECT films.title, screenings.screen, tickets.price
    FROM tickets 
    INNER JOIN screenings ON tickets.screening_id=screenings.screening_id
    INNER JOIN films ON screenings.film_id=films.film_id
    WHERE customer_id=?
    ORDER BY films.title;"""

    cursor = conn.execute(query, (customer_id,))

    c = []

    for i in cursor:
        c.append(i)

    return c


def screening_sales(conn):
    """
    Return a list of tuples:
    (screening_id, film_title, tickets_sold)

    Include all screenings, even if tickets_sold is 0.
    Order results by tickets_sold descending.
    """
    query = """SELECT screenings.screening_id, films.title, COUNT(tickets.ticket_id)
    FROM screenings LEFT JOIN tickets 
    ON tickets.screening_id=screenings.screening_id
    INNER JOIN films
    ON screenings.film_id=films.film_id
    GROUP BY screenings.screening_id
    ORDER BY COUNT(tickets.ticket_id) desc;"""

    cursor = conn.execute(query)

    c = []

    for i in cursor:
        c.append(i)

    return c


def top_customers_by_spend(conn, limit):
    """
    Return a list of tuples:
    (customer_name, total_spent)

    total_spent is the sum of ticket prices per customer.
    Only include customers who have bought at least one ticket.
    Order by total_spent descending.
    Limit the number of rows returned to `limit`.
    """
    query = """SELECT customers.customer_name, SUM(tickets.price)
    FROM tickets INNER JOIN customers
    ON tickets.customer_id=customers.customer_id
    GROUP BY customers.customer_name
    ORDER BY SUM(tickets.price) desc
    LIMIT ?"""

    cursor = conn.execute(query, (limit,))

    c = []

    for i in cursor:
        c.append(i)

    return c