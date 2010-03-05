# coding: utf-8

from django.db import models

import multilingual

class SimpleModel2(models.Model):
    # i18n fields
    class Translation(multilingual.Translation):
        bar = models.CharField(max_length=50)

    def __unicode__(self):
        return self.bar


class SimpleModel(models.Model):
    foo = models.CharField(max_length=10)

    # i18n fields
    class Translation(multilingual.Translation):
        bar = models.CharField(max_length=50)

    def __unicode__(self):
        return self.bar

# -----------------------------------------------------------------------------
# abstract base class
# -----------------------------------------------------------------------------
class ABCBaseModel(models.Model):
    class Meta:
        abstract = True

    foo = models.CharField(max_length=10)

    # i18n fields
    class Translation(multilingual.Translation):
        bar = models.CharField(max_length=50)

    def __unicode__(self):
        return self.bar


class ABCInheritanceTestModel(ABCBaseModel):
    pass


class ABCInheritanceTestModel2(ABCBaseModel):
    # i18n fields
    class Translation(multilingual.Translation):
        bar2 = models.CharField(max_length=50)


# -----------------------------------------------------------------------------
# regular inheritance
# -----------------------------------------------------------------------------
class BaseModel(models.Model):
    foo = models.CharField(max_length=10)

    # i18n fields
    class Translation(multilingual.Translation):
        bar = models.CharField(max_length=50)

    def __unicode__(self):
        return self.bar


class InheritanceTestModel(BaseModel):
    pass


class InheritanceTestModel2(BaseModel):
    # i18n fields
    class Translation(multilingual.Translation):
        bar2 = models.CharField(max_length=50)
