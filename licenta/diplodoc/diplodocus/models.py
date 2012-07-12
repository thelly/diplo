from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    idArticle = models.AutoField(primary_key=True)
    title = models.CharField(max_length=765, db_column='title', blank=True) # Field name made lowercase.
    #unde apare in site (companie, vizitator,...)
    section = models.CharField(max_length=30, db_column='section', blank=True) # Field name made lowercase.
    category=models.CharField(max_length=30, db_column='category', blank=True)
    content=models.TextField(db_column="content", blank=True)
    imgURL=models.CharField(max_length=255,db_column='imgURL',blank=True)
    #0=public, 1=private
    rights=models.IntegerField(db_column='rights', blank=True)
    class Meta:
        db_table = u'articol'
                
class StudentLinkedinprofile(models.Model):
    idlinkedinprofile = models.AutoField(primary_key=True, db_column='idlinkedinProfile') # Field name made lowercase.
    publicURL = models.CharField(max_length=765, db_column='publicURL', blank=True) # Field name made lowercase.
    privateURL = models.CharField(max_length=765, db_column='privateURL', blank=True) # Field name made lowercase.
    user = models.OneToOneField(User)
    last_update=models.DateTimeField(null=True,  db_column='last_update', blank=True)
    linkedinId=models.CharField(max_length=60,  db_column='linkedin_id')
    headline=models.CharField(max_length=60,  db_column='headline', blank=True)
    industry=models.CharField(max_length=60,  db_column='industry', blank=True)
    location=models.CharField(max_length=60,  db_column='location', blank=True)
    specialties=models.CharField(max_length=755,db_column="specialties", blank=True)
    interests=models.CharField(max_length=755,db_column="interests",blank=True)
    pictureURL=models.CharField(max_length=255,db_column="pictureURL",blank=True)
    summary=models.TextField(db_column="summary",blank=True)
    class Meta:
        db_table = u'studentLinkedinProfile'
