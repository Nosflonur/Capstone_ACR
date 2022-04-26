import sqlite3, csv
import random
import statistics
import os
from datetime import datetime
from sqlite3 import Error

connection = sqlite3.connect('competency_tracker.db')
cursor = connection.cursor()
db_file = 'competency_tracker.db'
print('\n' *100)
CLR = "\x1B[0K"  

view = 0
user_id = 0
test_id = 0
test_name = ""
test_date = ""
test_data_id = 0
raw_score = 0
competency = 0
manager = 0
user_id = 0
manager_id = 6
id_user = 0
now = ""
test_dict = {}
average_comp = 0
num_users = 0
result = ""
check = ()
       
def login_view():
    user_id = 0
    clearup()
    login_banner = [
     u"\u001b[34m"  
    "     ╔═════════════════════════════════════════╗",
    "     ║ ╔═════════════════════════════════════╗ ║",
    "     ║ ║        Competency Tracker           ║ ║",
    "     ║ ║               LOGIN                 ║ ║",
    "     ║ ╚═════════════════════════════════════╝ ║",
    "     ╚═════════════════════════════════════════╝\u001b[0m"
    ]
    for i in range(6):
        print(login_banner[i])
   
def login_menu():
    print(u"\u001b[34m") 
    print('    [U] LOGIN as USER')
    print('    [M] LOGIN as MANAGER')
    print('    [Q] Quit \u001b[0m')
                
def user_view():
    clearup()
    user_banner = [
     u"\u001b[33m"  
    "    ╔════════════════════════════════════════════╗",
    "    ║ ╔════════════════════════════════════════╗ ║",
    "    ║ ║           Competency Tracker           ║ ║",
    "    ║ ║               USER MENU                ║ ║",
    "    ║ ╚════════════════════════════════════════╝ ║",
    "    ╚════════════════════════════════════════════╝\u001b[0m"
    ]
    for i in range(6):
        print(user_banner[i])
    user_menu()
    
def user_menu():
    print(u"\u001b[33m") 
    print('    ╔════════════════════════════════════════════╗')
    print('    ║.  √[A] See my Personal Data.              .║')
    print('    ║.  √[B] Edit my Personal Data.             .║')
    print('    ║.  √[C] See my test results.               .║')
    print('    ║.  √[D] See a Summary of my Competencies.  .║')
    print('    ║.  √[E] Take a Test.                       .║')
    print('    ║.  √[L] LOGOUT                             .║')  
    print('    ╚════════════════════════════════════════════╝\u001b[0m')    
  
def manager_view():
    clearup()
    manager_banner = [
        u"\u001b[31m"  
    "                ╔═════════════════════════════════════════╗",
    "                ║ ╔═════════════════════════════════════╗ ║",
    "                ║ ║        Competency Tracker           ║ ║",
    "                ║ ║           MANAGER MENU              ║ ║",
    "                ║ ╚═════════════════════════════════════╝ ║",
    "                ╚═════════════════════════════════════════╝\u001b[0m"
    ]
    for i in range(6):
        print(manager_banner[i])
    manager_menu()
    
def manager_menu():
    print(u"\u001b[31m") 
    print('╔═════════════════════════════════════╦════════════════════════════════════════════╗')
    print('║  √[1] Find a User.                  ║ √[11] View all Users.                      ║')
    print('║  √[2] Add a User.                   ║ √[12] View 1 Subject Comps for All Users.  ║')
    print('║  √[3] Add a Test for 1 User.        ║ √[13] Have All Users take a Test.          ║')
    print('║  √[4] View All Comps for 1 User.    ║ √[14] View Comps for all Users.            ║')
    print('║  √[5] View All Tests for 1 User.    ║ √[15] View Ave of all Comps for All Users. ║')
    print('║  √[6] View Ave all Comps 1 User.    ║ √[16] CSV Import                           ║')
    print('║  √[7] Edit Info for 1 User.         ║ √[17] CSV Export                           ║')
    print('║  √[8] Edit 1 Test for 1 User.       ║ √[18] Report:Show Personal Info for 1 User.║')
    print('║  √[9] Delete 1 Test for 1 User.     ║ √[19] Report:Show All Comps for 1 User.    ║')
    print('║   [10] Save as PDF.                 ║ √[20] Report: Show All Comps for All Users.║')
    print('║  √[00] Log Out                      ║                                            ║') 
    print('╚═════════════════════════════════════╩════════════════════════════════════════════╝\u001b[0m')        

def view_user_info():
    conn()
    print('     *-*-* Here is the Current Personal Data *-*-*')
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Phone":12}{"Email":6}')
    print(f'{"--":5}{"----------":15}{"---------":15}{"-----":12}{"-----":6}')
    rows = cursor.execute("SELECT user_id, first_name, Last_name, phone, email FROM People WHERE user_id = ?",(user_id,)).fetchall()
    info_data =['ID', 'FIRST NAME', 'LAST NAME', 'PHONE', 'EMAIL']
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:<5}{info_data[1]:<15}{info_data[2]:<15}{info_data[3]:<12}{info_data[4]:6}')
        
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)  
 
