str = """Znzba nqbezrprh.
R b eranfpvzragb qn pevnghen qvffrzvabh-fr cryn green r frhf frthvqberf gbeanenz-fr rkrepvgbf.
R ryrf ncertbnenz n zrafntrz r fnpevsvpnenz ynibhenf pbz sbtb, pbz n nfghpvn qnf encbfnf.
R ryrf pevnenz hz abib zhaqb n fhn vzntrz r frzryunapn pbasbezr cebzrgvqb cryb grkgb fntenqb r pbagnenz qn pevnghen cnen fhnf pevnapnf.
Znzba qrfcregbh r, irwn fb, anqn znvf ren qb dhr hz qvfpvchyb."""


rot13 = {}
for c in (65,97):
	for i in range(26):
		rot13[chr(i+c)] = chr((i+13)%26+c)

print "".join([rot13.get(c,c) for c in str])