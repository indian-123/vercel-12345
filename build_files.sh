# build_files.sh
echo "build.."
python3.9 -m pip install -r requirements.txt
echo "make migration ...."
python3.9 manage.py makemigrations
echo "migrate........................................."
python3.9 manage.py migrate

echo "collect staic  .."
python3.9 manage.py collectstatic --noinput --clear

