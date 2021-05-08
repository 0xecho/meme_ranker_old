from django.test import TestCase, Client

import os
import uuid
from PIL import Image

from .helpers import two_randint
from .models import Meme

# Create your tests here.

class RandomGenTestCase(TestCase):

	def test_randints_differ(self):
		rand_ints = two_randint(1000)
		self.assertNotEqual(*rand_ints)

	def test_randints_error(self):
		self.assertRaises(Exception, two_randint, 0)

class UploadMemeTestCase(TestCase):

	images = []

	def get_new_image(self):
		name = "image_" + str(uuid.uuid4()) + ".png"
		img = Image.new('RGB', (100, 100))
		self.images.append(name)
		img.save(name)
		return name

	def setUp(self):
		for _ in range(2):
			name = self.get_new_image()
			meme = Meme(uploader="0xecho", likes=0)
			meme.image.save(name, open(name,"rb"))

	def test_meme_exists(self):
		self.assertTrue(Meme.objects.filter(uploader="0xecho"))

	def test_meme_likes(self):
		c = Client()

		meme = Meme.objects.filter(uploader="0xecho")[0]
		old_like_count = meme.likes
		c.get("/like", {"imgurl":meme.image.name})

		meme.refresh_from_db()
		self.assertEqual(old_like_count+1, meme.likes)

	def test_upload_meme(self):
		c = Client()
		name = self.get_new_image()

		c.post("/upload",{"image":open(name,"rb")})
		self.assertTrue(Meme.objects.count()==3)

	def tearDown(self):
		for image in self.images:
			if os.path.exists(image):
				os.remove(image)
		for meme in Meme.objects.all():
			if os.path.exists(meme.image.path):
				os.remove(meme.image.path)
			meme.delete()

