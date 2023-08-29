from django.db import models

from django.utils.text import slugify





class CategoryImage(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='category/%Y%B%A%d%H')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.name






class PartImages(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,null=True,blank=True)
    image_file = models.FileField(upload_to='images/%Y%B%A%d%H')
    category = models.ForeignKey(to=CategoryImage, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


    def save(self, *args,**kwargs):
        self.slug = slugify(self.name)
        super(PartImages, self).save(*args, **kwargs)


    def __str__(self):
        return self.name 




    
