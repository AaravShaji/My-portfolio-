import mysql.connector
from tabulate import tabulate

def add_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    cursor.execute(
        'create table if not exists book(bookId int(50) primary key, title varchar(20) , author varchar(20), publisher varchar(20), pages int(10), '
        'price int(10), edition varchar(30), copies int(30));')
    bookId = input('Enter Book Id: ')
    title = input('Enter Book Title: ')
    author = input('Enter Book Author: ')
    publisher = input('Enter Book Publisher: ')
    pages = input('Enter Book Pages: ')
    price = input('Enter Book Price: ')
    edition = input('Enter Book Edition: ')
    copies = int(input('Enter copies: '))
    sql = cursor.execute(
        'insert into book (bookId,title,author,price,pages,publisher,edition,copies)  values ( "' +
        bookId + '","' + title + '","' + author + '","' + price + '","' + pages + '","' + publisher + '","' + edition + '","' + str(
            copies) + '");')
    conn.commit()
    for _ in range(0, copies):
        cursor.execute(sql)
    conn.close()
    print('-' * 60)
    print('\nNew Book added successfully')
    print('-' * 60)


def add_member():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    cursor.execute(
        'create table if not exists member(MemberId int(50) primary key, Name varchar(20), Class varchar(11), Address varchar(40), Phone int(50), Email varchar(30));')
    MemberId = input('Enter Member Id: ')
    Name = input('Enter Member Name: ')
    Class = input('Enter Member Class & Section: ')
    Address = input('Enter Member Address: ')
    Phone = input('Enter Member Phone: ')
    Email = input('Enter Member Email: ')
    sql = cursor.execute(
        'insert into member(MemberId,Name,Class,Address,Phone,Email) values ( "' + MemberId + '","' + Name + '","' + Class + '","' + Address + '","' + Phone + '","' + Email + '");')
    conn.commit()
    cursor.execute(sql)
    conn.close()
    print('-' * 60)
    print('\nNew Member added successfully')
    print('-' * 60)


def modify_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    print('-' * 60)
    print('Modify Book Details Screen ')
    print('-' * 60)
    print('\n1. Book Title')
    print('\n2. Book Author')
    print('\n3. Book Publisher')
    print('\n4. Book Pages')
    print('\n5. Book Price')
    print('\n6. Book Edition')
    Choice = int(input('\nEnter your choice: '))
    field = ''
    if Choice == 1:
        field = 'title'
    if Choice == 2:
        field = 'author'
    if Choice == 3:
        field = 'publisher'
    if Choice == 4:
        field = 'pages'
    if Choice == 5:
        field = 'price'
    if Choice == 6:
        field = 'edition'
    bookId = input('Enter Book ID: ')
    value = input('Enter new value: ')
    if field == 'pages' or field == 'price':
        sql = cursor.execute('update book set ' + field + ' = ' + value + ' where bookId = ' + bookId + ';')
    else:
        sql = cursor.execute('update book set ' + field + ' = "' + value + '" where bookId = ' + bookId + ';')
    conn.commit()
    cursor.execute(sql)
    print('-' * 60)
    print('\nBook details Updated.....')
    print('-' * 60)
    conn.close()


def modify_member():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    print('-' * 60)
    print('Modify Member Information Screen ')
    print('-' * 60)
    print('\n1. Name')
    print('\n2. Class')
    print('\n3. Address')
    print('\n4. Phone')
    print('\n5. Email')
    Choice = int(input('\nEnter your choice: '))
    field = ''
    if Choice == 1:
        field = 'Name'
    if Choice == 2:
        field = 'Class'
    if Choice == 3:
        field = 'Address'
    if Choice == 4:
        field = 'Phone'
    if Choice == 5:
        field = 'Email'
    MemberId = input('Enter Member ID: ')
    value = input('Enter new value: ')
    sql = cursor.execute('update member set ' + field + ' = "' + value + '" where MemberId = ' + MemberId + ';')
    cursor.execute(sql)
    conn.commit()
    print('-' * 60)
    print('Member details Updated.....')
    print('-' * 60)
    conn.close()


def issue_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    cursor.execute(
        'create table if not exists issue(book_id int(50) primary key, MemberId int(50), book_title varchar(50), Name varchar(50), Class varchar(50), status varchar(20));')
    print('-' * 60)
    print('\n BOOK ISSUE SCREEN ')
    print('-' * 60)
    book_id = int(input('Enter the Book ID: '))
    MemberId = int(input('Enter the Member ID: '))
    book_title = input('Enter the title of the book: ')
    Name = input('Enter Name: ')
    Class = input('Enter Class: ')
    sql = cursor.execute('insert into issue(book_id,MemberId,book_title,Name,Class,status) values ("'+str(book_id)+'","'+str(MemberId)+'","'+book_title+'","'+Name+'","'+Class+'","issued");')
    cursor.execute(sql)
    conn.commit()
    print('-' * 60)
    print('Book has been issued successfully to:',Name)
    print('-' * 60)
    conn.close()


def submit_book():
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    cursor.execute(
        'create table if not exists submit(book_id int(50) primary key, book_title varchar(50), Name varchar(50), Class varchar(50),status varchar(20));')
    print('-' * 60)
    print('\n BOOK RETURN SCREEN ')
    print('-' * 60)
    book_id = int(input('Enter Book ID : '))
    book_title = input('Enter the title of the book: ')
    Name = input('Enter Name: ')
    Class = input('Enter Class: ')
    sql = cursor.execute('insert into submit(book_id,book_title,Name,Class,status) values ("' + str(
        book_id) + '","' + book_title + '","' + Name + '","' + Class + '","returned");')
    cursor.execute(sql)
    conn.commit()
    print('\n\nBook returned successfully by:',Name)
    a = "delete from issue where Name=%s"
    data = (Name,)
    cursor.execute(a, data)
    records = cursor.fetchall()
    conn.commit()
    print('-' * 60)
    print('\nMember deleted successfully from issue table and book available for next issue....')
    print('-' * 60)
    conn.close()


