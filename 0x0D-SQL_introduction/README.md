## 0x0D. SQL - Introduction

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/rtcwz.jpg)

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

       At the end of this project you are expected to be able to explain to anyone,
       without the help of Google:

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does DDL and DML stand for
* How to CREATE or ALTER a table
* How to SELECT data from a table
* How to INSERT, UPDATE or DELETE data
* What are subqueries
* How to use MySQL functions

**Requirements for SQL scripts**

* Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)

