from django.test import TestCase

# Create your tests here.

class LocationTestCase(TestCase):
    # Set up method
    def setUp(self):
        self.place = Location(location='Machakos')

    # Test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.place,Location))

    # Test Save method
    def test_save_method(self):
        self.place.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.place.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)<1)

    def tearDown(self):
        Location.objects.all().delete()

    # Tests whether the location name is updated
    def test_update_location(self):
        self.machakos.save_location()
        self.machakos.update_location(self.nairobi.id,'nairobi')
        new_update = Location.objects.get(name = "nairobi")
        self.assertEqual(new_update.name, 'nairobi')

    # Tests whether a user can search by location
    def test_search_by_location(cls):
        Location.objects.filter(location__i_category__icontains='nairobi')
        return self.nairobi