def edit_user_info():
    conn()
               
    while True:
        print('\n' *3)        
        print('     *-*-* Here is your Current Personal Data *-*-*')
        print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Phone":12}{"Email":6}')
        print(f'{"--":5}{"----------":15}{"---------":15}{"-----":12}{"-----":6}')
        rows = cursor.execute("SELECT * FROM People WHERE user_id = ?",(user_id,)).fetchall()
        info_data = []
        for info_data in rows:
            info_data = [str(info) for info in info_data]
            print(f'{info_data[0]:<5}{info_data[1]:<15}{info_data[2]:<15}{info_data[3]:<12}{info_data[4]:6}')
  
        field = ''
        print('''\nWhat NEEDS to be UPDATED? )
        (F) First Name   (L) Last Name   (P) Phone   (E) Email  (N) Nothing''')
      
        field = input().lower()
        field_value = ""
        new_value = ""
        
        fields_dict = {
            'f':'first_name','l':'last_name','p':'phone','e':'email'
        }
        
        if field in fields_dict.keys():
            field_value = fields_dict[field]
                  
        if field == 'f':
            new_value = input('Please enter the correct First Name: ')
            user = f'UPDATE People SET first_name = ? WHERE user_id = {id_user};'
            cursor.execute(user, [new_value])
            break
        
        if field == 'l':
            new_value = input('Please enter the correct Last Name: ')
            user = f'UPDATE People SET last_name = ? WHERE user_id = {id_user};'
            cursor.execute(user, [new_value])
            break
   
        if field == 'p':
            new_value = input('Please enter the correct Phone Number: ')
            user = f'UPDATE People SET phone = ? WHERE user_id = {id_user};'
            cursor.execute(user, [new_value])
            break
        
        if field == 'e':
            new_value = input('Please enter the correct eMail Address: ')
            user = f'UPDATE People SET email = ? WHERE user_id = {id_user};'
            cursor.execute(user, [new_value])
            break
               
        if field == 'n':
            return
        if field == '':
            return   

    cursor.execute(f'UPDATE People SET {field_value} = ? WHERE user_id = ?',(new_value, user_id))
    connection.commit()
    print('\n' *100)
    print('*-*-* The Record has been updated *-*-*') 

def view_user_tests():
    conn()
    print('\n' *1)        
    print('     *-*-* Here are the Test Scores *-*-*')
    print(f'{"ID":4}{"TEST":19}{"DATE":12}{"RAW":5}{"COMPETENCY":12}{"MANAGER ID":6}')
    print(f'{"--":4}{"----":19}{"-----":12}{"---":5}{"----------":12}{"----------":6}')
    rows = cursor.execute("SELECT * FROM Testdata WHERE user_id = ?",(user_id,)).fetchall()
    info_data = []
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[2]:4}{info_data[3]:19}{info_data[4]:12}{info_data[5]:5}{info_data[6]:12}{info_data[7]:6}')
        
    print('\n' *2)
    wait_one = str(input("Here is your TEST Scores (Press ENTER to continue): "))
    print('\n' *100)

def view_test_summary():
    conn()
    comp_list()
    print(f'{" " * 24}{"*-*-* Here are the Test Competencies *-*-*"}')
  
    print(f'{"First Name":15}{"Last Name":15}{" 1":4}{" 2":4}{" 3":4}{" 4":4}{" 5":4}{" 6":4}{" 7":4}{" 8":4}{" 9":4}{"10":4}{"11":4}{"12":4}{"13":4}{"14":4}{"15":4}{"16":4}')
    print(f'{"----------":15}{"---------":15}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}')
    rows = cursor.execute("SELECT * FROM People WHERE user_id = ?",(user_id,)).fetchall()
    info_data =['FIRST NAME', 'LAST NAME', 'C1', 'C2' 'C3', 'C4' 'C5', 'C6' 'C7', 'C8' 'C9', 'C10' 'C11', 'C12' 'C13', 'C14' 'C15', 'C16']
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[1]:15}{info_data[2]:15}{info_data[10]:4}{info_data[11]:4}{info_data[12]:4}{info_data[13]:4}{info_data[14]:4}{info_data[15]:4}{info_data[16]:4}{info_data[17]:4}{info_data[18]:4}{info_data[19]:4}{info_data[20]:4}{info_data[21]:4}{info_data[22]:4}{info_data[23]:4}{info_data[24]:4}{info_data[25]:4}')
        
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)          

