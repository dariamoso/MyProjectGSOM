!pip install ipython-sql
%load_ext sql
!env | grep POST
import os
USER = os.environ['POSTGRESQL_USER']
PASSWORD = os.environ['POSTGRESQL_PASSWORD']
POSTGRESQL_HOST = '10.129.0.25'
DBASE_NAME = 'demo'
CONNECT_DATA = 'postgresql://{}:{}@{}/{}'.format(
    USER,
    PASSWORD,
    POSTGRESQL_HOST,
    DBASE_NAME
)



%%sql $CONNECT_DATA
SELECT ticket_no as ticket, COUNT(flight_id) c
FROM Ticket_flights
GROUP BY ticket_no
HAVING COUNT(flight_id)>3
LIMIT 1000


%%sql $CONNECT_DATA
SELECT COUNT(*)
FROM (
    SELECT ticket_no
    FROM Ticket_flights
    GROUP BY ticket_no
    HAVING COUNT(flight_id)=5) as flights_greater_5

import psycopg2
with psycopg2.connect(
    dbname='jovyan'
) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT datname FROM pg_database')
        records = cur.fetchall()
        
print(records)

%%sql postgresql:///jovyan
CREATE TABLE Employees (
    EMPLOYEE_ID smallint NOT NULL,
    FIRST_NAME text NOT NULL,
    LAST_NAME text NOT NULL,
    HIRE_DATE date NOT NULL,
    JOB_ID text NOT NULL,
    MANAGER_ID smallint NOT NULL,
    DEPARTMENT_ID smallint NOT NULL
);

%%sql postgresql:///jovyan
CREATE TABLE Departments (
    DEPARTMENT_ID smallint NOT NULL,
    DEPARTMENT_NAME text NOT NULL,
    MANAGER_ID smallint NOT NULL
);

%%sql postgresql:///jovyan
INSERT INTO Employees VALUES(100, 'Steven', 'King', '1987-06-17', 'AD-PRES', 0, 90);
INSERT INTO Employees VALUES(101, 'Neena','Kochhar','1987-06-18','AD_VP',100,90);
INSERT INTO Employees VALUES(102, 'Lex','DeHaan','1987-06-19','AD_VP',100,90);
INSERT INTO Employees VALUES(103,'Alexander','Hunold', '1987-06-20','IT_PROG',102,60);
INSERT INTO Employees VALUES(107,'Diana','Lorentz','1987-06-24','IT_PROG',103,60);
INSERT INTO Employees VALUES(108,'Nancy','Greenberg','1987-06-25','FI_MGR',101,100);
INSERT INTO Employees VALUES(109,'Daniel','Faviet','1987-06-26','FI_ACCOUNT',108,100);
INSERT INTO Employees VALUES(114,'Den','Raphaely','1987-07-01','PU_MAN',100,30);
INSERT INTO Employees VALUES(118, 'Guy','Himuro','1987-07-05','PU_CLERK',114,30);
INSERT INTO Employees VALUES(144,'Peter','Vargas','1987-07-31','ST_CLERK',114,50);
INSERT INTO Employees VALUES(145,'John','Russell','1987-08-01','SA_MAN',100,80);
INSERT INTO Employees VALUES(146,'Karen','Partners','1987-08-02','SA_MAN', 100,80)

%%sql postgresql:///jovyan
INSERT INTO Departments VALUES(10,'Administration', 200);
INSERT INTO Departments VALUES(130,'Purchasing',114);
INSERT INTO Departments VALUES(40,'HumanResources',203);
INSERT INTO Departments VALUES(50,'Shipping',121);
INSERT INTO Departments VALUES(60,'IT',103);
INSERT INTO Departments VALUES(70,'PublicRelations',204);
INSERT INTO Departments VALUES(80,'Sales',145);
INSERT INTO Departments VALUES(90,'Executive',100);
INSERT INTO Departments VALUES(100,'Finance',108);
INSERT INTO Departments VALUES(110,'Accounting',205)

%%sql postgresql:///jovyan
SELECT * FROM Employees

%%sql postgresql:///jovyan
SELECT * FROM Departments


%%sql postgresql:///jovyan
SELECT department_name, first_name, last_name
FROM Departments d
JOIN Employees e USING(department_id)
ORDER BY e.hire_date
LIMIT 1