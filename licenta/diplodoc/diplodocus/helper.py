'''
Created on Jul 6, 2012

@author: Vlad Posea (http://vlad.posea.eu)
'''
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'diplodocus.settings'
from diplodoc.diplodocus import models


def createUserLinkedinProfile(profile,user):

    student=models.StudentLinkedinprofile()
    student.headline=profile['headline']
    student.linkedinId=profile['id']
    student.user=user
    student.interests=profile['interests']
    student.industry=profile['industry']
    student.location=profile['location']
    student.pictureURL=profile['pictureUrl']
    student.publicURL=profile['publicProfileUrl']
    #toadd
    #student.educations
    #student.positions
    try:
        student.save()
        return True
    except Exception:
        return False