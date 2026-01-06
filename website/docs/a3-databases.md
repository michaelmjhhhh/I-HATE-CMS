---
sidebar_position: 2
title: A3 Databases
---

# A3 Databases

## A3.1.1 Explain the features, benefits and limitations of relational databases.

- **Features:** 

  - Store data in tables(relations/entities), where *row = record = tuple = instance, column = attribute = field = feature.*

  - Each table has primary key to uniquely identify each record.

  - Foreign keys link tables together.

  - Allows relationships between tables (one-to-one, one-to-many, many-to-many).

  - Supports SQL (Structured Query Language) to query and manage data. Allow fast access and
    manipulation.

  - ***Primary Key***: A primary key is an attribute that uniquely identifies each record in a table and
    cannot be duplicated or null. 

  - ***Foreign Key***: is an attribute in one table that refers to the primary key of another table, thereby
    creating a relationship between the two entities. 

  - ***Cardinality***: is the type of relationship between the entities.
    • one-to-one: One-single record in the first table can only be connected with one record in the
    second table, vice versa.
    • one-to-many: An instance in one entity can be related to many instances(rows) in another
    entity.
    • many-to-many: Many instances in one entity can be related to many instances in another entity.
    Single record in tableA can be connected to multiple records in tableB, single record in tableB
    can also be connected to multiple records in tableA. 

  - ***Modality***: is the necessity of relationships between tables.
    • Mandatory: An entity occurrence must be related to another entity occurrence. Use full line
    to represent in ERD(**Chen's notation**).
    • Optional: An entity occurrence may or may not be related to another entity occurrence. Use
    dotted line to represent in ERD(**Chen's notation**).

  - Advantages of RDS:

    - Store large amount of data
    - Allow fast retrieval of information 
    - Allow multi-user access securely
    - Ensure data integrity and consistency

    

- **Benefits**: 

  - Scalability: RDS is more easier to scale than flat file database. 
  - Less duplication of data (because data can be split into different tables, linked by primary key and foreign key). Reduced redundancy.
  - More accurate and consistent data (because of primary/foreign keys and constraints). Better data integrity.
  - Easier to search and update using SQL.
  - Secure — access can be controlled.
  - Works well for large amounts of structured data.
  - Normalization is supported to reduce insert anomaly, update anomaly and deletion anomaly.
  - Reliable transaction processing: Relational databases have several checks that occur when transactions take place to ensure that the transactions are reliable. 
  - Community support: There are multiple streams of support for users of relational databases. 

- **Limitations**

  - Can be difficult to design at the start. The different entities and models within the database can be complex and challenging to implement. 

  - Big data scalability: Relational database models are not the best model for storing data that will be mined to make complex decisions. 

  - Rigid schema: The schemas of the database are rigid data types, and relationships must conform to very specific rules.

  - Unstructured data handling: Unstructured data that does not follow the rigid schema of the database model can be difficult to place within the model. For example videos. 

- **Composite key and Concatenated key**(used when single attribute cannot uniquely idendify each row)

  - ***Composite key***

    - A composite key is a logical **primary key** that consists of **two or more attributes** combined together to **uniquely identify a row** in a table.  
    - E.g. Neither `student_id` nor `course_id` alone can uniquely indentify each row, but the *combination* of both uniquely identifies an enrollment record.  `(student_id, course_id)` is a **composite key**.

  - ***Concatenated key*** 

    - A concatenated key is a physical implementation of a composite key, where multiple attributes are **literally joined (concatenated)** into a single value — often as a string — to serve as a **unique identifier.** Not primary key.     

  - **The difference between these two keys:** 

    - ![截屏2025-11-04 10.59.46](./assets/%E6%88%AA%E5%B1%8F2025-11-04%2010.59.46.png)

      


## A3.2.1 Describe database schema

- ***Database schema***:  is a blueprint of the database that identifies the different entities (tables), attributes (fields) and relationships (links) within the database, including the restraints on the data. 
  - ***Conceptual schema:*** identifies all the entities within the database and the relationship between these entities. This model does not contain specific details such as the attributes within the entities nor information about the restraints on the data, but does identify the types of relationships between the data.  
  - ![截屏2025-10-25 15.08.16](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2015.08.16.png)

- ***Logical Schema***: This model of the database identifies the different attributes within each of the entities. This will include the primary keys and foreign keys which create the relationships between the entities. Primary key is bold, foreign key is represented by "*". 
  - ![截屏2025-10-25 15.10.05](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2015.10.05.png)

  - ***Physical Schema***: This model of the databases identifies the different attributes and their data types as well as the primary key and foreign key link that will create the relationships between entities. 
- ![截屏2025-10-25 15.11.44](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2015.11.44.png)

## A3.2.2 Construct ERDs

- **Entity relationship diagrams (ERDs)** show the entities (tables), attributes (fields), and relationships within a relational database. 
- ***Chen Notation Sytle*** 
- Steps to construct an ERD:  
  - Step1: Identify the level of ERD required (conceptual, logical or physical). This will determine the detail required. 
  - Step2: Identify the entities involved and, if required, the attributes and data types. 
  - Step3: Identify the relationships (using verbs) between the entities. 
  - Step4: Identify the cardinality of the relationship, one-to-one, one-to-many or many-to-many. 
  - Step5: Identify the modality of the relationships. Are they optional or mandatory?  

## A3.2.3 Outline the different data types used in relational databases

- String data types: 
  - ![截屏2025-10-25 15.20.12](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2015.20.12.png)
  - ***Char*** is a fixed length. The length is defined by **CHAR(7)**, also includes spaces. If you insert a character less than 7 characters, Mysql will use spaces to replenish. Often used for fixed length ID, password, country code or status flags. 
  - ***VARCHAR*** is a variable length. Often used for names, emails, description. 
  - ***TEXT*** is a longer text, often used for blog posts, articles, or comments&product reviews.
  - ***MEDIUMTEXT*** is for larger texts, often used for complete books, novels, long documentation, or large JSON data. 
  - ***LONGTEXT*** is the largest data type. Used for complete software codebases, and archival data. 
  - For ***ENUM***, you must choose on value from the predefined list, often used for status fields or user roles. 
  - For ***SET***, you can choose zero or multiple records from the predefined list, often used for user skills/interests or multiple tags/categories. 
- Numeric data types:
  - ***BIT*** stores bit-field values where each bit can be 0 or 1. Often used to store boolean values(True/False,Open/Shut down), or permission flags. 
  - ***BOOL*** is best used for boolean flags, toggle(开关) settings, and status indicator. (Zero means false, non-zero means true).
  - ***INT*** can only store a whole number. Best used for primary keys(foreign keys), quantities or IDs(without character).
  - REMEBER, use ***FLOAT*** directly. If you want to add contraints on the decimal places of the number, use ***DECIMAL(a,b)***. The first argument a is the length of the whole number, b is the number of decimal places. 
- Date/time data types: 
  - ![截屏2025-10-25 15.38.09](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2015.38.09.png)

## A3.2.4 Construct tables for relational databases

- ![截屏2025-10-25 16.09.41](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2016.09.41.png)

## A3.2.5 Explain the difference between normal forms

> 如果要用一句话概括Normalization的要求，那就是the data **should rely on the key and only rely on the key, cannot rely on anything else.**
>
> Databases that are not designed properly can have the following issues. 

- **Insert Anomalies** 

  -  You cannot add data correctly as the data is dependent on other attributes in the database. You can’t insert a new record into the database without also adding other data that shouldn’t be required — because the table is not properly normalized. For example, you cannot add a course that isn't chosen by any students.

- **Deletion Anomalies:**

  - The database may have attributes that rely on non-related attributes. If you delete the non-related attributes, you unintentionally lose data. Non-related attributes are stored together in one table, if you want do delete an instance of an attribute and thus delete the whole row, you will lost other data in this row.

- **Update Anomalies: **

  -  Any update in a badly designed database will be a challenge as you have to look through every section of the database to ensure all items are deleted. This is not a challenge in a small database, but for a database with hundreds thousands, or millions of records, this becomes a significant problem. If there's duplicated data, and you want to update this data, if you don't change it everywhere manually, the data will be inconsistent and you will no longer know which one is the correct version.   

- **So what is normalization?**

  - Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity & consistency. 
  - It involves breaking down large tables into smaller, related tables and defining relationships between them.

- **Functional Dependencies**

  - **Functional dependency** means that one attribute (or a group of attributes) uniquely determines another attribute.  

    > For example, If you know A, than you can find exactly one B, they we say A functionally determines B.
    > `Uniquely determine` means each value of A corresponds to exactly one value of B,
    > but a value of B may correspond to many A’s. If two rows have the same value of A, they must have the same value of B. 

- **The process of normalization**

  - unformal form:
    - Initial candidate (possible) primary key identified
    - Repeating groups identified using indentation(缩进)
      - Repeating groups are the new data that needs to be added when a new entry is created.
      - Atomic的意思是每一个cell都只有一个值，没有重复，repeated group指的是一个单元格存了多个值，或者未来可能需要存多个值(potentially possible)。这是1NF需要确保的。 
  - ![截屏2025-10-28 16.27.59](./assets/%E6%88%AA%E5%B1%8F2025-10-28%2016.27.59.png)
  - ![截屏2025-10-28 16.28.08](./assets/%E6%88%AA%E5%B1%8F2025-10-28%2016.28.08.png)
  - ![截屏2025-10-28 16.28.16](./assets/%E6%88%AA%E5%B1%8F2025-10-28%2016.28.16.png)

> Here are some key terms that you must know when normalizing:

 - **Partial Dependency**: A partial dependency occurs when a non-prime attribute(非主键属性) is functionally dependent on part of a composite primary key, not on the whole key. 例如主键：(StudentID, CourseID)（复合主键）StudentName 只依赖 StudentID，不是整个主键 → 部分依赖。这是2NF需要消除的情况。

 - **Transitive Dependency**: A transitive dependency occurs when a non-prime attribute is functionally dependent on another non-prime attribute, which in turn is dependent on the primary key. 当一个非主键属性依赖于另一个非主键属性，而这个非主键属性又依赖于主键时，这叫叫传递依赖。这是3NF要消除的情况。

 - **Non-key Dependency**: A non-key dependency occurs when a non-prime attribute depends on another non-prime attribute rather than on the primary key. 任何非主键属性依赖于另外一个非主键属性，就是非键依赖。违反3NF，因为非键属性不应该依赖于非键属性。

> Here are some terms related to this topic

- **Referential integrity**: ensures that a foreign key value in one table must either be null or match an existing primary key value in another table, so that relationships between tables remain consistent.  

- **Data redundancy**: occurs when the same piece of information is stored in **multiple places in the database**, leading to inconsistencies and unnecessary storage. 

- **The characteris of unnormalized database and each normal forms:**

  - **Unnormalized data** contains **repeating groups, multi-valued attributes, and no defined primary key**, leading to data redundancy and anomalies. Not atomic. 

  - **First Normal Form(1NF)** means all attributes are atomic and each row is uniquely identifiable by a primary key. Unique means that there are no rows that are extactly the same. **All entries** in a **column** are of the **same kind**. 

  - **Second Normal Form(2NF)**: A relation is in **Second Normal Form (2NF)** if it is in 1NF and every non-prime attribute is fully functionally dependent on the entire primary key (no partial dependency). 说人话就是，**Every non-key column must depend on the** **entire** **Primary Key.**

  - **Third Normal Form(3NF):** A relation is in **Third Normal Form (3NF)** if it is in 2NF and no non-prime attribute is transitively dependent on the primary key.  说人话就是，**No non-key column depends on another non-key column.**




- **Three types of normal forms**:

  - **First normal form**:  The repeating data is moved into a new entity. The non repeating data stays in its own entity and is given a unique identifier (primary key). The primary key from the non-repeating entity is placed in the new entity as a foreign key. In the new entity a unique identifier is found. This will most likely be a composite key. The issue with the first normal form is that the new entity will have attributes that only rely on one part of the key, known as partial key dependencies. This does not align with the normalized database philosophy of the whole key and nothing but the key.
  - **Second normal form**: The partial key dependencies are removed into their own entity and a primary key is identified. The primary key features in the entity it was removed from as both a primary key and a foreign key at this point. The issue with second normal form is that some attributes in the entities do not rely on the key, they are their own information. These are known as transitive or non-key dependencies. These, again, do not align with the normalized database philosophy of "the whole key and nothing but the key".
  - **Third normal form**:  The transitive or non-key dependencies are moved into their own entity and given a primary key. The primary key becomes a foreign key in the entity it was removed from. Transitive dependencies can be present in any of the entities previously created. Once they are removed, your entities should meet the normalized database philosophy of "the whole key and nothing but the key". 

- **How to construct from UNF to 1NF to 2NF to 3NF:**

  - - Split, to get 1NF

    - Find a composite key, two attributes that can uniquely identify each record/row. 然后说人话就是，判断哪些attribute不依赖整个composite key，只是依赖一部分，找出来，然后拆分成2个表。原本的保留，新的attribute组成新的表，表的PK就是这些attribute依赖的那个，然后同样的那个attribute作为FK留在原表中。可能会拆分成多个。

    - 然后，判断哪些是partial dependent的，列出来, 这些再次拆分成子表。A partial dependent on B，那么把B这个attribute留在原表作为FK，新的表的PK就是这个attribute。新的表的另外一个attribute就是A。

    - ![截屏2025-10-28 20.30.24](./assets/%E6%88%AA%E5%B1%8F2025-10-28%2020.30.24.png)

    - ![截屏2025-10-28 20.30.33](./assets/%E6%88%AA%E5%B1%8F2025-10-28%2020.30.33.png)

    - ![截屏2025-10-28 20.30.38](./assets/%E6%88%AA%E5%B1%8F2025-10-28%2020.30.38.png)

      

## A3.2.6 Construct a database normalized to 3NF for a range of real-world examples

> 书上一堆废话，A3.2.5的内容掌握了就行

## A3.2.7 Evaluate the need for denormalizing databases

- **Advantages**
  - Simpler and faster queries as the database has to look at fewer entities to collect all the data.
  - Faster data retrieval as the database has fewer joins to complete. 
- **Disadvantages**
  - More challenging updates and inserts as some of the data is repeated.
  - Updating code can be difficult to write as the data is in multiple places. 
  - There may be inconsistencies as there are duplicate copies of data.
  - The fact there are many copies of some data requires more storage.
  - 这书上写的还是废话，其实就是**data redundancy**或者说是**duplicated data**

## A3.3.1 Outline the difference between data language types within structured query language (SQL)

- ![截屏2025-10-25 16.14.22](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2016.14.22.png)

- ***Data definition language(DDL)***
  - is used to create the database structures. 
  - It is used to create the schema, the tables, and constraints within the database. Using DDL statements, you can create the outline of the database. 
  - Example ***DDL*** commands in SQL:
    - **CREATE** used to create a entity/table. 
    - **ALTER** used to change the structure of the table/database
    - **DROP** used to delete table/entity from within the database structure. 
    - **TRUNCATE** used to remove all records/rows from an entity/table within the database structure, **but will not delete the table itself, only the records inside will be affected.** 
    - **RENAME** used to rename an entity/table within a database structure. 
    - **COMMENT** used to add a comment to the table, used when creating the table. 

- ***Data manipulation language(DML)***
  - is used to access the data within the database and to manipulate the data within the database. For example, querying the table for information, updating records, and deleting records. 
  - ![截屏2025-10-25 16.20.39](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2016.20.39.png)

- **Data control language(DCL)**
  - is used to control access to the database. The DCL helps to maintain security in the database as it allows user to have access to the database or it can revoke data from the database. 
  - **GRANT** allows user access privileges in a database. 
    - GRANT privileges ON database_name.table_name TO 'username'@'host';
      - E.g. 
        - GRANT SELECT, INSERT, ALTER, UPDATE ON demo.test TO 'username'@'host';
        - GRANT ALL PRIVILEGES ON demo.test TO 'username'@'host';
  - **REVOKE** allows the removal of privileges in a database. 
    - REVOKE privileges school.students FROM 'username'@'localhost';
      - E.g. 
        - REVOKE SELECT, INSERT, ALTER, UPDATE ON demo.test TO 'username'@'host';
        - REVOKE ALL PRIVILEGES ON demo.test TO 'username'@'host';

- **Transaction control language(TCL)**
  - is used to complete the changes in a database. 
  - ![截屏2025-10-25 16.30.00](./assets/%E6%88%AA%E5%B1%8F2025-10-25%2016.30.00.png)
  - 一个 transaction（事务）就是一组要么全部成功、要么全部失败的操作。
  - E.g.
    START TRANSACTION;
    UPDATE accounts SET balance = balance - 100 WHERE id = 1;
    UPDATE accounts SET balance = balance + 100 WHERE id = 2;
    COMMIT;
  - 如果中途出错，就可以用 `ROLLBACK` 回到最初状态。
  - `COMMIT` 将当前事务中的所有更改 **永久写入数据库**。
    START TRANSACTION;
    UPDATE students SET grade = 90 WHERE id = 1;
    COMMIT;
  - `COMMIT` 用于永久提交前面的 transaction 中的所有操作，无法撤销
  - `ROLLBACK` 撤销自上次 `START TRANSACTION` 以来所做的所有更改。
    START TRANSACTION;
    UPDATE students SET grade = 90 WHERE id = 1;
    ROLLBACK;
  - `ROLLBACK` 用于撤销前面的 transaction 中的所有操作(当 administrator 后悔前面的操作)

### Using SQL to develop a database/table

- **Create table**

```sql
CREATE DATABASE demoDB;

-- With primary key
CREATE TABLE table_name (
    Attribute1 datatype NOT NULL PRIMARY KEY,
    Attribute2 datatype,
    Attribute3 datatype
);

-- With primary key and foreign key
CREATE TABLE table_name (
    Attribute1 datatype NOT NULL PRIMARY KEY,
    Attribute2 datatype,
    Attribute3 datatype,
    Attribute4 datatype,
    FOREIGN KEY (Attribute4) REFERENCES other_table(Attribute4)
);
-- other_table is the name of another table that you are linking with
```

- **Drop table**

```sql
# Drop the tabel itself
DROP TABLE table_name;
```

- **Alter table**

```sql
-- Add a column
ALTER TABLE table_name
ADD COLUMN attribute datatype AFTER existing_attribute;

-- Example
ALTER TABLE Customer
ADD COLUMN deliveryAddress VARCHAR(255) AFTER customer_name;

-- Drop a column
ALTER TABLE table_name
DROP COLUMN attribute;

-- Example
ALTER TABLE Customer
DROP COLUMN deliveryPreference;

-- Modify column datatype
ALTER TABLE students
MODIFY COLUMN age VARCHAR(50);

-- Change column name and datatype
ALTER TABLE students
CHANGE COLUMN old_name new_name VARCHAR(50);

-- Rename the table
ALTER TABLE students RENAME TO pupils;

-- Add primary key
ALTER TABLE students
ADD PRIMARY KEY (id);

-- Add foreign key
ALTER TABLE orders
ADD CONSTRAINT fk_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);

-- Add constraints
-- Primary key constraint
ALTER TABLE students
ADD CONSTRAINT pk_student_id PRIMARY KEY (student_id);

-- Unique constraint
ALTER TABLE students
ADD CONSTRAINT unique_email UNIQUE (email);

-- Check constraint
ALTER TABLE students
ADD CONSTRAINT check_age CHECK (age >= 0 AND age <= 120);

-- Drop a constraint
ALTER TABLE table_name
DROP CONSTRAINT constraint_name;

-- NOT NULL
ALTER TABLE students
MODIFY COLUMN name VARCHAR(50) NOT NULL;

-- Default value
ALTER TABLE students
ALTER COLUMN status SET DEFAULT 'active';
```

- **Modifying data in a table**

```sql
-- Insert value
INSERT INTO table_name (Attribute1, Attribute2, Attribute3, ...)
VALUES (value1, value2, value3, ...);

-- Update value
UPDATE table_name
SET Attribute1 = value1, Attribute2 = value2
WHERE condition;

-- Delete value with condition
DELETE FROM table_name
WHERE condition;
```



## A3.3.2 Construct queries between two tables in SQL

> I also include some common sql commands in this chapter, not only containing the contents in the textbook.

- **Queries** are used in databases to extract data and provide context for data.  Data within a database has little relevance unless it is put into context. Queries can be used for filtering, which means finding the data you want to know from the database. 

- **BETWEEN**

```sql
SELECT * FROM table_name 
WHERE attributel BETWEEN valuel AND value2;

# Example
SELECT * from students where score BETWEEN 90 and 100
```

-  **ORDER BY** 

```sql
# Order by attribute ASC(default), DESC
SELECT * from table_name WHERE condition order by attribute ASC or DESC;

# Example
SELECT student_name from tests_score order by score ASC;

SELECT student_name from tests_score order by score ASC, student_name ASC;
```

- **GROUP BY**

```sql 
# Group by certain attribute
SELECT Attribute1, Attribute2
FROM table_name
WHERE condition
GROUP BY Attribute1, Attribute2
ORDER BY Attribute1;  

# Example show the average score of each subject
SELECT avg(score) as average_score, subject from Subjects group by subject order by avg(score) DESC;

```

- **HAVING** 
- Can be only used after GROUP BY

```sql
# Using having to filter the rows in group
SELECT COUNT(Attribute2), Attribute from table_name GROUP BY Attribute HAVING COUNT(Attribute2) condition;

# Example
SELECT COUNT(CustomerID), CustomerCountry FROM Customer GROUP BY CustomerCountry HAVING COUNT(CustomerID) > 2;
```

- **JOIN**
- There are three types of JOIN
  - `INNER JOIN` returns all the records that have matching values in both tables.
  - `LEFT JOIN`  returns all rows from the left table, and the matched rows from the right table. If there is no match, the result will still include the left table row**, but the right table columns will **show NULL. 
  - `RIGHT JOIN` returns all rows from the right table, and the matched rows from the left table. If there is no match, the left table columns will **show NULL**.  

```sql
# INNER JOIN
SELECT table_name1.attribute1, table_name1.attribute2, table_name1.attribute3, table_name2.attribute2 FROM table_name1 INNER JOIN table_name2 WHERE table_name1.attribute1 = table_name2.attribute2;

# Example
SELECT Item.ItemID, Item.ItemDesc, Item.ItemCost, Item.ArtistID, Artist.ArtistName, Artist.ArtistEmail FROM Item INNER JOIN Artist ON Item.ArtistID = Artist.ArtistID WHERE ItemCost > 100;
```

- **LIKE**
- The Like operator is used within the Where operator to look for non-exact matches. This is known as pattern matching within the attribute.
- There are two wildcards used within the database system
  - `_` represents one single character
  - `%` represents any number of characters(zero, one, or many). 

```sql
# Only select the Artist whose name ends with 'work'
SELECT Attribute1, Attribute2 FROM table_name WHERE Attribute LIKE pattern;
SELECT * FROM Artist WHERE ArtistName LIKE '%work';

# Only select the Artist whose name starts with 'work'
SELECT Attribute1, Attribute2 FROM table_name WHERE Attribute LIKE pattern;
SELECT * FROM Artist WHERE ArtistName LIKE 'work%';

# Only select the Artist whose name contains the substring 'work'
SELECT Attribute1, Attribute2 FROM table_name WHERE Attribute LIKE pattern;
SELECT * FROM Artist WHERE ArtistName LIKE '%work%';
```

- **CASE WHEN** **and** **CASE**

```sql
# Format for CASE WHEN
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE resultN
END AS xxx
FROM xxxx;

# Example for CASE WHEN
SELECT name, score,
    CASE
        WHEN score >= 90 THEN 'A'
        WHEN score >= 80 THEN 'B'
        WHEN score >= 70 THEN 'C'
        ELSE 'Fail'
    END AS grade
FROM Scores;

# Example for CASE
CASE score
    WHEN 90 THEN 'Perfect'
    WHEN 80 THEN 'Good'
    ELSE 'Average'
END AS grade
FROM Scores;

SELECT name,
  CASE score
      WHEN 90 THEN 'Perfect'
      WHEN 80 THEN 'Good'
      ELSE 'Average'
  END AS grade 
FROM Scores;
```

-  **IF** 

```sql
# Format for IF in Mysql
IF(condition, value_if_true, value_if_false)

# Example       
SELECT name, 
       IF(score >= 60, 'Pass', 'Fail') AS result
FROM Students;
```

- **IFNULL**
  - deal when null occurs

```sql 
# Format for IFNULL in Mysql
IFNULL(expression, default_value)

# Example
SELECT name, salary + IFNULL(bonus, 0) AS total_income
FROM Employees;
# This means, if bonus is NULL, the value returned by be zero, if you don't use IFNULL to check, the result may be NULL
```

- **NULLIF**
  - When two values equal, return null 

```sql
# Format for NULLIF in mysql
NULLIF(expr1, expr2)

# Example
SELECT NULLIF(10, 10);  -- return NULL
SELECT NULLIF(10, 5);   -- return 10

# Example: Dealing with potential ZeroDivisionError
SELECT year_salary / NULLIF(months,0) as avg_salary from employees;
```

- **Common Operations in Mysql**

```sql
=  # check if equals to 
!= # not equals to 
BETWEEN a AND b # both inclusive
xxx IN (x,y,z) # check whether the given value is in the predefined set
IS NULL
IS NOT NULL
AND, OR, NOT
/ # float division
div # integer division
```

- **Subquery 子查询**

```sql
# Basic format for subquery command
SELECT column_name
FROM table_name
WHERE column_name operator (SELECT column_name FROM table_name WHERE condition);

# Find the student whose score is above the average                        
SELECT name, grade
FROM Students
WHERE grade > (SELECT AVG(grade) FROM Students);

# 找出成绩前两位的同学
SELECT name, grade
FROM Students
where grade in (SELECT grade from Students order by grade DESC limit 2);
```

## A3.3.3 Explain how SQL can be used to update data in a database

> `INSERT INTO`以及`UPDATE`以及`DELETE`的用法前面都写了（注意这些都是DML，不需要`TABLE`关键字)

## A3.3.4 Construct caculations with a database using SQL's aggregate function

- Aggregate functions allow you to perform calculations on the data in the database.

```sql
# Calculate the average
SELECT AVG(attribute) FROM TABLE_NAME;

SELECT AVG(age) FROM student;

# Calculate the average with condition
SELECT AVG(attribute) FROM TABLE_NAME WHERE condition;

SELECT AVG(score) FROM student WHERE score > 87;

# Returns the number of rows using COUNT with condition
SELECT COUNT(attribute) FROM TABLE_NAME;

SELECT COUNT(student_id) FROM student;

SELECT COUNT(attribute) FROM TABLE_NAME WHERE condition;

SELECT COUNT(score) FROM student where score > 87;

# This only counts of the number of unique rows
SELECT COUNT(DISTINCT attribute) FROM student;

SELECT COUNT(DISTINCT hobby) FROM student;

# Returns the highest value in an entity for a selected attribute
SELECT MAX(attribute) FROM TABLE_NAME;

SELECT MAX(attribute) FROM TABLE_NAME WHERE condition;

# Returns the smallest value in an entity for a selected attribute
SELECT MIN(attribute) FROM TABLE_NAME;

SELECT MIN(attribute) FROM TABLE_NAME WHERE condition;

# Returnes the total sum of the data 
SELECT SUM(attribute) FROM TABLE_NAME;

SELECT SUM(attribute) FROM TABLE_NAME WHERE condition;
```




