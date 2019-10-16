from django.test import TestCase

# Create your tests here.

from comments.models import Creator, Comment

class CommentTestCase(TestCase):
    def setUp(self):
        creator_data = {
            'fullname': 'mom',
            'profile_picture_url': 'http://cdn.moastro.cn/user_avatar/wx88acc94e3b3d2bce/oFh8LwWJebXNkReq1f9PO4RsLkp0.jpg'
        }
        self.test_creator = Creator.objects.create(**creator_data)

    def test_have_creator(self):
        mom = Creator.objects.get(fullname='mom')
        self.assertEqual(mom.profile_picture_url, 'http://cdn.moastro.cn/user_avatar/wx88acc94e3b3d2bce/oFh8LwWJebXNkReq1f9PO4RsLkp0.jpg')