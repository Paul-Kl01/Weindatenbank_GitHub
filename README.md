# Weindatenbank_GitHub

## Installlieren:
pip install flask \
pip install psycopg2 \
pip install psycopg2-binary \
pip install flask-sqlalchemy \
\
ALternativ:\
pip install -r Dateipfad\requirements.txt

# Datenbank erstellen: 
python \
from app import db \
db.create_all() \
exit()