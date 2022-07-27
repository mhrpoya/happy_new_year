from time import sleep

from click import echo

item = 1
wid = 50

for _ in range(15):
    echo(("+" * item).center(wid))
    item += 2
    sleep(0.5)

echo("| HAPPY NEW YEAR |".center(wid))
echo("\ 2022 /".center(wid))

for _ in range(16, 0, -1):
    echo(("+" * item).center(wid))
    item -= 2
    sleep(0.5)