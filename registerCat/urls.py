from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'shop', views.ShopViewSet)
router.register(r'shopnearby', views.ShopNearByViewSet)
router.register(r'cats', views.CatViewSet)
router.register(r'randomcat', views.RandomCatViewSet, basename="randomcat")
router.register(r'catstest', views.CatTestViewSet)
router.register(r'catnearby', views.CatNearbyViewSet, basename='catnearby')
router.register(r'catimage', views.CatImageViewSet)
router.register(r'character', views.CharacterViewSet)
router.register(r'recommend', views.RecommendViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'commentimage', views.CommentImageViewSet)
router.register(r'commentimagerecommend', views.CommentImageRecommendViewSet, basename='commentimagerecommend')
router.register(r'commentimagerecommendbyimgsid', views.CommentImageRecommendByImgsIdViewSet, basename='commentimagerecommendbyimgsid')
router.register(r'advertise', views.AdvertiseViewSet, basename='advertise')
router.register(r'banner', views.BannerViewSet)
router.register(r'column', views.ColumnViewSet)
router.register(r'shoptype', views.ShopTypeViewSet)
router.register(r'reactioncat', views.ReactionCatIconViewSet)
router.register(r'reactionfood', views.ReactionFoodIconViewSet)
router.register(r'reactionword', views.ReactionWordIconViewSet)
router.register(r'reactionparty', views.ReactionPartyIconViewSet)
router.register(r'reactionseason', views.ReactionSeasonIconViewSet)
router.register(r'reactionheart', views.ReactionHeartIconViewSet)
router.register(r'commentreactionicon', views.CommentReactionIconViewSet)
router.register(r'notice', views.NoticeViewSet)
router.register(r'feature', views.FeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('totalrankingcat', views.TotalRankingCatView.as_view(), name='totalrankingcat'),
    path('monthrankingcat', views.MonthRankingCatView.as_view(), name='monthrankingcat'),
    path('searchprefecture', views.SearchPrefectureCatView.as_view(), name='searchprefecture'),
    path('searchcharacter', views.SearchCharacterCatView.as_view(), name='searchcharacter'),
    path('searchattendance', views.SearchAttendanceCatView.as_view(), name='searchattendance'),
    path('searchword', views.SearchFreeCatView.as_view(), name='searchword'),
    path('recommend', views.RecommendView.as_view(), name='recommend'),
    path('usercat', views.UserCatListView.as_view(), name='usercat'),
    path('comment', views.CommentListView.as_view(), name='comment'),
    path('commentbyuser', views.CommentByUserListView.as_view(), name='commentbyuser'),
]