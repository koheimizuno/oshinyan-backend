from django.conf import settings
from datetime import datetime, timedelta
from django.db.models import Count

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.models import Member
from account.serializers import MemberSerializer
from . import models
from . import serializers

from utils.send_email import send_email
from utils.email_templates import cat_register_email

# For Cat Start
class CatViewSet(viewsets.ModelViewSet):
    queryset = models.Cat.objects.filter(is_public=True)
    serializer_class = serializers.CatSerializer
    
class CatImageViewSet(viewsets.ModelViewSet):
    queryset = models.CatImage.objects.all()
    serializer_class = serializers.CatImageSerializer
    def get_queryset(self):
        return models.CatImage.objects.none()

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer

class FavoriteThingViewSet(viewsets.ModelViewSet):
    queryset = models.FavoriteThing.objects.all()
    serializer_class = serializers.FavoriteThingSerializer

class CatImageByAdminViewSet(viewsets.ModelViewSet):
    queryset = models.CatImageByAdmin.objects.all()
    serializer_class = serializers.CatImageByAdminSerializer

class RecommendViewSet(viewsets.ModelViewSet):
    queryset = models.Recommend.objects.all()
    serializer_class = serializers.RecommendSerializer

class RandomCatView(generics.ListCreateAPIView):
    queryset = models.Cat.objects.filter(is_public=True).order_by('?')[:9]
    serializer_class = serializers.CatSerializer

class TotalRankingCatView(generics.ListAPIView):
    serializer_class = serializers.CatSerializer
    def get_queryset(self):
        return models.Cat.objects.filter(is_public=True).annotate(recommend_count=Count('recommend')).order_by('-recommend_count', 'last_update')

