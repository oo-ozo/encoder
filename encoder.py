import base64 as b6
import os

os.system('clear')
print("""
[1] Normal encode

[2] Secure Encode <pro>

""")
inp = input("enter your choice>")
if inp == "1":
    inf = input("Enter file that you want to encode~>")
    ino = input("Enter file that you want tk set output~>")
    with open(inf, 'r') as i:
        text = i.read()
    tb = b6.b64encode(text.encode('ascii'))

    tbc = tb.decode('ascii')

    with open(ino , 'w+') as w:
        w.write("""import base64 as b6
wb = \"\"\"
{0}
\"\"\".encode('ascii')
exec(b6.b64decode(wb))
""".format(tbc))
    print("encode success")

elif inp == "2":
    print("""
if you want secure encode tool come my messanger 
<https://m.me/nicky.jame.py> and cost=1000MMK
""")