def take_test():
    conn()
    comp_list()
    global test_id
    global test_name
    global test_date
    global raw_score
    global competency
    global manager_id
    
    test_dict = {
    1:"Computer Anatomy",
    2:"Data Types",
    3:"Variables",
    4:"Functions",
    5:"Boolean Logic",
    6:"Conditionals",
    7:"Loops",
    8:"Data Structures",
    9:"Lists",
    10:"Dictionaries",
    11:"Working with Files",
    12:"Exception Handling",
    13:"Quality Assurance",
    14:"OOP",
    15:"Recursion",
    16:"Databases",
    }
    
    while True:
        try:
            test_id = int(input("Which TEST would you like to take (1-16)?"))
            if 1 <= test_id <= 16:
                break
            raise ValueError()
        except ValueError:
            print("Choose a test # between 1 and 16.")
    
    for i, j in test_dict.items():
        if (i) == (test_id):
            test_name = (j)
            print(test_name)
        else:
            pass 

    raw_score = random.randint(50,100)
    if raw_score >= 59:
        competency = 1
    if raw_score >= 69:
        competency = 2
    if raw_score >= 79:
        competency = 3
    if raw_score >= 89:
        competency = 4

    now = datetime.now() 
    test_date = now.strftime("%Y:%m:%d")
    
    print(f'{" " * 20}{"*-*-* Here is your Test Result *-*-*"}')
    print(f'{"TEST ID":9}{"TEST NAME":19}{"TEST DATE":12}{"RAW SCORE":11}{"COMPETENCY":12}{"MANAGER ID":10}')
    print(f'{"-------":9}{"---------":19}{"----------":12}{"---------":11}{"----------":12}{"----------":10}')
    print(f'{test_id:^9}{test_name:19}{test_date:12}{raw_score:^11}{competency:^12}{manager_id:^10}')
    
    test_info = (user_id,test_id,test_name,test_date,raw_score,competency,manager_id)
    cursor.execute("INSERT INTO Testdata (user_id, test_id, test_name, test_date, raw_score, competency, manager_id) VALUES (?,?,?,?,?,?,?)", test_info)
    connection.commit()
 
    print('\n' *2)
    wait_one = str(input("Press ENTER to continue): "))
    print('\n' *100)  

def find_user():
    conn()
    clearup()
    print('     *-*-* Here is a list of all users *-*-*')
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Phone":12}{"Email":6}')
    print(f'{"--":5}{"----------":15}{"---------":15}{"-----":12}{"-----":6}')
    rows = cursor.execute("SELECT user_id, first_name, Last_name, phone, email FROM People").fetchall()
    info_data =['ID', 'FIRST NAME', 'LAST NAME', 'PHONE', 'EMAIL']
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:<5}{info_data[1]:<15}{info_data[2]:<15}{info_data[3]:<12}{info_data[4]:6}')
        
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)  

def add_user():
    get_date()
    create_date = test_date
    clearup()
    conn()
   
    record = []
    print('     *-*-* Enter the NEW User Info *-*-*')
    print("")
    record.append(input("First   : \nLast    : \nPhone   : \neMail   : \nPassword: \x1B[4A"))
    print(f'{CLR}', end='')
    record.append(input("Last    : \nPhone   : \neMail   : \nPassword: \x1B[3A"))
    print(f'{CLR}', end='')
    record.append(input("Phone   : \neMail   : \nPassword: \x1B[2A"))
    print(f'{CLR}', end='')
    record.append(input("Mail    : \nPassword: \x1B[1A"))
    print(f'{CLR}', end='')
    record.append(input("Password: "))
    record.append(test_date)
    cursor.execute("INSERT INTO People (first_name, last_name, phone, email, password, create_date) VALUES(?, ?, ?, ?, ?, ?)", record)
    connection.commit()
    print(f'\nSUCCESS: People "{record[0]}" Successfully added!')
    connection.commit()

def add_test():
    conn()
    get_num_users()
    clearup()
    show_user_list()
    get_user_id()
 
    clearup()
    comp_list()
    global test_id
    global test_name
    global test_date
    global raw_score
    global competency
    global manager_id
    global test_dict
  
    test_dict = {
    1:"Computer Anatomy",
    2:"Data Types",
    3:"Variables",
    4:"Functions",
    5:"Boolean Logic",
    6:"Conditionals",
    7:"Loops",
    8:"Data Structures",
    9:"Lists",
    10:"Dictionaries",
    11:"Working with Files",
    12:"Exception Handling",
    13:"Quality Assurance",
    14:"OOP",
    15:"Recursion",
    16:"Databases",
    }
    
    while True:
        try:
            test_id = int(input("Which TEST would you like to take (1-16)?"))
            if 1 <= test_id <= 16:
                break
            raise ValueError()
        except ValueError:
            print("Choose a test # between 1 and 16.")
    
    for i, j in test_dict.items():
        if (i) == (test_id):
            test_name = (j)
            print(test_name)
        else:
            pass 

    raw_score = random.randint(50,100)
    if raw_score >= 59:
        competency = 1
    if raw_score >= 69:
        competency = 2
    if raw_score >= 79:
        competency = 3
    if raw_score >= 89:
        competency = 4
    
    now = datetime.now()
    test_date = now.strftime("%Y:%m:%d")
    
    clearup()
    print(f'{" " * 20}{"*-*-* Here is your Test Result *-*-*"}')
    print(f'{"TEST ID":9}{"TEST NAME":19}{"TEST DATE":12}{"RAW SCORE":11}{"COMPETENCY":12}{"MANAGER ID":10}')
    print(f'{"-------":9}{"---------":19}{"----------":12}{"---------":11}{"----------":12}{"----------":10}')
    print(f'{test_id:^9}{test_name:19}{test_date:12}{raw_score:^11}{competency:^12}{manager_id:^10}')
   
    test_info = (user_id,test_id,test_name,test_date,raw_score,competency,manager_id)
    cursor.execute("INSERT INTO Testdata (user_id, test_id, test_name, test_date, raw_score, competency, manager_id) VALUES (?,?,?,?,?,?,?)", test_info)
    connection.commit()
      
    print('\n' *2)
    wait_one = str(input("Press ENTER to continue): "))
    print('\n' *100)

