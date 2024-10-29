#Rod
def rod(prices, n):
    maximum = {}

    def add(length):
        if length == 0:
            return 0, []

        if length in maximum:
            return maximum[length]

        max_val = -1
        best_cut = []

        for i in range(1, length + 1):
            if i <= len(prices):
                val, cuts = add(length - i)
                val += prices[i - 1]  

                if val > max_val:
                    max_val = val
                    best_cut = [i] + cuts

        maximum[length] = (max_val, best_cut)
        return maximum[length]
    return add(n)

prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

max_val, optimal_cuts = rod(prices, n)
rod(prices,n)

#SQL

#1

conn = psycopg2.connect(
    dbname='demo', 
    user=os.environ['POSTGRESQL_USER'],
    password=os.environ['POSTGRESQL_PASSWORD'], 
    host=POSTGRESQL_HOST
)
cur = conn.cursor()

query = 'SELECT airport_code, airport_name, city FROM bookings.airports LIMIT 5'
cur.execute(query)
records = cur.fetchall()
cur.close()
conn.close()

records

#2

%%sql postgresql:///jovyan
    SELECT * FROM pg_database
%sql SELECT airport_code, airport_name, city FROM bookings.airports LIMIT 5

#3

%sql SELECT passenger_name FROM tickets WHERE ticket_no = '0005432312164'