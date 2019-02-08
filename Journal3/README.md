# Journal 3
### URL
The URL for the source code of this project is available here: https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal3
### Assignment Writeup
#### Intentions
My intention for this project was to create a contrived example of a SQL Injection, because we'll be using SQL in this class, presumably 
having it interact with a webpage.
#### Input Work Done
The input work done is this subdirectory of the repository.
#### Output Results

Login Screen with a good actor, from the table of users, and user's login screen.
![File selected from landing page](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/GoodActor.png)
![Returned data from that file](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/Home.png)

Log in as any valid user without their password
![Log in as any valid user without their password](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/injection.png)
![Returned data from that file](https://github.com/ekivolowitz/LIS351Projects/blob/master/imgs/Home.png)


#### Approach
It is common for web developers to not use [Prepared Statements](https://en.wikipedia.org/wiki/Prepared_statement) when crafting SQL queries. This means that you can inject your own SQL code, if you'd like. For example,
```sql
SELECT COUNT(*) FROM USERS WHERE username='" + username + "' AND pwd='" + password +"'
```
is injectable. If you give a valid username, and then insert
```
' OR 1=1--
```
You will have the statement
```sql
SELECT COUNT(*) FROM USERS WHERE username='" + username + "' AND pwd='' OR 1=1-- + "'
```
This essentially says, select user where username is the supplied username, and where the password is `''` OR WHEREVER `1=1`, which is always true. Then the `--` tells sqlite to ignore the rest of the query as it is commented out. This is a golden key to access any account on this site. 

#### Thoughts on the results
This was a fun little project because there is the space where programmers make intended functionality, and the space where they made functionality that they didn't intend for.

### Dependencies
* [python3](https://www.python.org/download/releases/3.0/)
* [Flask](http://flask.pocoo.org/)
### Usage
```bash
$ python3 main.py
```
Now navigate to `localhost:5000` in your favorite web browser and use the letter counting program!
### References
* [Journal 1](https://github.com/ekivolowitz/LIS351Projects/tree/master/Journal1)
* [Flask sql documentation](http://flask.pocoo.org/docs/1.0/patterns/sqlite3)