def one_user_summary():
    conn()
    get_num_users()
    clearup()
    show_user_list()
    get_user_id()
    view_test_summary()

def one_user_all_tests():
    conn()
    get_num_users()
    clearup()
    show_user_list()
    get_user_id()
    clearup()
    view_user_tests()

def view_user_tests_ave():
    conn()
    get_num_users()
    clearup()
    show_user_list()
    get_user_id()
    clearup()
    id_user = user_id
    print('\n' *1) 
    print(f'{" " * 20}{"*-*-* Here are the Test Scores with the Average *-*-*"}')       
    print(f'{"First Name":14}{"Last Name":15}{" 1":<4}{" 2":<4}{" 3":<4}{" 4":<4}{" 5":<4}{" 6":<4}{" 7":<4}{" 8":<4}{" 9":<4}{"10":<4}{"11":<4}{"12":<4}{"13":<4}{"14":<4}{"15":<4}{"16":<4}{"AVE":<6}')
    print(f'{"----------":14}{"---------":15}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"---":<6}')
    rows = cursor.execute("SELECT * FROM People WHERE user_id = ?",(user_id,)).fetchall()
    info_data =['FIRST NAME', 'LAST NAME', 'C1', 'C2' 'C3', 'C4' 'C5', 'C6' 'C7', 'C8' 'C9', 'C10' 'C11', 'C12' 'C13', 'C14' 'C15', 'C16']
    for info_data in rows:
        list_of_values = (info_data[10],info_data[11],info_data[12],info_data[13],info_data[14],info_data[15],info_data[16],info_data[17],info_data[18],info_data[19],info_data[20],info_data[21],info_data[22],info_data[23],info_data[24],info_data[25])
        average_comp = sum(list_of_values)/len(list_of_values)
        average_comp = round(average_comp, 1)
        print(f'{info_data[1]:14}{info_data[2]:15}{info_data[10]:<4}{info_data[11]:<4}{info_data[12]:<4}{info_data[13]:<4}{info_data[14]:<4}{info_data[15]:<4}{info_data[16]:<4}{info_data[17]:<4}{info_data[18]:<4}{info_data[19]:<4}{info_data[20]:<4}{info_data[21]:<4}{info_data[22]:<4}{info_data[23]:<4}{info_data[24]:<4}{info_data[25]:<4}{average_comp:<6}')
     
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))  
    clearup()

def one_user_edit_info():
    show_user_list()
    get_user_id()
    clearup()
    edit_user_info()

