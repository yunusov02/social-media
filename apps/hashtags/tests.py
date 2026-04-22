from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Hashtags

class HashtagTests(APITestCase):
    def setUp(self):
        self.hashtag_name = "#python"
        self.hashtag = Hashtags.objects.create(name=self.hashtag_name)
        self.list_url = reverse('hashtags-list')
        self.detail_url = reverse('hashtags-detail', kwargs={'pk': self.hashtag.id})

    def test_model_str_representation(self):
        """
        Test the string representation of the model.
        """

        self.assertEqual(str(self.hashtag), self.hashtag_name)

    def test_soft_delete_logic(self):
        """
        Test that the soft delete logic works on the model level.
        """
        
        count_before = Hashtags.objects.count()
        self.hashtag.delete()
        
        # Should not be in default objects
        self.assertEqual(Hashtags.objects.count(), count_before - 1)
        
        # Should be in all_objects and marked as deleted
        self.assertTrue(Hashtags.all_objects.filter(id=self.hashtag.id, is_deleted=True).exists())
        
        # Test restore
        hashtag = Hashtags.all_objects.get(id=self.hashtag.id)
        hashtag.restore()
        self.assertFalse(hashtag.is_deleted)
        self.assertEqual(Hashtags.objects.count(), count_before)

    def test_list_hashtags(self):
        """
        Test the GET api/hashtags/ endpoint.
        """
        
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the created hashtag is in the response (handling pagination if exists)
        if 'results' in response.data:
            self.assertEqual(len(response.data['results']), 1)
            self.assertEqual(response.data['results'][0]['name'], self.hashtag_name)
        else:
            self.assertEqual(len(response.data), 1)
            self.assertEqual(response.data[0]['name'], self.hashtag_name)

    def test_create_hashtag(self):
        """
        Test the POST api/hashtags/ endpoint.
        """
        
        data = {"name": "#django"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Hashtags.objects.count(), 2)
        self.assertEqual(Hashtags.objects.get(id=response.data['id']).name, "#django")

    def test_retrieve_hashtag(self):
        """
        Test the GET api/hashtags/{id}/ endpoint.
        """
        
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.hashtag_name)

    def test_update_hashtag(self):
        """
        Test the PATCH/PUT api/hashtags/{id}/ endpoint.
        """
        new_name = "#coding"
        response = self.client.patch(self.detail_url, {"name": new_name})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.hashtag.refresh_from_db()
        self.assertEqual(self.hashtag.name, new_name)

    def test_delete_hashtag_api_is_soft(self):
        """
        Test that the DELETE endpoint performs a soft delete.
        """
        
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
        # Verify it's gone from active queryset
        self.assertFalse(Hashtags.objects.filter(id=self.hashtag.id).exists())
        
        # Verify it still exists in DB with is_deleted=True
        deleted_hashtag = Hashtags.all_objects.get(id=self.hashtag.id)
        self.assertTrue(deleted_hashtag.is_deleted)
        self.assertIsNotNone(deleted_hashtag.deleted_at)




