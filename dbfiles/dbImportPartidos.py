from elementtree import ElementTree as et
# Load the xml content from a string
tree = et.parse('Partidos.xml')

root = tree.getroot()

for partido in root:
	nome = partido[2]
	sigla = partido[1][0][0]

	# print "id: " + deputado.attrib.get('id')
	print "nome: " + nome.text
	print "sigla: " + sigla.text
	print '\n'