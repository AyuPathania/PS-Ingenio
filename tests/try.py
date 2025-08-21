from faker import Faker
fake = Faker()

print(fake.credit_card_number(card_type="visa"))
print(fake.credit_card_expire())
print(fake.credit_card_security_code(card_type="visa"))
print(fake.postcode())