class MonthRankingCatView(generics.ListAPIView):
    serializer_class = serializers.CatSerializer
    def get_queryset(self):
        date_param = self.request.query_params.get('date')
        if date_param:
            try:
                date = datetime.strptime(date_param, '%Y-%m-%d').date()
                end_date = date
                start_date = end_date - timedelta(days=32)
                return models.Cat.objects.filter(is_public=True, last_update__gte=start_date, last_update__lte=end_date).annotate(recommend_count=Count('recommend')).order_by('-recommend_count', 'last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)

class SearchPrefectureCatView(generics.ListAPIView):
    serializer_class = serializers.CatSerializer
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            try:
                return models.Cat.objects.filter(shop__prefecture=keyword).annotate(recommend_count=Count('recommend')).order_by('-recommend_count').order_by('-last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)

class SearchCharacterCatView(generics.ListAPIView):
    serializer_class = serializers.CatSerializer
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            try:
                return models.Cat.objects.filter(character__character=keyword).annotate(recommend_count=Count('recommend')).order_by('-recommend_count').order_by('-last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)

class SearchFreeCatView(generics.ListAPIView):
    serializer_class = serializers.CatSerializer
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            try:
                return models.Cat.objects.filter(cat_name__icontains=keyword).annotate(recommend_count=Count('recommend')).order_by('-recommend_count').order_by('-last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)
        
class UserCatListView(generics.ListAPIView):
    serializer_class = serializers.CatSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        cat_ids = models.Recommend.objects.filter(user=user).values_list('cat_id', flat=True)
        return models.Cat.objects.filter(is_public=True, id__in=cat_ids)

class RecommendView(generics.ListCreateAPIView):
    queryset = models.Recommend.objects.all()
    serializer_class = serializers.RecommendSerializer
    def post(self, request, *args, **kwargs):
        user_id = request.data.pop('user_id', None)
        cat_id = request.data.pop('cat_id', None)
        advertise_id = request.data.pop('advertise_id', None)
        try:
            user_instance = Member.objects.get(id=user_id)
            if cat_id: 
                cat_instance = models.Cat.objects.get(id=cat_id)
                models.Recommend.objects.create(cat=cat_instance, user=user_instance)
                return Response({'message': 'Successfully created!'}, status=status.HTTP_201_CREATED)
            if advertise_id: 
                advertise_instance = models.Advertise.objects.get(id=advertise_id)
                models.Recommend.objects.create(advertise=advertise_instance, user=user_instance)
                return Response({'message': 'Successfully created!'}, status=status.HTTP_201_CREATED)
        except models.Cat.DoesNotExist:
            return Response({'message': 'Cat not found'}, status=status.HTTP_404_NOT_FOUND)
        except Member.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, *args, **kwargs):
        cat_id = request.query_params.get('cat_id')
        serializer = models.Recommend.objects.filter(cat=cat_id).values_list('user_id', flat=True)
        users = Member.objects.filter(id__in=serializer)
        serializer = MemberSerializer(users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
# For Cat End
        
# For Advertise Start
class AdvertiseViewSet(viewsets.ModelViewSet):
    queryset = models.Advertise.objects.all()
    serializer_class = serializers.AdvertiseSerializer

class AdvertiseView(generics.ListAPIView):
    queryset = models.Advertise.objects.filter(is_public=True).order_by('?')[:9]
    serializer_class = serializers.AdvertiseSerializer
# For Advertise End

# For Shop Start
class ShopViewSet(viewsets.ModelViewSet):
    queryset = models.Shop.objects.all()
    serializer_class = serializers.ShopSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['shop_name', 'prefecture', 'shop_type']
    search_fields = ['shop_name', 'prefecture']
    def create(self, request, *args, **kwargs):
        shop_data = self.get_serializer(data=request.data)
        images = request.FILES.getlist('imgs')
        shop_name = request.data.get('shop_name')
        if shop_data.is_valid():
            if not models.Shop.objects.filter(shop_name=shop_name).exists():
                item = shop_data.save()
                for image in images:
                    models.ShopImage.objects.create(shop_id=item.id, imgs=image)
                
                send_email(shop_data.data['email'], "看板猫！発見御礼にゃ！", "<p>" + shop_data.data['shop_name'] + "様</p>" + cat_register_email)
                send_email(settings.BACKEND_EMAIL, '看板猫　登録依頼にゃ！',
                           f"""
                                <p>事務局担当者</p>
                                <p>
                                    「推しニャン」サイトに看板猫発見の依頼がありました。<br/>
                                    下記ご確認ください。
                                </p>
                                <p>日時：{shop_data.data['last_update']}</p>
                                <p>
                                    <span>店舗名：{shop_data.data['shop_name']}</span><br />
                                    <span>住所：{shop_data.data['prefecture'], shop_data.data['city'], shop_data['street'], shop_data.data['detail_address']}</span><br />
                                    <span>メールアドレス：{shop_data.data['email']}</span><br />
                                    <span>電話：{shop_data.data['phone']}</span><br />
                                    <span>店舗許諾：{shop_data.data['shop_permission']}</span><br />
                                    <span>看板猫情報：{shop_data.data['cat_info']}</span>
                                </p>
                                <p>以上です。</p>
                            """
                        )
                
                return Response(shop_data.data, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': shop_data.errors}, status=status.HTTP_400_BAD_REQUEST)

class ShopImageViewSet(viewsets.ModelViewSet):
    queryset = models.ShopImage.objects.all()
    serializer_class = serializers.ShopImageSerializer

class ShopTypeViewSet(viewsets.ModelViewSet):
    queryset = models.ShopType.objects.all()
    serializer_class = serializers.ShopTypeSerializer
# For Shop Start

# For Comment Start
class CommentViewSet(viewsets.ModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    def create(self, request, *args, **kwargs):
        comment_data = self.get_serializer(data=request.data)
        images = request.FILES.getlist('imgs')
        if comment_data.is_valid():
            item = comment_data.save()
            for image in images:
                models.CommentImage.objects.create(comment_id=item.id, imgs=image)
            return Response(comment_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': comment_data.errors}, status=status.HTTP_400_BAD_REQUEST)

class CommentListView(generics.ListAPIView):
    serializer_class = serializers.CommentListSerializer
    def get_queryset(self):
        cat_id = self.request.query_params.get('cat_id')
        if cat_id is not None:
            try:
                return models.Comment.objects.filter(cat=cat_id)
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)
        
class CommentByUserListView(generics.ListAPIView):
    serializer_class = serializers.CommentListSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user_id = self.request.user.id
        if user_id is not None:
            try:
                return models.Comment.objects.filter(user=user_id)
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)
        
class CommentImageRecommendView(generics.ListCreateAPIView):
    queryset = models.CommentImageRecommend.objects.all()
    serializer_class = serializers.CommentImageRecommendSerializer        
    def post(self, request, *args, **kwargs):
        user_id = request.data.pop('user_id', None)
        comment_image_id = request.data.pop('comment_image_id', None)
        try:
            user_instance = Member.objects.get(id=user_id)
            if comment_image_id:
                comment_image_instance = models.CommentImage.objects.get(id=comment_image_id)  # Ensure it references CommentImage
                models.CommentImageRecommend.objects.create(comment_image=comment_image_instance, user=user_instance)
                return Response({'message': 'Successfully created!'}, status=status.HTTP_201_CREATED)
        except models.CommentImage.DoesNotExist:
            return Response({'message': 'Comment image not found'}, status=status.HTTP_404_NOT_FOUND)
        except Member.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class ReactionCatIconViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionCatIcon.objects.all()
    serializer_class = serializers.ReactionCatIconSerializer

class ReactionFoodIconViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionFoodIcon.objects.all()
    serializer_class = serializers.ReactionFoodIconSerializer

class ReactionWordIconViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionWordIcon.objects.all()
    serializer_class = serializers.ReactionWordIconSerializer

class ReactionPartyIconViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionPartyIcon.objects.all()
    serializer_class = serializers.ReactionPartyIconSerializer

class ReactionHeartIconViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionHeartIcon.objects.all()
    serializer_class = serializers.ReactionHeartIconSerializer

class ReactionSeasonIconViewSet(viewsets.ModelViewSet):
    queryset = models.ReactionSeasonIcon.objects.all()
    serializer_class = serializers.ReactionSeasonIconSerializer

class CommentReactionIconViewSet(viewsets.ModelViewSet):
    queryset = models.CommentReactionIcon.objects.all()
    serializer_class = serializers.CommentReactionIconSerializer
# For Comment End
        
class BannerViewSet(viewsets.ModelViewSet):
    queryset = models.Banner.objects.all()
    serializer_class = serializers.BannerSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = models.Column.objects.filter(is_public=True)
    serializer_class = serializers.ColumnSerializer