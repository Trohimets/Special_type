from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import Feedback, Schedule, Playbill, News, \
    People, Companies
from .serializers import FeedbackModelSerializer, \
    ScheduleModelSerializer, \
    PlaybillModelSerializer, NewsModelSerializer, PeopleModelSerializer, \
    CompaniesModelSerializer, RestCaptchaSerializer
from rest_framework import filters, mixins, viewsets, views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class CaptureCheckViewSet(views.APIView):
    def post(self, request):
        serializer = RestCaptchaSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"ok":'Check'})
        raise ValidationError(detail='validation error')


class FeedbackModelViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                           viewsets.GenericViewSet, mixins.CreateModelMixin):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackModelSerializer


class ScheduleModelViewSet(ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleModelSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class PlaybillModelViewSet(ReadOnlyModelViewSet):
    queryset = Playbill.objects.all()
    serializer_class = PlaybillModelSerializer


class NewsModelViewSet(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsModelSerializer


class PeopleModelViewSet(ReadOnlyModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleModelSerializer


class CompanyModelViewSet(ReadOnlyModelViewSet):
    queryset = Companies.objects.all()
    serializer_class = CompaniesModelSerializer
