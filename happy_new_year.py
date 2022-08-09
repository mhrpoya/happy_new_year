from cgi import print_environ
from time import sleep

from click import echo

item = 1
wid = 50
wid_2 = 80
party = "\U0001f973"

for _ in range(15):
    echo((party * item).center(wid))
    item += 2
    sleep(0.5)

echo("/ HAPPY NEW YEAR \\".center(wid_2))
echo("\ 2022 /".center(wid_2))

for _ in range(16, 0, -1):
    echo((party * item).center(wid))
    item -= 2
    sleep(0.5)