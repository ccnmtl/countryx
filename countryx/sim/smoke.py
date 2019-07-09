from smoketest import SmokeTest
from countryx.sim.models import State


class DBConnectivity(SmokeTest):
    def test_retrieve(self):
        cnt = State.objects.all().count()
        self.assertTrue(cnt > 0)
