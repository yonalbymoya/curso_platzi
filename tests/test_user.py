import unittest
from faker import Faker
from src.user import User

class UserTests(unittest.TestCase):

    def setUp(self):
        self.faker = Faker(locale="es")

    def test_user_create(self):
        name_generate = self.faker.name()
        email_generate = self.faker.email()
        user = User(name=name_generate, email=email_generate)
        self.assertEqual(user.name, name_generate)
        self.assertEqual(user.email, email_generate)