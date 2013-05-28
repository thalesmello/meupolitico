from django.core.management import setup_environ

# If myapp is not in your PYTHONPATH, append it to sys.path
import sys
sys.path.append('../')
from meupolitico import settings
setup_environ(settings)
from politicians.models import *

# print Politician.objects.all()

###################################################
# Popular Partidos
# print Party.objects.all()
for p in Party.objects.all():
	p.delete()
from elementtree import ElementTree as et
# Load the xml content from a string
tree = et.parse('Partidos.xml')

root = tree.getroot()

for partido in root:
	nome = partido[2]
	sigla = partido[1][0][0]

	p = Party(name=nome.text, acronym=sigla.text.replace(" ", "").upper())
	p.save()
# 	# p.id
###################################################
# # Popular Senadores
# print Politician.objects.all()
for p in Politician.objects.all():
	p.delete()
from elementtree import ElementTree as et
tree = et.parse('Senadores.xml')

for parlamentar in tree.findall("Parlamentares/Parlamentar"):
	nome = parlamentar.find("NomeSenador")
	nomeParlamentar = parlamentar.find("NomeParlamentar")
	partido = parlamentar.find("SiglaPartido")

	p = Politician(name=nome.text, cargo="Senador", party=Party.objects.get(acronym=partido.text.replace(" ", "").upper()))
	p.save()
# print Politician.objects.all()	
###################################################
# Popular Deputados
# print Politician.objects.all()
for p in Politician.objects.all():
	p.delete()
from elementtree import ElementTree as et
tree = et.parse('Deputados.xml')
# root = tree.getroot()
for deputado in tree.findall("deputado"):
	nome = deputado.find("nome")
	nomeParlamentar = deputado.find("nomeParlamentar")
	partido = deputado.find("partido")

	p = Politician(name=nome.text, cargo="Deputado Federal", party=Party.objects.get(acronym=partido.text.replace(" ", "").upper()))
	p.save()
# print Politician.objects.all()	
###################################################