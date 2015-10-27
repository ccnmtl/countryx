from datetime import datetime
from django.contrib.auth.models import User
import factory
from countryx.sim.models import (
    Role, State, StateChange, StateVariable,
    StateRoleChoice, Section, SectionTurnDates,
    SectionGroup, SectionGroupState, SectionGroupPlayer,
)


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: "user%d" % n)


class RoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = Role
    name = factory.Sequence(lambda n: 'role {0}'.format(n))


class StateFactory(factory.DjangoModelFactory):
    class Meta:
        model = State
    name = factory.Sequence(lambda n: 'state {0}'.format(n))
    turn = 0
    state_no = 0


class StateChangeFactory(factory.DjangoModelFactory):
    class Meta:
        model = StateChange
    state = factory.SubFactory(StateFactory)
    president = 0
    envoy = 1
    regional = 2
    opposition = 3
    next_state = factory.SubFactory(StateFactory)


class StateVariableFactory(factory.DjangoModelFactory):
    class Meta:
        model = StateVariable
    state = factory.SubFactory(StateFactory)
    name = factory.Sequence(lambda n: 'variable {0}'.format(n))


class StateRoleChoiceFactory(factory.DjangoModelFactory):
    class Meta:
        model = StateRoleChoice
    state = factory.SubFactory(StateFactory)
    role = factory.SubFactory(RoleFactory)
    choice = 0
    desc = ""


class SectionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Section
    name = factory.Sequence(lambda n: 'section {0}'.format(n))
    term = factory.Sequence(lambda n: 'term {0}'.format(n))
    year = 2000
    created_date = datetime.now()


class SectionTurnDatesFactory(factory.DjangoModelFactory):
    class Meta:
        model = SectionTurnDates
    section = factory.SubFactory(SectionFactory)
    turn1 = datetime.now()


class SectionGroupFactory(factory.DjangoModelFactory):
    class Meta:
        model = SectionGroup
    section = factory.SubFactory(SectionFactory)
    name = factory.Sequence(lambda n: 'group {0}'.format(n))


class SectionGroupStateFactory(factory.DjangoModelFactory):
    class Meta:
        model = SectionGroupState
    state = factory.SubFactory(StateFactory)
    group = factory.SubFactory(SectionGroupFactory)
    date_updated = datetime.now()


class SectionGroupPlayerFactory(factory.DjangoModelFactory):
    class Meta:
        model = SectionGroupPlayer

    user = factory.SubFactory(UserFactory)
    group = factory.SubFactory(SectionGroupFactory)
    role = factory.SubFactory(RoleFactory)
