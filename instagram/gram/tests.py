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
        search_location = Location.objects.filter(location__i_location__icontains='nairobi')
        self.assertEqual(search_location)

    class CategoryTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.category = Category(i_category='travel')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category))

    # Testing Save method
    def test_save_method(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)

    # Testing Delete method
    def test_delete_method(self):
        self.category.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)<1)

    # Tests whether the category name is updated
    def test_update_category(self):
        self.travel.save_category()
        self.travel.update_category(self.food.id,'food')
        new_update = Location.objects.get(name = "food")
        self.assertEqual(new_update.name, 'food')

    # Tests whether a user can search by category
    def test_search_by_category(cls):
        search_category = Location.objects.filter(category__i_category__icontains='music')
        self.assertEqual(search_category)

    class ImageTestClass(TestCase):
    # Set up method
    def setUp(self):
        # Creating a location
        self.place = Location(location='Machakos')
        self.place.save_location()

        # Creating a category
        self.category = Category(category='cities')
        self.category.save_category()

        # Creating a new image and saving it
        self.image= Image(image_name = 'city lights', image_description= 'A photo of a busy city at night.',location= self.place, category=  self.category)
        self.image.save_image()

        # testing instance
        def test_instance(self):
            self.assertTrue(isinstance(self.image,Image))

        # Test Saving
        def test_save_method(self):
            self.image.save_image()
            image = Image.objects.all()
            self.assertTrue(len(images)>0)

        # Test deleting
        def test_delete_method(self):
            self.image.delete_image()
            image = Image.objects.all()
            self.assertTrue(len(images)<1)

        # Tests whether the image description is updated
        def test_update_image_description(self):
            
            self.image.save_image()
            self.image.update_image_description(self.image.id,'city')
            new_update = Image.objects.get(name = "image")
            self.assertEqual(new_update.description, 'city')

        # Tests whether image can be searched by location
        def test_search_location(self):
            
            self.machakos.save_location()
            self.image.save_image()
            images = Image.filter_by_location("machakos")
            self.assertTrue(len(images) > 0)

        # Tests whether image can be searched by category
        def test_search_category(self):
            
            self.travel.save_category()
            self.image.save_image()
            images = Image.filter_by_category("travel")
            self.assertTrue(len(images) > 0)

