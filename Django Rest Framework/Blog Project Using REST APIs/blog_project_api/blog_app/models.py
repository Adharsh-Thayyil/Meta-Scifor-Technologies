from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def edit(self, title, description, image):
        self.title = title
        self.description = description
        self.image = image
        self.save()

    def short_description(self):
        words = self.description.split()
        if len(words) > 50:
            return ' '.join(words[:30]) + '...'
        else:
            return self.description
