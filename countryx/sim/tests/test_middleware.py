from django.test import TestCase

from countryx.sim.middleware import ensure_consistency_of_all_sections
from countryx.sim.tests.factories import SectionTurnDatesFactory


class MiddlewareTest(TestCase):

    def test_no_sections(self):
        ensure_consistency_of_all_sections()

    def test_with_one_section(self):
        SectionTurnDatesFactory()
        ensure_consistency_of_all_sections()