def edit_onetest_oneuser():
    conn()
    show_user_list()
    get_user_id()
    clearup()       
    print('                  *-*-* Here are the Test Scores *-*-*')
    print(f"-" * 77)
    print(f'{"TEST DATA ID":14}{"ID":4}{"TEST NAME":19}{"DATE":12}{"RAW":5}{"COMPETENCY":12}{"MANAGER ID":6}')
    print(f'{"------------":14}{"--":4}{"---------":19}{"-----":12}{"---":5}{"----------":12}{"----------":6}')
    rows = cursor.execute("SELECT * FROM Testdata WHERE user_id = ?",(user_id,)).fetchall()
    info_data = []
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:^14}{info_data[2]:4}{info_data[3]:19}{info_data[4]:12}{info_data[5]:5}{info_data[6]:12}{info_data[7]:6}')
    print(f'{"------------":14}{"--":4}{"---------":19}{"-----":12}{"---":5}{"----------":12}{"----------":6}') 
    print(f'{"TEST DATA ID":14}{"ID":4}{"TEST NAME":19}{"DATE":12}{"RAW":5}{"COMPETENCY":12}{"MANAGER ID":6}')
    print("       ∆")
    print("       |")
    print("       |")
    print(f"-" * 77)
    print("")
    while True:
        try:
            test_data_id = int(input("         Enter the TEST DATA ID number? "))
            if 1 <= test_id <= 1000:
                break
            raise ValueError()
        except ValueError:
            print("         Choose a TEST DATA ID # from the list above.")  
            
        field = ''
        print('''\nWhat NEEDS to be UPDATED? )
        [T]Test Name  [D]Test Date  [R]Raw Score (1-100)  [C]Competency (0-4)  [M]Manager ID  [N]Nothing''')
        
        field = input().lower()
        field_value = ""
        new_value = ""
        
        fields_dict = {
            't':'test_name','d':'test_date','r':'raw_score','c':'competency','m':'manager_id'
        }
        
        if field in fields_dict.keys():
            field_value = fields_dict[field]
                  
        if field == 't':
            new_value = input('Please enter the correct Test Name: ')
            user = f'UPDATE Testdata SET test_name = ? WHERE test_data_id = {test_data_id};'
            cursor.execute(user, [new_value])
            break
        
        if field == 'd':
            new_value = input('Please enter the correct Test Date: ')
            user = f'UPDATE Testdata SET test_date = ? WHERE test_data_id = {test_data_id};'
            cursor.execute(user, [new_value])
            break
        
        if field == 'r':
            new_value = input('Please enter the correct Raw Score # (0-100): ')
            user = f'UPDATE Testdata SET raw_score = ? WHERE test_data_id = {test_data_id};'
            cursor.execute(user, [new_value])
            break
        
        if field == 'c':
            new_value = input('Please enter the correct Competency Score (0-4): ')
            user = f'UPDATE Testdata SET competency = ? WHERE test_data_id = {test_data_id};'
            cursor.execute(user, [new_value])
            break
    
        if field == 'm':
            new_value = input('Please enter the correct Manager ID #: ')
            user = f'UPDATE Testdata SET manager_id = ? WHERE test_data_id = {test_data_id};'
            cursor.execute(user, [new_value])
            break
                
        if field == 'n':
            return
        if field == '':
            return   
    connection.commit()
        
    print('                  *-*-* Here is the Change Verification *-*-*')
    print(f"-" * 77)
    print(f'{"TEST DATA ID":14}{"ID":4}{"TEST NAME":19}{"DATE":12}{"RAW":5}{"COMPETENCY":12}{"MANAGER ID":6}')
    print(f'{"------------":14}{"--":4}{"---------":19}{"-----":12}{"---":5}{"----------":12}{"----------":6}')
    rows = cursor.execute("SELECT * FROM Testdata WHERE test_data_id = ?",(test_data_id,)).fetchall()
    info_data = []
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:^14}{info_data[2]:4}{info_data[3]:19}{info_data[4]:12}{info_data[5]:5}{info_data[6]:12}{info_data[7]:6}')

    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)

def delete_onetest_oneuser():
    connection = sqlite3.connect('competency_tracker.db')
    cursor = connection.cursor()
    get_user_id() 
    clearup()       
    print('                  *-*-* Here are the Tests *-*-*')
    print(f"-" * 77)
    print(f'{"TEST DATA ID":14}{"ID":4}{"TEST NAME":19}{"DATE":12}{"RAW":5}{"COMPETENCY":12}{"MANAGER ID":6}')
    print(f'{"------------":14}{"--":4}{"---------":19}{"-----":12}{"---":5}{"----------":12}{"----------":6}')
    rows = cursor.execute("SELECT * FROM Testdata WHERE user_id = ?",(user_id,)).fetchall()
    info_data = []
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:^14}{info_data[2]:4}{info_data[3]:19}{info_data[4]:12}{info_data[5]:5}{info_data[6]:12}{info_data[7]:6}')
    print(f'{"------------":14}{"--":4}{"---------":19}{"-----":12}{"---":5}{"----------":12}{"----------":6}') 
    print(f'{"TEST DATA ID":14}{"ID":4}{"TEST NAME":19}{"DATE":12}{"RAW":5}{"COMPETENCY":12}{"MANAGER ID":6}')
    print("       ∆")
    print("       |")
    print("       |")
    print(f"-" * 77)
    print("")
  
    query = f'DELETE FROM Testdata WHERE test_data_id = ?'
    delete_test = int(input("         Enter the TEST DATA ID number to be *DELETED* "))
    cursor.execute(query, [delete_test])
    connection.commit()
    
    print("         Choose a TEST DATA ID # from the list above.")    
    print('                  *-*-* The Test has been DELETED *-*-*') 
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)    

def view_all_user_info():
    conn()
    print('     *-*-* Here is all Current Personal Data *-*-*')
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Phone":12}{"Email":6}')
    print(f'{"--":5}{"----------":15}{"---------":15}{"-----":12}{"-----":6}')
    rows = cursor.execute("SELECT user_id, first_name, Last_name, phone, email FROM People ",).fetchall()
    info_data =['ID', 'FIRST NAME', 'LAST NAME', 'PHONE', 'EMAIL']
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:<5}{info_data[1]:<15}{info_data[2]:<15}{info_data[3]:<12}{info_data[4]:6}')
        
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)  

