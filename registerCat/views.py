from datetime import datetime, timedelta
from django.db.models import Count

from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from account.models import Member
from account.serializers import MemberSerializer
from .models import Cat, CatImage, CatImageByAdmin, Character, FavoriteThing, Recommend
from .serializers import CatSerializer, CatImageSerializer, CatImageByAdminSerializer, CharacterSerializer, FavoriteThingSerializer, RecommendSerializer

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    def create(self, request, *args, **kwargs):
        cat_data = self.get_serializer(data=request.data)
        images = request.FILES.getlist('imgs')
        if cat_data.is_valid():
            item = cat_data.save()
            for image in images:
                CatImage.objects.create(cat_id=item.id, imgs=image)
            return Response(cat_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'errors': cat_data.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class CatImageViewSet(viewsets.ModelViewSet):
    queryset = CatImage.objects.all()
    serializer_class = CatImageSerializer
    def get_queryset(self):
        return CatImage.objects.none()

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class FavoriteThingViewSet(viewsets.ModelViewSet):
    queryset = FavoriteThing.objects.all()
    serializer_class = FavoriteThingSerializer

class CatImageByAdminViewSet(viewsets.ModelViewSet):
    queryset = CatImageByAdmin.objects.all()
    serializer_class = CatImageByAdminSerializer

class RecommendViewSet(viewsets.ModelViewSet):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer


class RandomCatView(generics.ListCreateAPIView):
    queryset = Cat.objects.filter(is_public=True).order_by('?')[:9]
    serializer_class = CatSerializer

class TotalRankingCatView(generics.ListAPIView):
    serializer_class = CatSerializer
    def get_queryset(self):
        return Cat.objects.filter(is_public=True).annotate(recommend_count=Count('recommend')).order_by('-recommend_count', 'last_update')

class MonthRankingCatView(generics.ListAPIView):
    serializer_class = CatSerializer
    def get_queryset(self):
        date_param = self.request.query_params.get('date')
        if date_param:
            try:
                date = datetime.strptime(date_param, '%Y-%m-%d').date()
                end_date = date
                start_date = end_date - timedelta(days=32)
                return Cat.objects.filter(is_public=True, last_update__gte=start_date, last_update__lte=end_date).annotate(recommend_count=Count('recommend')).order_by('-recommend_count', 'last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)

class SearchPrefectureCatView(generics.ListAPIView):
    serializer_class = CatSerializer
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            try:
                return Cat.objects.filter(prefecture=keyword).annotate(recommend_count=Count('recommend')).order_by('-recommend_count').order_by('-last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)

class SearchFreeCatView(generics.ListAPIView):
    serializer_class = CatSerializer
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword:
            try:
                return Cat.objects.filter(cat_name__icontains=keyword).annotate(recommend_count=Count('recommend')).order_by('-recommend_count').order_by('-last_update')
            except ValueError:
                return Response("Invalid date format", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Date parameter is required", status=status.HTTP_400_BAD_REQUEST)
        
class UserCatListView(generics.ListAPIView):
    serializer_class = CatSerializer
    def get_queryset(self):
        user = self.request.user
        cat_ids = Recommend.objects.filter(user=user).values_list('cat_id', flat=True)
        return Cat.objects.filter(is_public=True, id__in=cat_ids)

class RecommendView(generics.ListCreateAPIView):
    queryset = Recommend.objects.all()
    serializer_class = RecommendSerializer
    def post(self, request, *args, **kwargs):
        user_id = request.data.pop('user_id', None)
        cat_id = request.data.pop('cat_id', None)
        try:
            cat_instance = Cat.objects.get(id=cat_id)
            user_instance = Member.objects.get(id=user_id)
            Recommend.objects.create(cat=cat_instance, user=user_instance)
            return Response({'message': 'Successfully created!'}, status=status.HTTP_201_CREATED)
        except Cat.DoesNotExist:
            return Response({'message': 'Cat not found'}, status=status.HTTP_404_NOT_FOUND)
        except Member.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    def get(self, request, *args, **kwargs):
        cat_id = request.query_params.get('cat_id')
        serializer = Recommend.objects.filter(cat=cat_id).values_list('user_id', flat=True)
        users = Member.objects.filter(id__in=serializer)
        serializer = MemberSerializer(users, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

