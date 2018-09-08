from django.test import TestCase
from .models import Post
from django.urls import reverse

# Create your tests here.

class PostModelTest(TestCase):

	def setUp(self):
		Post.objects.create(context = 'sample text')


	def test_text_content(self):
		post = Post.objects.get(id=1)
		expected_object_name = f'{post.context}'
		self.assertEqual(expected_object_name,'sample text')

class HomePageViewTest(TestCase):

	def setUp(self):
		Post.objects.create(context = 'another test')


	def  test_view_url_exists_at_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code , 200)
	
	def test_view_url_by_name(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code , 200)

	def test_View_uses_correct_template(self):
		resp = self.client.get('/')
		self.assertTemplateUsed(resp, 'home.html')