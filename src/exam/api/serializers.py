from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from exam.models import Exam, AnswerExam


"""Serializers for exam/answers"""


class ExamSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    answer_list = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Exam
        fields = ['uri', 'owner', 'title', 'remark', 'file', 'timestamp', 'answer_list']

    def get_uri(self, obj):
        request = self.context.get('request')
        return api_reverse('exams:exam-detail', kwargs={'id': obj.id}, request=request)

    """Nested serializer for related field to_exam (models.py)"""

    def get_answer_list(self, obj):
        qs = obj.answerexam_set.all().order_by('-timestamp')
        return AnswerExamSerializer(qs, many=True).data

    """Override representation of datetime to more human format"""

    def to_representation(self, instance):
        representation = super(ExamSerializer, self).to_representation(instance)
        representation['timestamp'] = instance.timestamp.strftime("%Y-%m-%d | %H:%M:%S")
        return representation


class AnswerExamSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AnswerExam
        fields = ['uri', 'owner', 'title', 'remark', 'file', 'score', 'to_exam', 'timestamp']

    def get_uri(self, obj):
        return f'api/answer/{obj.id}'

    def to_representation(self, instance):
        representation = super(AnswerExamSerializer, self).to_representation(instance)
        representation['timestamp'] = instance.timestamp.strftime("%Y-%m-%d | %H:%M:%S")
        return representation
