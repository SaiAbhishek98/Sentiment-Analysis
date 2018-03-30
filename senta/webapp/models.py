from django.db import models

# Create your models here.

class Tweets(models.Model):
	tweet = models.CharField(max_length=3,default="NULL")
	verified_user = models.IntegerField(default=0) #0- not verified, 1 - verified
	no_of_retweets = models.IntegerField(default =0)
	location = models.CharField(max_length=500, default="NULL")
	tweet_id = models.CharField(max_length=20,default="0")


class HashTags(models.Model):
	tweet_id = models.ForeignKey(Tweets,on_delete=models.CASCADE)
	hash_tag = models.CharField(max_length=100,default="0")


class Mentions(models.Model):
	tweet_id = models.ForeignKey(Tweets,on_delete=models.CASCADE)
	mention = models.CharField(max_length=100,default="0")