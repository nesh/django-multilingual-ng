"""
XX. Model inheritance

Model inheritance exists in two varieties:
    - abstract base classes which are a way of specifying common
      information inherited by the subclasses. They don't exist as a separate
      model.
    - non-abstract base classes (the default), which are models in their own
      right with their own database tables and everything. Their subclasses
      have references back to them, created automatically.

Both styles are demonstrated here.
"""

from django.db import models
import multilingual

#
# Abstract base classes
#

class CommonInfo(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    # i18n fields
    class Translation(multilingual.Translation):
        title = models.CharField(max_length=200)

    class Meta:
        abstract = True
        ordering = ['name']

    def __unicode__(self):
        return u'%s %s' % (self.__class__.__name__, self.name)

class Worker(CommonInfo):
    job = models.CharField(max_length=50)

class Student(CommonInfo):
    school_class = models.CharField(max_length=10)

    # i18n fields
    class Translation(multilingual.Translation):
        cls = models.CharField(max_length=200)

    class Meta:
        pass


__test__ = {'API_TESTS':"""
# ABC
>>> w = Worker(name='Fred', age=35, job='Quarry worker', title='foo bar')
>>> w.save()

>>> s = Student(name='Pebbles', age=5, school_class='1B', cls='newbie')
>>> s.save()

"""}
