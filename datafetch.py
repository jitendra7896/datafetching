import mysql.connector

mydata = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password@123",
  port="3306",
  database="user1"
)
x=raw_input("Enter customer code==")
sqls=("Select c.cust_name,o.ord_num,a.agent_name,o.ord_date,o.advance_amount,o.ord_amount from((orders as o  inner join customer as c on o.cust_code=c.cust_code)inner join agents as a on o.agent_code=a.agent_code) where c.cust_code='"+ x +"'")
jcursor = mydata.cursor()
jcursor.execute(sqls)
y=jcursor.fetchall()
print(y)
