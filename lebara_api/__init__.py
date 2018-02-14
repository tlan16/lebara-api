import requests
from bs4 import BeautifulSoup


class LebaraApi:
    # class variable
    username = ''
    password = ''
    csrfToken = ''
    session = requests.session()
    summary = {}

    # class concstants
    loginPageUrl = 'https://secure2.lebara-mobile.com.au/customer/login'
    csrfSelector = '#login-form > input[type="hidden"]'
    accountSummarySelector = '#account-summary > tbody'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.csrfToken = self.getCsrfToken()

    def getCsrfToken(self):
        response = self.session.get(self.loginPageUrl)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrfToken = soup.select_one(self.csrfSelector)['value']
        return csrfToken

    def login(self):
        payload = {
            'csrfToken': self.csrfToken,
            'user_name': self.username,
            'user_password': self.password,
        }
        response = self.session.post(self.loginPageUrl, data=payload)

        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select_one(self.accountSummarySelector)
        rows = table.findChildren('tr')
        for row in rows:
            title = row.select_one('th').text
            self.summary[title] = []
            for cell in row.findChildren('td'):
                self.summary[title].append(cell.text)

        return self

    def getAccountSummery(self):
        return self.summary
