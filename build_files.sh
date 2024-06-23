echo " BUILD START"
# Install dependencies
python3.11.7 -m pip install -r requirement.txt

# Collect static files
python3.11.7 manage.py collectstatic --noinput --clear

# Migrate the database
python3.11.7 manage.py migrate

echo " BUILD END"
