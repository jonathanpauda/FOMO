from django.db import models
from django.conf import settings
from polymorphic.models import PolymorphicModel


class Category(models.Model):
    '''Category for products'''
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.name



# pip3 install django-polymorphic
class Product(PolymorphicModel):
    '''A bulk, individual, or rental product'''
    TYPE_CHOICES = (
        ( 'BulkProduct', 'Bulk Product' ),
        ( 'IndividualProduct', 'Individual Product' ),
        ( 'RentalProduct', 'Rental Product' ),
    )
    STATUS_CHOICES = (
        ( 'A', 'Active' ),
        ( 'I', 'Inactive' ),
    )
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(choices=STATUS_CHOICES, default='A')
    name = models.TextField()
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)


    def image_url(self):
        '''Always returns an image'''
        image = ProductImage.objects.filter(product=self)
        #build the url if i have at least one image_url
        try:
            return settings.STATIC_URL + 'catalog/media/products/' + image[0].filename
        except:
            return settings.STATIC_URL + 'catalog/media/products/image_unavailable.gif'

    def image_urls(self):
        '''Return a list of images'''
        images_qry = ProductImage.objects.filter(product=self)
        images = []
        print('%%%%%%%%%%%%%%%%%%%%%%%LKAJSLKFJADSLKFJALSKDJFALSDKJFALDSKJFALKDSJFALDKSFJADSLKJFLAKDSJFALKDSFJA')
        try:
            for image in images_qry:
                imgURL =  settings.STATIC_URL + 'catalog/media/products/' + image.filename
                images.append([imgURL])
        except:
            for image in images_qry:
                imgURL =  settings.STATIC_URL + 'catalog/media/products/image_unavailable.gif'
                images.append([imgURL])
        return images



    


class BulkProduct(Product):
    '''A bulk product'''
    TITLE = 'Bulk'
    quantity = models.IntegerField()
    reorder_trigger = models.IntegerField()
    reorder_quantity = models.IntegerField()


class IndividualProduct(Product):
    TITLE = 'Individual'
    '''A product tracked individually'''
    pid = models.TextField()


class RentalProduct(Product):
    '''A rental product (tracked individually)'''
    TITLE = 'Rental'
    pid = models.TextField()
    max_rental_days = models.IntegerField(default=0)
    retire_date = models.DateField(null=True, blank=True)


class ProductImage(models.Model):
    '''An image for a product'''
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    filename = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    @property
    def url(self):
        if self.filename:
            return '{}catalog/media/products/{}'.format(settings.STATIC_URL, self.filename)
        return '{}catalog/media/products/notfound.jpg'.format(settings.STATIC_URL)


# just an empty one to get the url to the notfound.png file
NOT_FOUND_PRODUCT_IMAGE = ProductImage()

