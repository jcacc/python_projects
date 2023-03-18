import pyodbc

# Set up the database connection
server = 'CHOMPYIII\SQLEXPRESS'
database = 'tripReports'
driver = '{SQL Server}' # You may need to modify the driver name based on your setup
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};DATABASE={database}')

# Define the schema for the trip report
report_schema = {
    'date': 'date',
    'substance': 'varchar(255)',
    'dosage': 'float',
    'duration': 'varchar(50)',
    'notes': 'text'
}

# Create a table for the trip reports if it doesn't already exist
# with conn.cursor() as cursor:
#     table_name = 'trip_reports'
#     cursor.execute(f"IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='{table_name}' AND xtype='U') CREATE TABLE {table_name} (id INT IDENTITY(1,1) PRIMARY KEY, {','.join(f'{k} {v}' for k, v in report_schema.items())})")

# Define a function to insert a new trip report into the database
def add_trip_report(date, substance, dosage, duration, notes):
    with conn.cursor() as cursor:
        insert_query = f"INSERT INTO trip_reports (date, substance, dosage, duration, notes) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (date, substance, dosage, duration, notes))
        conn.commit()

# Define a function to view past trip reports
def view_trip_reports():
    with conn.cursor() as cursor:
        select_query = f"SELECT * FROM trip_reports ORDER BY date DESC"
        cursor.execute(select_query)
        rows = cursor.fetchall()
        for row in rows:
            print(f"Date: {row.date} | Substance: {row.substance} | Dosage (mg): {row.dosage} | Duration: {row.duration} | Notes: {row.notes}\n")

# Define a function to display the menu options
def display_menu():
    print("Greetings ")
    
    print("1. Enter a new trip report")
    print("2. View past trip reports")
    print("3. Exit")

# Prompt the user to enter a menu option
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        # Prompt the user to enter a new trip report
        date = input("Enter the date of your trip (YYYY-MM-DD): ")
        substance = input("Enter the name of the substance you took: ")
        dosage = float(input("Enter the dosage in milligrams: "))
        duration = input("Enter the duration of the trip (ex: 4h20m): ")
        notes = input("Enter any notes about your trip: ")
        
        # Add the new trip report to the database
        add_trip_report(date, substance, dosage, duration, notes)
        print("Trip report added!\n")
        
    elif choice == '2':
        # View past trip reports
        view_trip_reports()
        
    elif choice == '3':
        # Exit the program
        break
        
    else:
        print("Invalid choice. Please try again.\n")

# Close the database connection
conn.close()