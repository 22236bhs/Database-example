'''Olly Kitchingman- fighter plane database application'''
#imports
import sqlite3

#constants
DATABASE = "fighters.db"
EXITNUM = "7"

#functions
def print_all_aircraft(order=None):
    '''print all the aircraft nicely'''
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        if order is None:
            sql = "SELECT * FROM fighter;"
        else:
            sql = f"SELECT * FROM fighter ORDER BY {order} DESC"
        cursor.execute(sql)    
        results = cursor.fetchall()
        #loop throught all of the results
        print(f"{"name":<30}{"speed":<8}{"max_g":<8}{"climb":<8}{"range":<8}{"payload":<8}")
        for data in results:
            print(f"{data[1]:<30}{data[2]:<8}{data[3]:<8}{data[4]:<8}{data[5]:<8}{data[6]:<8}")




#main code

while True:
    user_input = input(f"""\nWhat would you like to do?
1. Print all aircraft
2. Print all aircraft by order of speed
3. Print all aircraft by order of max_g
4. Print all aircraft by order of climb
5. Print all aircraft by order of range
6. Print all aircraft by order of payload
{EXITNUM}. Exit\n\n""")
    try:
        if user_input == "1":
            print_all_aircraft()
        elif user_input == "2":
            print_all_aircraft("speed")
        elif user_input == "3":
            print_all_aircraft("max_g")
        elif user_input == "4":
            print_all_aircraft("climbrate")
        elif user_input == "5":
            print_all_aircraft("range")
        elif user_input == "6":
            print_all_aircraft("payload")
        elif user_input == EXITNUM:
            break
        else:
            print("Invalid input")
    except:
        print("Invalid input")