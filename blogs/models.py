from django.db import models

class Blog(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_text = models.TextField()

    def __str__(self):
        return self.blog_title

class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comments")
    comments = models.TextField()

    def __str__(self):
        return self.comments


