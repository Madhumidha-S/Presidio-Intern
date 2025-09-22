# SQL & DBMS Notes

---

# 1. CRUD Operations

- **Create (INSERT)** - Add new records  
- **Read (SELECT)** - Retrieve records  
- **Update (UPDATE)** - Modify existing records  
- **Delete (DELETE)** - Remove records  

**Examples:**
```
CREATE TABLE name(value datatype, ....);
Select * from tableName where something = value;

UPDATE tableName SET col1 = value, ..., WHERE condition;
INSERT INTO Students (id, name, age) VALUES (1, 'Alice', 20);

ALTER TABLE tableName
ADD col datatype;

DELETE FROM tableName WHERE condition;
```

# 2. SQL Queries

- **SELECT** - Retrieve data
- **WHERE** - Filter rows
- **GROUP BY** - Aggregate grouping
- **HAVING** - Filter aggregated results
- **ORDER BY** - Sort results

**Examples**
```
SELECT name, salary FROM Employees WHERE salary > 50000;
SELECT dept, AVG(salary)
FROM Employees
GROUP BY dept
HAVING AVG(salary) > 60000;
SELECT name FROM Employees ORDER BY salary DESC;
```

# 3. SQL Joins

- **INNER JOIN** - Only matching rows
- **LEFT JOIN** - All rows from left table + matches from right
- **RIGHT JOIN** - All rows from right table + matches from left
- **FULL JOIN** - All rows from both tables
- **CROSS JOIN** - Cartesian product
- **SELF JOIN** - Within same table
- **NATURAL JOIN** - Matches columns with the same name in both tables

```
-- INNER JOIN SYNTAX
CREATE TABLE table2(
	...
	PRIMARY KEY(column),
	FOREIGN KEY(column) REFERENCES table1(columnName)
);

SELECT table2.column, table1.columnName
FROM table2
INNER JOIN table1 ON table2.column = table1.columnName
```

**Some Examples**

```
-- LEFT JOIN
SELECT e.name, d.dept_name
FROM Employees e
LEFT JOIN Departments d ON e.dept_id = d.id;

-- CROSS JOIN
SELECT e.name, d.dept_name
FROM Employees e
CROSS JOIN Departments d;
```

# 4. SQL Constraints

- **PRIMARY** KEY - Unique + Not Null
- **FOREIGN** KEY - References another table
- **UNIQUE** - No duplicates
- **NOT NULL** - Must have a value
- **CHECK** - Enforce condition
- **DEFAULT** - Assign default value

**Examples**
```
CREATE TABLE Students (
  id INT PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  age INT CHECK (age >= 18),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES Departments(id)
);
```

# 5. SQL Subqueries

- Query inside another query
- Can be used in **SELECT**, **FROM**, or **WHERE** clauses

**Examples**
```
SELECT name
FROM Employees
WHERE salary > (SELECT AVG(salary) FROM Employees);
SELECT dept_id, 
       (SELECT COUNT(*) FROM Employees e WHERE e.dept_id = d.id)
FROM Departments d;
```

# 6. DBMS ER Model

- Entity - Real-world object (Student, Course)
- Attributes - Properties (name, age, etc.)
- Relationship - Association between entities

**Types of Relationships:**

- One-to-One
- One-to-Many
- Many-to-One
- Many-to-Many

**Example:**

- Student (id, name)
- Course (id, title)
- Relationship: EnrolledIn (Student <-> Course)

# 7. DB Normalization

- 1NF - Atomic values, no repeating groups
- 2NF - 1NF + No partial dependency
- 3NF - 2NF + No transitive dependency
- BCNF - Stronger form of 3NF
- 4NF - BCNF + No multivalued dependencies. 
- 5NF - 4NF + No Join Dependancies

# 8. Database Indexing

- Acts like a **book index** for a database  
- Helps locate data **quickly** 
- Avoids full table scans, improving **query performance**
- Speeds up **data retrieval**  
- Reduces **query time complexity**, especially on large tables  
- Efficient for **WHERE**, **JOIN**, and **ORDER BY** queries

**Types of Indexes**

- Clustered Index (Primary Key) - Determines **physical order** of data in the table (only 1 per table), data stored in leaf nodes of the index

- Non-Clustered Index (Secondary Index) - Does **not change physical order** of table data (**multiple non-clustered indexes**), Stored in a **separate structure** with pointers to actual data

**Examples**

```
-- Create a clustered index on primary key
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary DECIMAL(10,2)
);

-- Create a non-clustered index
CREATE INDEX idx_salary ON Employees(salary);
```
# 9. Database Transactions

- A **transaction** is a sequence of one or more SQL operations executed as a single unit of work
- Either all operations succeed or none are applied, ensures data consistency and integrity

**Examples:**

```
-- Start a transaction
BEGIN TRANSACTION;

-- Operations
UPDATE Accounts SET balance = balance - 100 WHERE id = 1;
UPDATE Accounts SET balance = balance + 100 WHERE id = 2;

-- Save changes
COMMIT;

-- Or undo changes if something goes wrong
ROLLBACK;
```

**ACID Properties**

- **Atomicity** - All operations in a transaction succeed or none do  
- **Consistency** - Database moves from one valid state to another  
- **Isolation** - Concurrent transactions do not interfere  
- **Durability** - Changes are permanent once committed 

# 10. Aggregate Functions

**Purpose:** Perform calculations on a set of values and return a single value  

**Commands:**
- COUNT(column) - Number of rows  
- SUM(column) - Total sum  
- AVG(column) - Average value  
- MIN(column) - Minimum value  
- MAX(column) - Maximum value  

**Example:**
```
SELECT COUNT(id), AVG(salary), MAX(salary)
FROM Employees
WHERE dept_id = 1;
```

# 11. String Functions

- UPPER(string)
- LOWER(string)
- LENGTH(string)
- CONCAT(str1, str2, …)
- SUBSTRING(string, start, length)
- TRIM(string) 
- REPLACE(string, old, new)
- LEFT(string, n)
- RIGHT(string, n) 


