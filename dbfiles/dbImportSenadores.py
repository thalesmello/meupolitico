from elementtree import ElementTree as et
# Load the xml content from a string
tree = et.parse('Senadores.xml')
# root = tree.getroot()
for parlamentar in tree.findall("Parlamentares/Parlamentar"):
	nome = parlamentar.find("NomeSenador")
	nomeParlamentar = parlamentar.find("NomeParlamentar")
	partido = parlamentar.find("SiglaPartido")

	# print "id: " + parlamentar.attrib.get('id')
	print "nome: " + nome.text
	print "nomeParlamentar: " + nomeParlamentar.text
	print "partido: " + partido.text
	print '\n'