def dMember():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    ac = input('Enter Member ID: ')
    a = "delete from member where MemberId=%s"
    data = (ac,)
    cursor.execute(a, data)
    conn.commit()
    print('-' * 60)
    print('Member deleted successfully')
    print('-' * 60)
    conn.close()


def dispbook():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    a = "select * from book"
    cursor.execute(a)
    myresult = cursor.fetchall()
    for i in myresult:
        h=['bookId' , '\ttitle'  , '\tauthor' , '\tpublisher' , 'pages', 'price', 'edition', 'copies']
        print(tabulate([i],headers=h,tablefmt='plain'))
        conn.close()

def dispmember():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    a = "select * from member"
    cursor.execute(a)
    myresult = cursor.fetchall()
    h=['MemberId' , '\tname'  , '\tclass & section' , '\taddress' , 'phone', 'email']
    for i in myresult:
        print(tabulate([i],headers=h,tablefmt='plain'))
        conn.close()


def dbook():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    ac = input('Enter Book ID: ')
    a = "delete from book where bookId=%s"
    data = (ac,)
    cursor.execute(a, data)
    conn.commit()
    print('-' * 60)
    print('Book deleted successfully')
    print('-' * 60)
    conn.close()

def submit_table():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    a = "select * from submit"
    cursor.execute(a)
    myresult = cursor.fetchall()
    h=['book_id','book_title','Name','Class','status']
    for i in myresult:
        print('-' * 60,'\n\n')
        print(tabulate([i],headers=h,tablefmt='plain'))
        print('\n\n','-' * 60)

def issue_table():
    conn = mysql.connector.connect(host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    a = "select * from issue"
    cursor.execute(a)
    myresult = cursor.fetchall()
    h=['book_id','MemberId','book_title','Name','Class','status']
    for i in myresult:
        print('-' * 60,'\n\n')
        print(tabulate([i],headers=h,tablefmt='plain'))
        print('\n\n','-' * 60)


def display_menu():
    while True:
        print('-' * 60)
        print('\t>--DISPLAY MENU--<')
        print('-' * 60)
        print('\n1. Display Member')
        print('\n2. Display Book')
        print('\n3. Display the returned books table')
        print('\n4. Display the issued books table')
        print('\n5. Exit to main menu')
        choice =int(input('\nEnter your choice:'))
        if choice == 1:
            dispmember()
        elif choice == 2:
            dispbook()
        elif choice ==3:
            submit_table()
        elif choice ==4:
            issue_table()
        else:
            choice==5
            break
                    
def search_book(field):
    conn = mysql.connector.connect(
        host='localhost', database='library', user='root', password='Aarav21%')
    cursor = conn.cursor()
    print('-' * 60)
    print('\n BOOK SEARCH SCREEN ')
    print('-' * 60)
    msg = 'Enter ' + field + ' Value :'
    title = input(msg)
    sql = 'select * from book where ' + field + ' like "%' + title + '%"'
    cursor.execute(sql)
    records = cursor.fetchall()
    print('Search Result for :', field, ' :', title)
    print('-' * 60)
    h=['bookId' , '\ttitle'  , '\tauthor' , '\tpublisher' , 'pages', 'price', 'edition', 'copies']
    for record in records:
        print(tabulate([record],headers=h,tablefmt='plain'))
    conn.close()
    print('-' * 60)
    input('\nPress ENTER to continue....\n')


def search_menu():
    while True:
        print('-' * 60)
        print('\t>---SEARCH MENU---<')
        print('-' * 60)
        print("\n1.  To search a book by its title")
        print('\n2.  To search a book by its author')
        print('\n3.  To search a book by its publisher')
        print('\n4.  Exit to main Menu')
        choice = int(input('\nEnter your choice: '))
        field = ''
        if choice == 1:
            field = 'title'
        if choice == 2:
            field = 'author'
        if choice == 3:
            field = 'publisher'
        if choice == 4:
            break
        search_book(field)

def main_menu():
    while True:
        print("""
                                    -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                                         WELCOME TO LIBRARY MANAGEMENT SYSTEM
                                    -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
                                   
    1.  Add Book
    2.  Add Member
    3.  Modify Book
    4.  Modify Member
    5.  Issue Book
    6.  Submit Book
    7.  Delete Book
    8.  Delete Member
    9.  Display Menu
   10. Search Menu
   11. Exit Library Manager
   """)
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            add_member()
        elif choice == '3':
            modify_book()
        elif choice == '4':
            modify_member()
        elif choice == '5':
            issue_book()
        elif choice == '6':
            submit_book()
        elif choice == '7':
            dbook()
        elif choice == '8':
            dMember()
        elif choice == '9':
           display_menu()
        elif choice == '10':
            search_menu()
        elif choice == '11':
            print('-' * 60)
            print('Thank you')
            print('-' * 60)
            break
        else:
            print("Incorrect choice, try again.......")
            main_menu()
            continue
        ans = input('Would you like to exit the system ?[Y/N]')
        if ans == 'y' or ans == 'Y':
            print('-' * 60)
            print('Thank you')
            print('-' * 60)
            break 

def pswd():
    ps=input("\nEnter the password to access Library Manager: ")
    if ps=='1234':
        main_menu()
    else:
        print('-' * 60)
        print("Wrong password,try again...")
        print('-' * 60)
        pswd()
pswd()
        
        


