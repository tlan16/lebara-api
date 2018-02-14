# lebara-api
Get account info from lebara official website.

# Usage
```python
from lebara_api import LebaraApi

username = 'username'
password = 'password'

lebara = LebaraApi(username, password)
lebara.login()
print(lebara.getAccountSummery())
```

# Installation
```bash
pip install -U lebara-api
```

# Command-line interface
```
usage: lebara-api [-h] [-u USERNAME] [-p PASSWORD]

lebara cli.

optional arguments:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        your lebara username
  -p PASSWORD, --password PASSWORD
                        your lebara username
```
