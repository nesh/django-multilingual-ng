from django.conf import settings
from django.test import TestCase
from multilingual.languages import get_default_language, set_default_language

from models import *

class SimpleTest(TestCase):
    def test_all_set(self):
        """ test reading translated data """
        current_language = get_default_language()
        obj = SimpleModel.objects.create(bar='bar')

        for lang, name in settings.LANGUAGES:
            # TODO: check if the activate is right way of activating language
            set_default_language(lang)
            obj.bar = 'bar_%s' % lang
        set_default_language(current_language)
        obj.save()

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar_%s' % lang)
        set_default_language(current_language)

    def test_fallback(self):
        """ test fallback to default language """
        current_language = get_default_language()
        obj = SimpleModel.objects.create(bar='bar')
        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(current_language)


class SimpleTest2(TestCase):
    """ just test if class with only i18n fields works """
    def test_base(self):
        """ simplest case """
        obj = SimpleModel2.objects.create(bar='bar')
        self.assertEqual(obj.bar, 'bar')


class ABCInheritanceTest(TestCase):
    def test_inheritance(self):
        """ test inherited fields from ABC - no additional fields """
        obj = ABCInheritanceTestModel.objects.create(foo='foo', bar='bar')
        self.assertEqual(obj.bar, 'bar')

    def test_inheritance2(self):
        """ test inherited fields from ABC - with additional fields """
        obj = ABCInheritanceTestModel2.objects.create(foo='foo', bar='bar', bar2='bar2')
        self.assertEqual(obj.bar, 'bar')
        self.assertEqual(obj.bar2, 'bar2')


class InheritanceTest(TestCase):
    def test_inheritance(self):
        """ test inherited fields - no additional fields """
        obj = InheritanceTestModel.objects.create(foo='foo', bar='bar')
        self.assertEqual(obj.bar, 'bar')

    def test_inheritance2(self):
        """ test inherited fields - with additional fields """
        obj = InheritanceTestModel2.objects.create(foo='foo', bar='bar', bar2='bar2')
        self.assertEqual(obj.bar, 'bar')
        self.assertEqual(obj.bar2, 'bar2')
