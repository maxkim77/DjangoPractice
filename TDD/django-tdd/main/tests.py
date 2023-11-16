from django.test import TestCase, Client
from .models import Post
from bs4 import BeautifulSoup
from datetime import datetime

class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post_001 = Post.objects.create(
            title='첫 번째 포스트입니다.',
            content='Hello World. We are the world.',
        )
        self.post_001.updated_at = datetime.now()
        self.post_001.save()

    def test_page_inheritance(self):
        pages = ['', '/about/', '/contact/', '/blog/']
        for page in pages:
            response = self.client.get(page)
            self.assertEqual(response.status_code, 200)
            soup = BeautifulSoup(response.content, 'html.parser')
            self.assertTrue(soup.find('header'))
            self.assertTrue(soup.find('body'))
            self.assertTrue(soup.find('footer'))

    def test_post_list(self):
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')

        if Post.objects.count() == 0:
            self.assertIn('게시물이 존재하지 않습니다. 첫번째 게시물에 주인공이 되세요!', soup.body.text)
        else:
            self.assertTrue(len(soup.find_all('h2', class_='contents-heading')) >= 1)

    def test_post_detail(self):
        response = self.client.get(f'/blog/{self.post_001.id}/')
        soup = BeautifulSoup(response.content, 'html.parser')

        # 템플릿에 class 속성이 없는 경우
        h2_tag = soup.find('h2')
        self.assertIsNotNone(h2_tag)
        self.assertIn(self.post_001.title, h2_tag.text)
   # 기타 검증...
        self.assertIn(self.post_001.content, soup.find('p', class_='contents-text').text)
        self.assertIn(self.post_001.updated_at.strftime("%Y-%m-%d"), soup.find('p', class_='contents-updated').text)

        self.assertTrue(soup.find('header'))
        self.assertTrue(soup.find('body'))
        self.assertTrue(soup.find('footer'))
