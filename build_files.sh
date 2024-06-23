echo " BUILD START"
# Install dependencies
pip install -r requirement.txt

# Collect static files
python manage.py collectstatic --noinput --clear

# Migrate the database
python manage.py migrate

echo " BUILD END"
