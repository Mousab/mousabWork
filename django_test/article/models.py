from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body  = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField()

    def __unicode__(self):
        return self.title

class Commant(models.Model):
    text = models.TextField()
    a_id  = models.ForeignKey('Article')

    def __unicode__(self):
        return 'Post ID: '+str(self.a_id)+'Comment Text: '+str(self.text)
