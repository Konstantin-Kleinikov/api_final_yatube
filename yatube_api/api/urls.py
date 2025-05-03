from django.urls import include, path

urlpatterns_v1 = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(urlpatterns_v1)),
]
