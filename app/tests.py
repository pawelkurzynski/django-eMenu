
import datetime

from django.utils import timezone
from django.test import TestCase
from django.urls import reverse

from .models import *

# Create your tests here.
class MenuModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Menu.objects.create(title='Test Menu', text = 'Opis', pub_date=timezone.now(), mod_date=timezone.now(),)


    def test_first_name_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_date_of_death_label(self):
        author=Author.objects.get(id=1)
        field_label = author._meta.get_field('date_of_death').verbose_name
        self.assertEquals(field_label,'died')

    def test_first_name_max_length(self):
        author=Author.objects.get(id=1)
        max_length = author._meta.get_field('first_name').max_length
        self.assertEquals(max_length,100)

class MenuIndexViewTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        #Create 13 menus for pagination tests
        number_of_menus = 13
        for menu_num in range(number_of_menus):
            Menu.objects.create(title='Test Menu %s' % menu_num, text = 'Opis %s' % menu_num, pub_date=timezone.now(), mod_date=timezone.now(),)

    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('') 
        self.assertEqual(resp.status_code, 200) 

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('app:index_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('app:index_list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app/index_list.html')

    def test_pagination_is_ten(self):
        resp = self.client.get(reverse('app:index_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['menus_list']) == 10)

    def test_lists_all_authors(self):
        #Get second page and confirm it has (exactly) remaining 3 items
        resp = self.client.get(reverse('app:index_list')+'?page=2')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('is_paginated' in resp.context)
        self.assertTrue(resp.context['is_paginated'] == True)
        self.assertTrue( len(resp.context['menus_list']) == 3)


class MenuDetailViewTests(TestCase):
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('app:index_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('app:detail'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'app/detail.html')