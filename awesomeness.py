str = """Sryvcr pntbh.
Qbhtynf unq gb cbbc, uvf ohgg jnf nyy fgvaxl orpnhfr ur unq gb cbbc fb onqyl.
Gurer jnf n tebff jbzna anzrq Erorppn jub jnf fhaonguvat nyy anxrq naq fur jnf sng.
Qbhtynf jnyxrq hc gb ure naq fnvq, V arrq gb cbbc. 
Bxnl, Erorppn ercyvrq, V yvxr cbbc. Qbhtynf fdhnggrq qbja bire gur sng fhaonguvat ynql naq jrag cbbc.
Gur cbbc fng gurer ba Erorppnf obbof, ybbxvat yvxr n jrvare."""


rot13 = {}
for c in (65,97):
	for i in range(26):
		rot13[chr(i+c)] = chr((i+13)%26+c)

print "".join([rot13.get(c,c) for c in str])