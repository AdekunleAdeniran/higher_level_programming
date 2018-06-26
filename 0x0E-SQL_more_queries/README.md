## 0x0E. SQL - More queries

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/66988091.jpg)

**About MySQL**

MySQL is an open source database management software that helps users store, organize, and retrieve data. It is a very powerful program with a lot of flexibility—this tutorial will provide the simplest introduction to MySQL

How to Install MySQL on Ubuntu and CentOS
If you don't have MySQL installed on your droplet, you can quickly download it.

**Ubuntu:**

`sudo apt-get install mysql-server`

How to Access the MySQL shell
Once you have MySQL installed on your droplet, you can access the MySQL shell by typing the following command into terminal:

`mysql -u root -p`

After entering the root MySQL password into the prompt (not to be confused with the root droplet password), you will be able to start building your MySQL database.

**Two points to keep in mind:**

1. All MySQL commands end with a semicolon; if the phrase does not end with a semicolon, the command will not execute.

2. Also, although it is not required, MySQL commands are usually written in uppercase and databases, tables, usernames, or text are in lowercase to make them easier to distinguish. However, the MySQL command line is not case sensitive.
(source: https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)

**What you should learn from this project**

	At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

**Exercises**

**0. My privileges!**

	Write a script that lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server.

**1. Root user**

	Write a script that creates the MySQL server user user_0d_1.

* user_0d_1 should have all privileges on your MySQL server
* The user_0d_1 password should be set to user_0d_1_pwd
* If the user user_0d_1 already exists, your script should not fail

**2. Read user**
	
	Write a script that creates the database hbtn_0d_2 and the user user_0d_2.

* user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
* The user_0d_2 password should be set to user_0d_2_pwd
* If the database hbtn_0d_2 already exists, your script should not fail
* If the user user_0d_2 already exists, your script should not fail

**3. Always a name mandatory**

	Write a script that creates the table force_name on your MySQL server.

* force_name description:
	* id INT
	* name VARCHAR(256) can’t be null
* The database name will be passed as an argument of the mysql command
* If the table force_name already exists, your script should not fail