from unittest import TestCase
from dotenv import load_dotenv
from os.path import join, dirname
from os import environ
from lebara_api import LebaraApi

dotenv_path = join(dirname(__file__), '../../', '.env')
load_dotenv(dotenv_path)


class TestLebaraApi(TestCase):
    def test_get_account_info(self):
        username = environ.get('lebara-username')
        password = environ.get('lebara-password')

        self.assertNotEquals(len(username), 0)
        self.assertNotEquals(len(password), 0)

        lebara = LebaraApi(username, password)
        lebara.login()

        account_summary = lebara.getAccountSummery()

        self.assertNotEquals(len(account_summary), 0)
