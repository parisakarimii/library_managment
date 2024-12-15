import sqlite3
import sys


conn=sqlite3.connect('Library.db')
cursor=conn.cursor()

def create_table():
    sql='''create table tblBook(
        book_id integer primary key Autoincrement,
        title text(100),
        author text(50),
        pub_year integer,
        subject text(50)
    )
    '''
    cursor.execute(sql)
    conn.commit()
    
def insert_data(title,subject,author,pub_year):
    sql= f" insert into tblBook (title,subject,author,pub_year) values ('{title}','{subject}','{author}','{pub_year}') "
    cursor.execute(sql)
    conn.commit()
    
def show_data(book_id):
    result = cursor.execute(f'select * from tblBook where book_id={book_id}').fetchall()
    if result:
        data=result[0]
        return f'''book_id= {data[0]}

title= {data[1]}

subject= {data[2]}

pub_year= {data[3]}

author= {data[4]}'''
    else:
        return f"Not in database!"


def updatee_data(field,new_value,book_id):
    sql= f" update tblBook set {field}='{new_value}'  where book_id={book_id} "
    cursor.execute(sql)
    conn.commit()

def deletee_data(book_id):
    sql= f" delete from tblBook where book_id={book_id}"
    cursor.execute(sql)
    conn.commit()
    
def exit_data():
    sys.exit()
    
def main():
    create_table()
    print('''what do you want to do?
            1) Insert Data
            2) Update Data
            3) Delete Data
            4) Show Data
            5) Exit
          ''')
    choice=input()
    if choice=='1':
        title=input('Title: ')
        subject=input('Subject: ')
        author=input('Author: ')
        pub_year=input('Publish Year: ')
        insert_data(title,subject,author,pub_year)
    elif choice=='2':
        print('''What do you want to update? 
                1) Title
                2) Subject
                3) Author
                4) Publish year
              ''')
        choice_update=input()
        if choice_update=='1':
            field='title'
        elif choice_update=='2':
            field='subject'
        elif choice_update=='3':
            field='author'
        elif choice_update=='4':
            field='pub_year'
        new_value=input('Enter new value: ')
        book_id=input('Enter Book ID: ')
        update_data(book_id,field,new_value)
    delete_data()
    show_data()
    exit_data()
    
if __name__=='__main__':
    main()
    conn.close()
    