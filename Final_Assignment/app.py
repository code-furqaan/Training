# import pyodbc as db
from dbutils import result_as_dict
from db_connector import DBConnector
from command_functions import command_functions

def shell():
    db = DBConnector()

    while True:
        print()
        user_input = input("db> ")
        parts = user_input.split(' ')
        command = parts[0]
        arguments = parts[1:]
        try:
            if command.lower() in ["quit", "exit", "bye"]:
                break
            db.execute(command, arguments)
            
        except Exception as e:
            print("Command not recognized.")
            print(e)
    pass

def main():
    print('\nRun \'help\' for the list of executable commands')
    shell()

if __name__=='__main__':
    main()
