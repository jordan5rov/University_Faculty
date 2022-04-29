from django.test import TestCase
from django.urls import reverse

from University_Faculty.classroom.models import Quiz


class QuizDataViewTest(TestCase):
    def test_quiz_data__returns_correct_data(self):
        Quiz.objects.create(name='Test Quiz', max_score=100, required_score_to_pass=50, time=10)
        response = self.client.post(reverse('data quiz'), {'quiz_id': 10})
        a = 5

    def test_quiz_data_view_status_code(self):
        pass
