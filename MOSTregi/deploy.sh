echo "==============================================" &&
echo "  makemigrations                             |" &&
echo "==============================================" &&
python3 manage.py makemigrations &&
echo "==============================================" &&
echo "  migrate                                    |" &&
echo "==============================================" &&
python3 manage.py migrate &&
echo "==============================================" &&
echo "  test (exclude unfinished)                  |" &&
echo "==============================================" &&
python3 manage.py test --exclude-tag=unfinished &&
echo "==============================================" &&
echo "  runserver                                  |" &&
echo "==============================================" &&
python3 manage.py runserver
