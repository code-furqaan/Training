import pyodbc as db
from command_functions import command_functions

class DBConnector:
    def __init__(self):
        driver='{ODBC Driver 17 for SQL Server}'
        server=r'localhost'
        database='library_db'
        encrypt='no'
        trusted_connection='yes'

        connection_string=f'''
            DRIVER={driver};
            SERVER={server};
            DATABASE={database};
            trusted_connection={trusted_connection};
            ENCRYPT={encrypt};
        '''
        self.connection_string = connection_string

    
    def execute(self, command, arguments):
         if command.lower() in 'help':
                command_functions[command.lower()](command_functions)
                return
         with db.connect(self.connection_string) as connection:
                cursor= connection.cursor()
                command_functions[command.lower()](cursor,*arguments)


    


    