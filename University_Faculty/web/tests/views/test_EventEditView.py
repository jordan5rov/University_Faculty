import datetime

from django.urls import reverse

from University_Faculty.common.constants import VALID_EVENT_DATA

from django.test import TestCase

from University_Faculty.web.models import Event


class EventEditViewTests(TestCase):
    VALID_EVENT_DATA = VALID_EVENT_DATA

    def test_edit_event__when_all_valid__expect_to_edit(self):
        event = Event.objects.create(**self.VALID_EVENT_DATA)
        self.client.post(
            reverse('edit event', kwargs={'pk': event.pk}),
            {'title': 'New Title', 'description': 'New Description' * 10, 'date': datetime.date(3023, 1, 1)}
        )

        event.refresh_from_db()
        self.assertIsNotNone(event)
        self.assertEqual(event.title, 'New Title')

    def test_edit_event__when_invalid_date__expect_to_not_edit(self):
        event = Event.objects.create(**self.VALID_EVENT_DATA)
        self.client.post(
            reverse('edit event', kwargs={'pk': event.pk}),
            {'title': 'New Title', 'description': 'New Description' * 10, 'date': datetime.date(2022, 1, 1)}
        )
        event.refresh_from_db()
        self.assertIsNotNone(event)
        self.assertNotEqual(event.date, datetime.date(2022, 1, 1))

    def test_edit_event__when_all_valid__expect_to_redirect(self):
        event = Event.objects.create(**self.VALID_EVENT_DATA)
        response = self.client.post(
            reverse('edit event', kwargs={'pk': event.pk}),
            {'title': 'New Title', 'description': 'New Description' * 10, 'date': datetime.date(3023, 1, 1)}
        )

        event.refresh_from_db()
        expected_url = reverse('see more event')
        self.assertIsNotNone(event)
        self.assertRedirects(response, expected_url)

    def test_edit_event__when_all_valid__expect_status_code_302(self):
        event = Event.objects.create(**self.VALID_EVENT_DATA)
        response = self.client.post(
            reverse('edit event', kwargs={'pk': event.pk}),
            {'title': 'New Title', 'description': 'New Description' * 10, 'date': datetime.date(3023, 1, 1)}
        )

        event.refresh_from_db()
        self.assertIsNotNone(event)
        self.assertEqual(response.status_code, 302)