def all_users_take_one_test():
    conn()
    comp_list()
    global test_id
    global test_name
    global test_date
    global raw_score
    global competency
    global manager_id
    
    test_dict = {
    1:"Computer Anatomy",
    2:"Data Types",
    3:"Variables",
    4:"Functions",
    5:"Boolean Logic",
    6:"Conditionals",
    7:"Loops",
    8:"Data Structures",
    9:"Lists",
    10:"Dictionaries",
    11:"Working with Files",
    12:"Exception Handling",
    13:"Quality Assurance",
    14:"OOP",
    15:"Recursion",
    16:"Databases",
    }
    
    while True:
        try:
            test_id = int(input("Which TEST to take (1-16)?"))
            if 1 <= test_id <= 16:
                break
            raise ValueError()
        except ValueError:
            print("Choose a test # between 1 and 16.")
    
    for i, j in test_dict.items():
        if (i) == (test_id):
            test_name = (j)
            print(test_name)
        else:
            pass 
    print('\n' *100)
    print(f'{" " * 25}{"*-*-* Here is the Test Results *-*-*"}')
    print(f'{"USER ID":9}{"TEST ID":9}{"TEST NAME":19}{"TEST DATE":12}{"RAW SCORE":11}{"COMPETENCY":12}{"MANAGER ID":10}')
    print(f'{"-------":9}{"-------":9}{"---------":19}{"----------":12}{"---------":11}{"----------":12}{"----------":10}')
    
    user = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]    
    for x in user:  
        user_id = x       
        
        raw_score = random.randint(50,100)
        if raw_score >= 59:
            competency = 1
        if raw_score >= 69:
            competency = 2
        if raw_score >= 79:
            competency = 3
        if raw_score >= 89:
            competency = 4
        
        now = datetime.now() 
        test_date = now.strftime("%Y:%m:%d")
        
        print(f'{user_id:^9}{test_id:^9}{test_name:19}{test_date:12}{raw_score:^11}{competency:^12}{manager_id:^10}')
        test_info = (user_id,test_id,test_name,test_date,raw_score,competency,manager_id)
        cursor.execute("INSERT INTO Testdata (user_id, test_id, test_name, test_date, raw_score, competency, manager_id) VALUES (?,?,?,?,?,?,?)", test_info)
        connection.commit()
       
        
    print('\n' *2)
    wait_one = str(input("Press ENTER to continue): "))
    print('\n' *100)   
 
def all_users_test_summary():
    conn()
    clearup()
    comp_list()
    print(f'{" " * 24}{"*-*-* Here are the Test Competencies *-*-*"}')
    print(f"-" * 91)
    print(f'{"First Name":15}{"Last Name":15}{" 1":4}{" 2":4}{" 3":4}{" 4":4}{" 5":4}{" 6":4}{" 7":4}{" 8":4}{" 9":4}{"10":4}{"11":4}{"12":4}{"13":4}{"14":4}{"15":4}{"16":4}')
    print(f'{"----------":15}{"---------":15}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}{"--":4}')
    rows = cursor.execute("SELECT * FROM People").fetchall()
    info_data =['FIRST NAME', 'LAST NAME', 'C1', 'C2' 'C3', 'C4' 'C5', 'C6' 'C7', 'C8' 'C9', 'C10' 'C11', 'C12' 'C13', 'C14' 'C15', 'C16']
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[1]:15}{info_data[2]:15}{info_data[10]:4}{info_data[11]:4}{info_data[12]:4}{info_data[13]:4}{info_data[14]:4}{info_data[15]:4}{info_data[16]:4}{info_data[17]:4}{info_data[18]:4}{info_data[19]:4}{info_data[20]:4}{info_data[21]:4}{info_data[22]:4}{info_data[23]:4}{info_data[24]:4}{info_data[25]:4}')
        
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))
    print('\n' *100)       

def all_users_average_test_summary():
    
    conn()

    comp_list()
    print(f'{" " * 24}{"*-*-* Here are the Test Competencies *-*-*"}')
    print(f"-" * 91)
    print(f'{"First Name":14}{"Last Name":15}{" 1":<4}{" 2":<4}{" 3":<4}{" 4":<4}{" 5":<4}{" 6":<4}{" 7":<4}{" 8":<4}{" 9":<4}{"10":<4}{"11":<4}{"12":<4}{"13":<4}{"14":<4}{"15":<4}{"16":<4}{"AVE":<6}')
    print(f'{"----------":14}{"---------":15}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"--":<4}{"---":<6}')
    rows = cursor.execute("SELECT * FROM People").fetchall()
    info_data =['FIRST NAME', 'LAST NAME', 'C1', 'C2' 'C3', 'C4' 'C5', 'C6' 'C7', 'C8' 'C9', 'C10' 'C11', 'C12' 'C13', 'C14' 'C15', 'C16']
    for info_data in rows:
        list_of_values = (info_data[10],info_data[11],info_data[12],info_data[13],info_data[14],info_data[15],info_data[16],info_data[17],info_data[18],info_data[19],info_data[20],info_data[21],info_data[22],info_data[23],info_data[24],info_data[25])
        average_comp = sum(list_of_values)/len(list_of_values)
        average_comp = round(average_comp, 1)
        print(f'{info_data[1]:14}{info_data[2]:15}{info_data[10]:<4}{info_data[11]:<4}{info_data[12]:<4}{info_data[13]:<4}{info_data[14]:<4}{info_data[15]:<4}{info_data[16]:<4}{info_data[17]:<4}{info_data[18]:<4}{info_data[19]:<4}{info_data[20]:<4}{info_data[21]:<4}{info_data[22]:<4}{info_data[23]:<4}{info_data[24]:<4}{info_data[25]:<4}{average_comp:<6}')
        
    print('\n' *2)
    wait_one = str(input("(Press ENTER to continue): "))

