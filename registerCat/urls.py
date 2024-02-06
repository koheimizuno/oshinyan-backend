from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cats', views.CatViewSet)
router.register(r'catimage', views.CatImageViewSet)
router.register(r'character', views.CharacterViewSet)
router.register(r'favoritething', views.FavoriteThingViewSet)
router.register(r'comment', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('randomcat', views.RandomCatView.as_view(), name='randomcat'),
    path('totalrankingcat', views.TotalRankingCatView.as_view(), name='totalrankingcat'),
    path('monthrankingcat', views.MonthRankingCatView.as_view(), name='monthrankingcat'),
    path('searchprefecture', views.SearchPrefectureCatView.as_view(), name='searchprefecture'),
    path('searchword', views.SearchFreeCatView.as_view(), name='searchword'),
    path('recommend', views.RecommendView.as_view(), name='recommend'),
    path('usercat', views.UserCatListView.as_view(), name='usercat'),
]