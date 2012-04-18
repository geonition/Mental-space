from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

urlpatterns = patterns('mental_space.views',
            url(r'^$',
                'mental_space',
                name='mental_space'),
        )
