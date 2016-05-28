from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', admin.site.urls),
]
