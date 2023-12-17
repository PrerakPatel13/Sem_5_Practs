import mysql.connector as msc
cnx = msc.connect(user='root', password='Mysql@123', host="127.0.0.1",database="gada_electronics")
cursorstr = cnx.cursor()
cursorstr.execute('create database gada_electronics')

cursorstr.execute('create table student(id int(25) , first_name varchar(25), last_name varchar(25));')

cursorstr.execute("insert into student values (128,'Ayush','Shah'),(129,'aditya','rohila'),(130,'dev','patel');")

cursorstr.execute("delete from student where id=128;")

cursorstr.execute("select * from student;")

cursorstr.execute("select * from student where id=129;")

cursorstr.execute("update student set last_name='patel' where id=129 ;")

cursorstr.execute("ALTER TABLE student ADD marks varchar(25)")

cursorstr.execute("update student set marks='25' where id=129 ;")

result=cursorstr.fetchall()
for x in result:
    print(x)
cnx.commit()
