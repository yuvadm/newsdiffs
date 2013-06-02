from django.conf.urls.defaults import *

urlpatterns = patterns('',
  #
  url(r'^upvote/$', 'newsdiffs.frontend.views.upvote', name='upvote'),
  url(r'^diffview/$', 'newsdiffs.frontend.views.old_diffview'),
  url(r'^diff/(?P<vid1>\d+)/(?P<vid2>\d+)/(?P<urlarg>.*)$', 'newsdiffs.frontend.views.diffview', name='diffview'),
  url(r'^about/$', 'newsdiffs.frontend.views.about', name='about'),
  url(r'^browse/$', 'newsdiffs.frontend.views.browse', name='browse'),
  url(r'^browse/(.*)$', 'newsdiffs.frontend.views.browse', name='browse'),
  url(r'^contact/$', 'newsdiffs.frontend.views.contact', name='contact'),
  url(r'^examples/$', 'newsdiffs.frontend.views.examples', name='examples'),
  url(r'^subscribe/$', 'newsdiffs.frontend.views.subscribe', name='subscribe'),
  url(r'^press/$', 'newsdiffs.frontend.views.press', name='press'),
  url(r'^article-history/$', 'newsdiffs.frontend.views.article_history', name='article_history'),
  url(r'^article-history/(?P<urlarg>.*)$', 'newsdiffs.frontend.views.article_history', name='article_history'),
  url(r'^$', 'newsdiffs.frontend.views.front', name='root'),
)