def csv_to_db():
    connection = sqlite3.connect("competency_tracker.db")
    cursor = connection.cursor()
    with open('midterm_test_data_file.csv','r') as file:
        data = csv.DictReader(file)
        user_info = [(i['user_id'], i['test_id'], i['test_name'], i['test_date'], i['raw_score'], i['competency'], i['manager_id']) for i in data]
        print(user_info)   
        
        cursor.executemany("INSERT INTO Testdata (user_id, test_id, test_name, test_date, raw_score, competency, manager_id) VALUES (?,?,?,?,?,?,?)", user_info)
        connection.commit()
    connection.close()

def db_people_to_csv():
    clearup()
    try:
        conn()
        print("Exporting People data into CSV............")
        cursor.execute("SELECT * FROM People")
        with open("people_data.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "/people_data.csv"

    except Error as e:
        print(e)
    finally:
        connection.close()
        
    print('\n' * 2)
    print("people_data.csv exported Successfully")
    wait_one = str(input("(Press ENTER to continue): "))
    clearup()
      
def db_test_to_csv():
    clearup()
    try:
        conn()
        print("Exporting Test data into CSV............")
        cursor.execute("SELECT * FROM Testdata")
        with open("test_data.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=",")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "/test_data.csv"

    except Error as e:
        print(e)
    finally:
        connection.close()
        
    print('\n' * 2)
    print("test_data.csv exported Successfully")
    wait_one = str(input("(Press ENTER to continue): "))
    clearup()

def report_one_user_info():
    get_user_id()
    get_banner()
    view_user_info()

def report_one_user_summary():
    get_user_id()
    get_banner()
    view_test_summary() 

def report_all_users_summary():
    get_banner()
    all_users_average_test_summary()

def make_conn(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return connection

def conn():
    connection = sqlite3.connect('competency_tracker.db')
    cursor = connection.cursor()

def get_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM People")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
               
def view_rows(rows):
    connection = sqlite3.connect('competency_tracker.db')
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * FROM People").fetchall()
   
    for row in rows:
        print(f'{row[0]:<5}{row[1]:<25}{row[2]:<29}{row[3]:<17}{row[4]:<7}{row[5]:<10}{row[6]:<14}{row[7]:<7}')

def rand_user():
    current_user_id = 0
    current_user_id = random.randint(1, 6)
    
def comp_list():
    print(f'{" " * 33}{"*-*-* Test Name Key *-*-*"}')
    print("")
    print(f"-" * 91)
    print(" 1:Computer Anatomy    2:Data Types     3:Variables            4:Functions 05:Boolean Logic")
    print(" 5:Boolean Logic       6:Conditionals   7:Loops                8:Data Structures         ")
    print(" 9:Lists              10:Dictionaries  11:Working with Files  12:Exception Handling ")
    print("13:Quality Assurance  14:OOP           15:Recursion           16:Databases")
    print(f"-" * 91)
    print("")
 
def get_score():
    raw_score = random.randint(50, 100)
    
def get_comp():  
    if raw_score < 60:
        competency = 0
    if raw_score < 59:
        competency = 1
    if raw_score < 69:
        competency = 2
    if raw_score < 79:
        competency = 3
    if raw_score < 89:
        competency = 4
        
def get_user_id():
    global user_id
    global id_user
    while True:
        try:
            user_id = int(input("Enter the USER's ID? "))
            if 1 <= user_id <= 13:
                break
            raise ValueError()
        except ValueError:
            print("Enter the USER's ID?. ")
            clearup()
            
def get_banner():
    global test_date
    global now
    get_date()
    clearup()
    report_banner = [
        u"\u001b[32;1m"
    "    ╔═════════════════════════════════════════════════════╗",
    "    ║ ╔═════════════════════════════════════════════════╗ ║",
    "    ║ ║  RRRRR   EEEEE   PPPPP   OOOOO   RRRRR   TTTTT  ║ ║",
    "    ║ ║  R   R   E       P   P   O   O   R   R     T    ║ ║",
    "    ║ ║  RRRRR   EEEEE   PPPPP   O   O   RRRRR     T    ║ ║",
    "    ║ ║  R R     E       P       O   O   R R       T    ║ ║",
    "    ║ ║  R   R   EEEEE   P       OOOOO   R   R     T    ║ ║",
    "    ║ ╚═════════════════════════════════════════════════╝ ║",
    "    ╚═════════════════════════════════════════════════════╝"
    ]
    for i in range(9):
        print(report_banner[i])
    
    print(f'{" " * 20}{"DATE: "}{test_date}')
    print("\u001b[0m")
    
def get_date():
    
    global test_date
    global now
    now = datetime.now() 
    test_date = now.strftime("%Y:%m:%d")
    
def  get_test_names():
    test_dict = {
    1:"Computer Anatomy",
    2:"Data Types",
    3:"Variables",
    4:"Functions",
    5:"Boolean Logic",
    6:"Conditionals",
    7:"Loops",
    8:"Data Structures",
    9:"Lists",
    10:"Dictionaries",
    11:"Working with Files",
    12:"Exception Handling",
    13:"Quality Assurance",
    14:"OOP",
    15:"Recursion",
    16:"Databases",
    }
    
def cal_average(num):
    sum_num = 0
    for t in num:
        sum_num = sum_num + t           

    avg = sum_num / len(num)
    return avg

def get_num_users():  
    conn()
    print("Count of Rows")
    cursor.execute("SELECT * FROM People")
    num_users = (len(cursor.fetchall()))
    connection.commit()
    
def show_user_list():
    print('     *-*-* Here is a list of all users *-*-*')
    print(f'{"ID":5}{"First Name":15}{"Last Name":15}{"Phone":12}')
    print(f'{"--":5}{"----------":15}{"---------":15}{"-----":12}')
    rows = cursor.execute("SELECT user_id, first_name, Last_name, phone FROM People").fetchall()
    info_data =['ID', 'FIRST NAME', 'LAST NAME', 'PHONE', 'EMAIL']
    for info_data in rows:
        info_data = [str(info) for info in info_data]
        print(f'{info_data[0]:<5}{info_data[1]:<15}{info_data[2]:<15}{info_data[3]:<12}')
        
    print('\n' *2)

def clearup():
    print('\n' *50) 

while True:
         
    if view == 2:
        login_input = ""
        user_input = ""
        manager_view()
        manager_input = str(input("What would you like to do?: "))
        clearup()
        
        if manager_input == '1': 
            find_user()

        if manager_input == '2':
            add_user()

        if manager_input == '3':
            add_test()

        if manager_input == '4':
            one_user_summary()

        if manager_input == '5':
            one_user_all_tests()

        if manager_input == '6':
            view_user_tests_ave()

        if manager_input == '7':
            one_user_edit_info()

        if manager_input == '8':
            edit_onetest_oneuser()

        if manager_input == '9':
            delete_onetest_oneuser()

        if manager_input == '10':
            pass

        if manager_input == '11':
            view_all_user_info()

        if manager_input == '12':
            all_users_test_summary()
            
        if manager_input == '13':
            all_users_take_one_test()

        if manager_input == '14':
            all_users_test_summary()

        if manager_input == '15':
            all_users_average_test_summary()

        if manager_input == '16':
            pass

        if manager_input == '17':
            clearup()
            print("     [P]-People Data or [T]-Test Data")
            print('\n' *2)
            export_input = str(input(f'{" " * 5}{"Which CSV export do you want?"}')) 
            export_input = export_input.upper()
            if export_input == "P":
                db_people_to_csv()
            if export_input == "T":
                db_test_to_csv()

        if manager_input == '18':
            report_one_user_info()

        if manager_input == '19':
            report_one_user_summary()
            
        if manager_input == '20':
            report_all_users_summary()
            
        if manager_input == 'q':
            view = 0
            break
        
        if manager_input == '00':
            view = 0
            user_id = 0
            manager = 6
            clearup()
            continue
  
    if view == 1:
        login_input = ""
        user_view()
        user_input = str(input("What would you like to do?: "))
        user_input = user_input.upper()
        
        if user_input == 'A':
            view_user_info()
    
        if user_input == 'B':
            edit_user_info()
        
        if user_input == 'C':
            view_user_tests()
        
        if user_input == 'D':
            view_test_summary()
        
        if user_input == 'E':
            take_test()
        
        if user_input == 'L':
            view = 0
            user_id = 0
            clearup()
            continue

    if view == 0:
        login_view()
        print('\n' *2)
        record = [] 
        print(f'{" " * 13}{"*-*-* Please LOGIN *-*-*"}')
        print('\n' *2)
        email = (input("eMail   : \nPassword: \x1B[1A"))
        print(f'{CLR}', end='')
        password = (input("Password: "))
        
        connection = sqlite3.connect("competency_tracker.db")
        cursor = connection.cursor()
        query = 'SELECT * FROM People WHERE email = ? AND password = ?'
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        
        if not result:
            print("Login failed")

        else:
            print("Welcome, Logging in ...")
            user_id = result[0]
            first_name = result[1]
            last_name = result[2]
            phone = result[3]
            email = result[4]
            password = result[5]
            active = result[6]
            create_date = result[7]
            hire_date = result[8]
            manager = result[9]
    
            if result[9] == 1:
                view = 2
                manager_id = result[0]

            else:
                view = 1  

print('\n' *100)
print("                       Good Bye")
print('\n' *5)
