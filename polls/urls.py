from . import views
from django.urls import path, include
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet)

polls_router = routers.NestedSimpleRouter(router, r'polls', lookup='poll')
polls_router.register(r'questions', views.QuestionViewSet, basename='poll-questions')


urlpatterns = [
    path('', include(router.urls)),
    path('', include(polls_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]