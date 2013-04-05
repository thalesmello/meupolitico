from django.test import TestCase
from django.utils import timezone
from politicians.models import Party

class PartyModelTest(TestCase):
    def test_creating_a_new_party_and_saving_it_to_the_database(self):
        # start by creating a new Party object with its "name" and "acronym" set
        party = Party()
        party.name = "Partido dos Iteanos Bitolados"
        party.acronym = "PIB"

        # check we can save it to the database
        party.save()

        # now check we can find it in the database again
        all_parties_in_database = Party.objects.all()
        self.assertEquals(len(all_parties_in_database), 1)
        only_party_in_database = all_parties_in_database[0]
        self.assertEquals(only_party_in_database, party)

        # and check that it's saved its two attributes: name and acronym
        self.assertEquals(only_party_in_database.name, party.name)
        self.assertEquals(only_party_in_database.acronym, party.acronym)
