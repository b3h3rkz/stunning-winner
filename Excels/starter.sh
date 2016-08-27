pip install virtualenv
virtualenv -p python3.4 .
source bin/activate
pip install --upgrade setuptools
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser  


