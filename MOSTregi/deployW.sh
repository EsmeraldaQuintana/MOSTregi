echo "==============================================" &&
echo "  makemigrations                             |" &&
echo "==============================================" &&
py manage.py makemigrations &&
echo "==============================================" &&
echo "  migrate                                    |" &&
echo "==============================================" &&
py manage.py migrate &&
echo "==============================================" &&
echo "  test (exclude unfinished)                  |" &&
echo "==============================================" &&
py manage.py test --exclude-tag=unfinished &&
echo "==============================================" &&
echo "  runserver                                  |" &&
echo "==============================================" &&
py manage.py runserver
