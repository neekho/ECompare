from django.db import models
from django.urls import reverse
from users.models import RetailerProfile

from PIL import Image
import qrcode
from io import BytesIO
from django.core.files import File

import uuid

# Create your models here.
class Laptop(models.Model):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    brand_name = models.CharField(max_length=30)

    model_name = models.CharField(max_length=75)

    retailer = models.ForeignKey(RetailerProfile, on_delete=models.CASCADE)

    laptop_image = models.ImageField(default='default-laptop.jpg', upload_to='laptop_pics')

    price = models.IntegerField(default=0)

    specs = models.TextField(max_length=1500)

    laptop_url = models.URLField(max_length=1000, default='UNAVAIABLE URL')

    likes = models.IntegerField(default=0) 



    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return f'{self.brand_name}: {self.model_name} - {self.price}'

    def save(self, *args, **kwargs):
        
        # laptop image resizing
        super().save()

        img = Image.open(self.laptop_image.path)
      
        if img.height > 500 or img.width > 500:
            output_size = (400, 400)
            img.thumbnail(output_size)

            img.save(self.laptop_image.path)




        #  creation of the laptop's qr code
        qr_value = f'http://192.168.0.25:8000/shop/laptop/{self.uuid}/'
        print(qr_value)

        qrcode_img = qrcode.make(qr_value)
        canvas = Image.new('RGB', (440, 440), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.uuid}.png'
        buffer = BytesIO()
        canvas.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()

        super().save()



    def get_absolute_url(self):
        return reverse('laptop-detail', kwargs={'pk': self.pk})