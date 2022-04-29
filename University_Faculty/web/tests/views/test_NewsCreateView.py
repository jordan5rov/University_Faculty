from University_Faculty.common.constants import VALID_NEWS_DATA
from django.test import TestCase
from django.urls import reverse

from University_Faculty.web.models import News


class TestNewsCreateView(TestCase):
    VALID_NEWS_DATA = VALID_NEWS_DATA

    def test_create_news__when_all_valid__expect_to_create(self):
        self.client.post(
            reverse('create news'),
            data=self.VALID_NEWS_DATA,
        )
        news = News.objects.first()
        self.assertIsNotNone(news)
        self.assertEqual(news.title, self.VALID_NEWS_DATA['title'])
        self.assertEqual(news.description, self.VALID_NEWS_DATA['description'])

    def test_news_create_view_status_code(self):
        response = self.client.get(reverse('create news'))
        self.assertEquals(response.status_code, 200)
