import requests
from faker import Faker
import urllib3


fake = Faker()
session = requests.Session()
urllib3.disable_warnings()
for i in range(1000):
    name, password, email, address = fake.name(), fake.password(), fake.email(), fake.address()
    response = session.get(
        'https://localhost:8443/index.html?username={}?password?={}?email={}?address={}'.format(
            name,
            password,
            email,
            address,
        ),
        verify=False,
    )
    print('-----------------------------')
    if response.status_code == 200:
        print('User: {}, Password: {}, Email: {}, Address: {}'.format(
            name,
            password,
            email,
            address
        ))
    else:
        print(response.text)
