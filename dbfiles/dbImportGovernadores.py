from elementtree import ElementTree as et
# Load the xml content from a string
tree = et.parse('Governadores.xml')

root = tree.getroot()

for governador in root[1]:
	nome = governador[1][0]
	estado = governador[0][0][0]
	# img = governador[2][0].attrib.get('href')
	img = governador[2][0][0].attrib.get('srcset').split(" ")[-2]
	partido = governador[3][0]
	print nome.text
	print estado.text
	print img
	print partido.text