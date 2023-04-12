import csv
import random
from fake_data import Faker

fake = Faker()

# Define the number of sample orders
num_orders = 100

# Define possible values for t-shirts
sizes = ['S', 'M', 'L', 'XL', 'XXL']
colors = ['Red', 'Blue', 'Green', 'Yellow', 'White', 'Black', 'Gray']
styles = ['Round Neck', 'V-Neck', 'Long Sleeve', 'Hoodie', 'Crewneck']
tv_shows = ['Breaking Bad', 'Friends', 'Game of Thrones', 'The Office', 'Stranger Things']

# Define possible values for fulfillment types
fulfillment_types = ['pickup', 'shipping']

# Create and write to a CSV file
with open('sample_orders.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['order_id', 'customer_name', 'email', 'phone', 'address', 'size', 'color', 'style', 'tv_show', 'quantity', 'price', 'fulfillment_type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(num_orders):
        writer.writerow({
            'order_id': i + 1,
            'customer_name': fake.name(),
            'email': fake.email(),
            'phone': fake.phone_number(),
            'address': fake.address().replace('\n', ', '),
            'size': random.choice(sizes),
            'color': random.choice(colors),
            'style': random.choice(styles),
            'tv_show': random.choice(tv_shows),
            'quantity': random.randint(1, 5),
            'price': '{:.2f}'.format(random.uniform(15, 50)),
            'fulfillment_type': random.choice(fulfillment_types)
        })
