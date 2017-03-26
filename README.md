# certponto-bot
Automating the boring stuff

## Quick start

```bash
# Install the python-selenium package
sudo dnf install python2-selenium -y              # Fedora 24 and 25

# Install the selenium python client and the java server [1]
pip install -U selenium
java -jar selenium-server-standalone-2.7.0.jar    # Release and version may vary

# Open the bateponto.py file and add your credentials
cpf 		= "YOUR CPF GOES HERE"
password	= "YOUR PASSWORD GOES HERE"
date 		= "DATE WORKED GOES HERE"

# Run it
python bateponto.py

[1] Reference: https://pypi.python.org/pypi/selenium/2.7.0
