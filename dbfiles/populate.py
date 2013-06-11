from django.core.management import setup_environ

import sys
sys.path.append('../')
from meupolitico import settings
setup_environ(settings)
from politicians.models import *

# print Politician.objects.all()

###################################################
# Popular Partidos
for p in Party.objects.all():
	p.delete()
from elementtree import ElementTree as et
tree = et.parse('Partidos.xml')
root = tree.getroot()
for partido in root:
	nome = partido[2]
	sigla = partido[1][0][0]

	p = Party(name=nome.text, acronym=sigla.text.replace(" ", "").upper())
	p.save()
###################################################
# Limpar Politicos
for p in Politician.objects.all():
	p.delete()
###################################################
# Popular Politicos Manualmente
# Presidente Dilma Rouseff
foto = 'http://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Dilma_Rousseff_-_foto_oficial_2011-01-09.jpg/200px-Dilma_Rousseff_-_foto_oficial_2011-01-09.jpg'
wp = 'http://pt.wikipedia.org/wiki/Dilma_Rousseff'

p = Politician(name='Dilma Rousseff', cargo="Presidente", cidade="Belo Horizonte - MG", foto_url=foto, wikipedia = wp, party=Party.objects.get(acronym='PT'))
p.save()
###################################################
# Popular Governadores
"""from elementtree import ElementTree as et
tree = et.parse('Governadores.xml')
root = tree.getroot()
for governador in root[1]:
	nome = governador[1][0]
	estado = governador[0][0][0]
	img = governador[2][0][0].attrib.get('srcset').split(" ")[-2]
	partido = governador[3][0]

	p = Politician(name=nome.text.title(), cargo="Governador", cidade=" - "+estado.text, foto_url=img, party=Party.objects.get(acronym=partido.text.replace(" ", "").upper()))
	p.save()
# 	# p = Politician.objects.get(name=nome.text)
# 	# p.foto_url = img
# 	# p.save()"""
###################################################
# # Popular Senadores
from elementtree import ElementTree as et
tree = et.parse('Senadores.xml')
for parlamentar in tree.findall("Parlamentares/Parlamentar"):
	nome = parlamentar.find("NomeParlamentar")
	nomeParlamentar = parlamentar.find("NomeSenador")
	partido = parlamentar.find("SiglaPartido")
	foto = parlamentar.find("Foto")
	estado = parlamentar.find("SiglaUf")
	telefone = parlamentar.find("TelefoneParlamentar")

	p = Politician(name=nome.text.title(), cargo="Senador", telefone=telefone.text, cidade=" - "+estado.text, foto_url=foto.text, party=Party.objects.get(acronym=partido.text.replace(" ", "").upper()))
	p.save()
###################################################
# Popular Deputados
from elementtree import ElementTree as et
tree = et.parse('Deputados.xml')
for deputado in tree.findall("deputado"):
	nome = deputado.find("nome")
	nomeParlamentar = deputado.find("nomeParlamentar")
	partido = deputado.find("partido")
	estado = parlamentar.find("uf")
	telefone = parlamentar.find("fone")

	p = Politician(name=nome.text.title(), cargo="Deputado Federal", party=Party.objects.get(acronym=partido.text.replace(" ", "").upper()))
	if telefone != None:
		p['telenfone'] = telefone.text
	if estado != None:
		p['cidade']=" - "+estado.text
	p.save()
###################################################
