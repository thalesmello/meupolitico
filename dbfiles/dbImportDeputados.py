from elementtree import ElementTree as et
# Load the xml content from a string
tree = et.parse('Deputados.xml')
# root = tree.getroot()
for deputado in tree.findall("deputado"):
	nome = deputado.find("nome")
	nomeParlamentar = deputado.find("nomeParlamentar")
	partido = deputado.find("partido")

	# print "id: " + deputado.attrib.get('id')
	print "nome: " + nome.text
	print "nomeParlamentar: " + nomeParlamentar.text
	print "partido: " + partido.text
	print '\n'