import os.path

from django.conf.urls import url
import django.views.static

from countryx.sim.views import (
    root, cheat, allpaths, player_choose, faculty_feedback_submit,
    allquestions, allvariables, check_statechanges, player_game,
    faculty_group_detail, faculty_player_detail_byturn,
    faculty_player_detail, faculty_section_reset, faculty_section_manage,
    faculty_section_bygroup, faculty_section_byplayer, faculty_end_turn,
)


media_root = os.path.join(os.path.dirname(__file__), "media")

urlpatterns = [
    url(r'^media/(?P<path>.*)$', django.views.static.serve,
        {'document_root': media_root}),
    url(r'^$', root),

    # player pages
    url(r'^player/game/(?P<group_id>\d+)/$', player_game),
    url(r'^player/game/(?P<group_id>\d+)/(?P<turn_id>\d+)/$', player_game),

    # player ajax requests
    url(r'^player/choose/$', player_choose),

    # faculty ajax requests
    url(r'^faculty/reset/(?P<section_id>\d+)/$', faculty_section_reset),

    # faculty management pages
    url(r'^allpaths/$', allpaths),
    url(r'^allpaths/questions$', allquestions),
    url(r'^allpaths/variables$', allvariables),
    url(r'^faculty/manage/(?P<section_id>\d+)/$', faculty_section_manage),
    url(r'^faculty/manage/(?P<section_id>\d+)/end_turn/$', faculty_end_turn),
    url(r'^faculty/groups/(?P<section_id>\d+)/$', faculty_section_bygroup),
    url(r'^faculty/players/(?P<section_id>\d+)/$', faculty_section_byplayer),
    url(r'^faculty/group/(?P<group_id>\d+)/$', faculty_group_detail),
    url((r'^faculty/player/turn/(?P<group_id>\d+)/'
         r'(?P<player_id>\d+)/(?P<state_id>\d+)/$'),
        faculty_player_detail_byturn),
    url(r'^faculty/player/(?P<player_id>\d+)/$', faculty_player_detail),
    url(r'^faculty/feedback/$', faculty_feedback_submit),
    url(r'^cheat/$', cheat),
    url(r'^check_statechanges/$', check_statechanges),
]
