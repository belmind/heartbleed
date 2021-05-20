import requests
from faker import Faker
import urllib3
import random


fake = Faker()
session = requests.Session()
urllib3.disable_warnings()
actions = ['login', 'payment']

for _ in range(1000):
    action = random.choice(actions)
    print('-----------------------------')
    if action == 'login':
        email = fake.email()
        password = fake.password()
        response = session.get(
            'https://localhost:8443/index.html?email={}?password?={}'.format(
                email,
                password,
            ),
            verify=False,
        )
        print('Action: {}, Email: {}, Password: {}'.format(action, email, password))
    elif action == 'payment':
        name = fake.name()
        address = fake.address()
        card_number = fake.credit_card_number()
        expiry = fake.credit_card_expire()
        ccv = fake.credit_card_security_code()
        response = session.get(
            'https://localhost:8443/index.html?name={}?address={}?card_number={}?expiry={}?CCV={}'.format(
                name,
                address,
                card_number,
                expiry,
                ccv,
            ),
            verify=False,
        )
        print("""Action: {}, Name: {}, Address: {}, Credit Card Number: {}, \n
            Expiry: {}, CCV: {}""".format(
                action,
                name,
                address,
                card_number,
                expiry,
                ccv
            )
        )
