import Faker
import random

fake = Faker()

# List of departments and positions
departments = ['Marketing', 'Sales', 'HR', 'Finance', 'IT']
positions = ['Manager', 'Director', 'Specialist', 'Analyst', 'Coordinator']

# List of states
states = ['Ohio', 'Kentucky']

# Generate data for 150 employees
for i in range(150):
    # Generate name, email, and phone
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    
    # Randomly assign department and position
    department = random.choice(departments)
    position = random.choice(positions)
    
    # Randomly assign state and generate city and address
    state = random.choice(states)
    city = fake.city()
    address = fake.street_address()
    
    # Print employee information
    print(f'{name}, {email}, {phone}, {department}, {position}, {city}, {state}, {address}')
