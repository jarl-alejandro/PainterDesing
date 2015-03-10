from django.db import models
from users.models import User

class Photo(models.Model):
	image = models.ImageField(upload_to = "photo")
	user = models.ForeignKey(User)
	desc = models.TextField()
	like = models.IntegerField(default = 0)

	def __unicode__(self):
		return "%s %s" % (self.user.email, self.desc)