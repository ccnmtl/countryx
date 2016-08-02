from django.conf.urls import url
import os.path

media_root = os.path.join(os.path.dirname(__file__), "media")

urlpatterns = [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': media_root}),
    url(r'^$', 'countryx.sim.views.root'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'sim/logged_out.html'}),

    # player pages
    url(r'^player/game/(?P<group_id>\d+)/$', 'countryx.sim.views.player_game'),
    url(r'^player/game/(?P<group_id>\d+)/(?P<turn_id>\d+)/$',
        'countryx.sim.views.player_game'),

    # player ajax requests
    url(r'^player/choose/$', 'countryx.sim.views.player_choose'),

    # faculty ajax requests
    url(r'^faculty/reset/(?P<section_id>\d+)/$',
        'countryx.sim.views.faculty_section_reset'),

    # faculty management pages
    url(r'^allpaths/$', 'countryx.sim.views.allpaths'),
    url(r'^allpaths/questions$', 'countryx.sim.views.allquestions'),
    url(r'^allpaths/variables$', 'countryx.sim.views.allvariables'),
    url(r'^faculty/manage/(?P<section_id>\d+)/$',
        'countryx.sim.views.faculty_section_manage'),
    url(r'^faculty/manage/(?P<section_id>\d+)/end_turn/$',
        'countryx.sim.views.faculty_end_turn'),
    url(r'^faculty/groups/(?P<section_id>\d+)/$',
        'countryx.sim.views.faculty_section_bygroup'),
    url(r'^faculty/players/(?P<section_id>\d+)/$',
        'countryx.sim.views.faculty_section_byplayer'),
    url(r'^faculty/group/(?P<group_id>\d+)/$',
        'countryx.sim.views.faculty_group_detail'),
    url((r'^faculty/player/turn/(?P<group_id>\d+)/'
         r'(?P<player_id>\d+)/(?P<state_id>\d+)/$'),
        'countryx.sim.views.faculty_player_detail_byturn'),
    url(r'^faculty/player/(?P<player_id>\d+)/$',
        'countryx.sim.views.faculty_player_detail'),
    url(r'^faculty/feedback/$', 'countryx.sim.views.faculty_feedback_submit'),
    url(r'^cheat/$', 'countryx.sim.views.cheat'),
    url(r'^check_statechanges/$', 'countryx.sim.views.check_statechanges'),
]
