from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, permissions, mixins, generics
from .serializers import ExamSerializer, AnswerExamSerializer
from exam.models import Exam, AnswerExam


"""
Methods for uploading exams and answers
"""


class ExamUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = ExamSerializer(data=request.data)
        print(request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamAnswersUpload(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = AnswerExamSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Methods for showing list of exams and answers
"""


class ExamAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    permission_classes = []
    serializer_class = ExamSerializer

    def get_queryset(self):
        request = self.request
        qs = Exam.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExamAnswerAPIView(mixins.CreateModelMixin, generics.ListAPIView):

    permission_classes = []
    serializer_class = AnswerExamSerializer

    def get_queryset(self):
        request = self.request
        qs = AnswerExam.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


"""
Methods for showing detail of given record exam/answer to exam
"""


class ExamAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class AnswerExamAPIDetailView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = AnswerExamSerializer
    queryset = AnswerExam.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
