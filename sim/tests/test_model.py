from django.test import TestCase, Client
from genocideprevention.sim.models import *
import simplejson
import datetime, time

class ModelTestCases(TestCase):
    fixtures = ["test_data.json"]
    
    def test_group_status_noaction(self):
        # update the data manually to setup this test
        group = SectionGroup.objects.get(name='A')
        self.assertEquals(GROUP_STATUS_NOACTION, group.status())
            
    def test_group_status_pending_submitted(self):
        # update the data manually to setup this test
        group = SectionGroup.objects.get(name='A')
        current_state = group.sectiongroupstate_set.latest().state
        players = SectionGroupPlayer.objects.filter(group=group)
        
        count = 0
        for player in players:
            turn = SectionGroupPlayerTurn.objects.create(player=player, turn=current_state.turn, choice=1, submit_date=datetime.datetime.now(), reasoning="foobar")
            if count < 3:
                self.assertEquals(GROUP_STATUS_PENDING, group.status())
            else:
                self.assertEquals(GROUP_STATUS_SUBMITTED, group.status())
            count += 1
            
    def test_player_status(self):
        group = SectionGroup.objects.get(name='B')
        player = SectionGroupPlayer.objects.get(user__username='playerE')
        
        states = group.sectiongroupstate_set.all().order_by('state__turn')
        
        self.assertEquals(PLAYER_STATUS_NOACTION, player.status(states[0].state))
        
        # create a draft for states[1]
        turn = SectionGroupPlayerTurn.objects.create(player=player, turn=states[0].state.turn, choice=1, reasoning="foobar")
        self.assertEquals(PLAYER_STATUS_PENDING, player.status(states[0].state))
        
        turn.submit_date=datetime.datetime.now()
        turn.save()
        self.assertEquals(PLAYER_STATUS_SUBMITTED, player.status(states[0].state))
        
    def test_player_current_status(self):
        group = SectionGroup.objects.get(name='B')
        player = SectionGroupPlayer.objects.get(user__username='playerA')
        
        self.assertEquals(PLAYER_STATUS_NOACTION, player.current_status())
        
    def test_section_current_turn(self):
        time_format = "%Y-%m-%d %H:%M"
        
        section = Section.objects.get(name="Test")
        self.assertEquals(1, section.current_turn())
        
        # make turn 1 be in the past & retest
        turn_dates = SectionTurnDates.objects.get(section=section)
        turn_dates.turn1 = datetime.datetime.fromtimestamp(time.mktime(time.strptime("2008-12-20 12:00", time_format)))
        turn_dates.turn2 = datetime.datetime.fromtimestamp(time.mktime(time.strptime("2020-01-20 12:00", time_format)))
        turn_dates.save()
        
        self.assertEquals(2, section.current_turn())
        
    def test_sectiongroup_force_response_all_players(self):
        # Group A has no player turns in the test data
        
        # Setup some helpful turns for Group A to test all the conditions
        group = SectionGroup.objects.get(name='A')
        state = group.sectiongroupstate_set.latest().state
        playerA = SectionGroupPlayer.objects.get(user__username='playerA')
        playerB = SectionGroupPlayer.objects.get(user__username='playerB')
        playerC = SectionGroupPlayer.objects.get(user__username='playerC')
        playerD = SectionGroupPlayer.objects.get(user__username='playerD')
        
        # create a draft for playerA
        SectionGroupPlayerTurn.objects.create(player=playerA, turn=state.turn, choice=1, reasoning="draft")
        
        # create a full submit for playerB
        SectionGroupPlayerTurn.objects.create(player=playerB, turn=state.turn, choice=2, reasoning="final", submit_date=datetime.datetime.now())
        
        # leave the other two players alone (playerC & payerD)
        group.force_response_all_players()
        
        a_turn = SectionGroupPlayerTurn.objects.get(player=playerA, turn=1, submit_date__isnull=False)
        self.assertEquals(1, a_turn.choice)
        
        b_turn = SectionGroupPlayerTurn.objects.get(player=playerB, turn=1, submit_date__isnull=False)
        self.assertEquals(2, b_turn.choice)   
        
        c_turn = SectionGroupPlayerTurn.objects.get(player=playerC, turn=1, submit_date__isnull=False)       
        self.assert_(c_turn.choice > 0)  
        
        d_turn = SectionGroupPlayerTurn.objects.get(player=playerD, turn=1, submit_date__isnull=False)
        self.assert_(d_turn.choice > 0)
        
    def test_sectiongroup_updatestate(self):
        # Group A has no player turns in the test data
        group = SectionGroup.objects.get(name='A')
        state = group.sectiongroupstate_set.latest().state
         
        # update_state should choke in this situation 
        try:
            group.update_state()
        except:
            pass
        else:
            fail("expected an error in cases where the group does not have submitted answers for each player")
        
        # pick the responses for each player so we can verify the state choice
        players = SectionGroupPlayer.objects.filter(group=group)
        for player in players:
            SectionGroupPlayerTurn.objects.create(player=player, turn=state.turn, choice=2, reasoning="final", submit_date=datetime.datetime.now())
                
        # now, try to update the state
        group.update_state()
        state = group.sectiongroupstate_set.latest().state
        self.assertEquals(State.objects.get(turn=2, name="Violence - COIN"), state)
        