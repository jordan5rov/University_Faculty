import datetime

from django.test import TestCase
from django.urls import reverse

from University_Faculty.common.constants import VALID_EVENT_DATA
from University_Faculty.web.models import Event


class EventCreateViewTests(TestCase):
    VALID_EVENT_DATA = VALID_EVENT_DATA

    def test_create_event__when_all_valid__expect_to_create(self):
        self.client.post(
            reverse('create event'),
            data=self.VALID_EVENT_DATA,
        )

        event = Event.objects.first()
        self.assertIsNotNone(event)
        self.assertEqual(event.title, self.VALID_EVENT_DATA['title'])
        self.assertEqual(event.description, self.VALID_EVENT_DATA['description'])
        self.assertEqual(event.date, self.VALID_EVENT_DATA['date'])

    def test_create_event_when_all_valid__expect_to_redirect_to_home(self):
        response = self.client.post(
            reverse('create event'),
            data=self.VALID_EVENT_DATA,
        )

        event = Event.objects.first()
        self.assertIsNotNone(event)
        expected_url = reverse('home')
        self.assertRedirects(response, expected_url)

    def test_create_event_when_all_valid__expect_status_code_302(self):
        response = self.client.post(
            reverse('create event'),
            data=self.VALID_EVENT_DATA,
        )
        event = Event.objects.first()
        self.assertIsNotNone(event)
        self.assertEqual(response.status_code, 302)

    def test_create_event_when_date_not_valid__expected_to_not_create(self):
        invalid_data = self.VALID_EVENT_DATA.copy()
        invalid_data['date'] = datetime.datetime(2020, 1, 1, 0, 0)
        self.client.post(
            reverse('create event'),
            data=invalid_data,
        )
        self.assertIsNone(Event.objects.first())

