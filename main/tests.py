from django.test import TestCase
from django.urls import resolve, reverse
from .views import indexView
from .models import Author, Service, Testimonial
from projects.models import Project

# Create your tests here.


class StatusCodeTests(TestCase):

    def setUp(self):
        Service.objects.create(name='test1', title='test title1',
                               description='test description1', rate=25, order=1)
        Service.objects.create(name='test2', title='test title2',
                               description='test description2', rate=25, order=2)
        Service.objects.create(name='test3', title='test title3',
                               description='test description3', rate=25, order=4)
        Service.objects.create(name='test4', title='test title4',
                               description='test description4', rate=25, order=3)

    def test_index_view_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(response.context['service_list']), 3)
        print(response.context['service_list'])

    def test_about_view_status_code(self):
        response = self.client.get('/about/')
        self.assertEquals(response.status_code, 200)

    def test_services_view_status_code(self):
        response = self.client.get('/services/')
        self.assertEquals(response.status_code, 200)

    def test_testimonials_view_status_code(self):
        response = self.client.get('/testimonials/')
        self.assertEquals(response.status_code, 200)
