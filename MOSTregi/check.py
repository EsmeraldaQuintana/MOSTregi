import sys
from pathlib import Path

intake = sys.argv[1]
string = "" + intake
if Path(string).is_file() is True:
	print ("This does exist!")
else:
	print ("This does not exist!")

