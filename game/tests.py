from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Game


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_game = Game.objects.create(
            owner = testuser1,
            title = 'test game',
            description = 'game description',
            rating = 10
        )
        test_game.save()

    def test_game_content(self):
        game = Game.objects.get(id=1)
        actual_owner = str(game.owner)
        actual_title = str(game.title)
        actual_description = str(game.description)
        actual_rating = game.rating
        self.assertEqual(actual_owner, 'testuser1')
        self.assertEqual(actual_title, 'test game')
        self.assertEqual(actual_description, 'game description')
        self.assertEqual(actual_rating, 10)