from django.core.management.base import BaseCommand
from countryx.sim.models import SectionGroupPlayerTurn
from countryx.sim.models import SectionGroupPlayer
from countryx.sim.models import SectionGroupState
from countryx.sim.models import SectionGroup
from countryx.sim.models import SectionTurnDates
from countryx.sim.models import SectionAdministrator
from countryx.sim.models import Section

try:
    # python 2
    my_input = raw_input
except NameError:
    # python 3
    my_input = input


class Command(BaseCommand):
    def clean(self):
        print("Deleting from SectionGroupPlayerTurn....")
        SectionGroupPlayerTurn.objects.all().delete()

        print("Deleting from SectionGroupState....")
        SectionGroupState.objects.all().delete()

        print("Deleting from SectionGroupPlayer....")
        SectionGroupPlayer.objects.all().delete()

        print("Deleting from SectionGroup....")
        SectionGroup.objects.all().delete()

        print("Deleting from SectionTurnDates...")
        SectionTurnDates.objects.all().delete()

        print("Deleting from SectionGroupState....")
        SectionAdministrator.objects.all().delete()

        print("Deleting from Section....")
        Section.objects.all().delete()

    def handle(self, *app_labels, **options):
        # kill everything associated with this section

        result = my_input(
            "Are you sure you want to delete all data related to sections, "
            "groups and users? y/n\r\n")

        if (result == 'n' or result == 'N'):
            print("Canceling...")
        elif (result == 'y' or result == 'Y'):
            self.clean()
            print("Cleaning complete")
        else:
            print("Did not understand the command. Quitting.")
