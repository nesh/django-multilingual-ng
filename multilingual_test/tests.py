from django.conf import settings
from django.test import TestCase
from multilingual.languages import get_default_language, set_default_language

from models import *

class SimpleTest(TestCase):
    def test_simple(self):
        default_language = get_default_language()
        obj = SimpleModel.objects.create(bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            obj.bar = 'bar_%s' % lang
        set_default_language(default_language)
        obj.save()

        self.assertEqual(obj.foo, 'foo')
        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar_%s' % lang)
        set_default_language(default_language)

    def test_default(self):
        default_language = get_default_language()
        obj = SimpleModel.objects.create(bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(default_language)


class SimpleTest2(TestCase):
    def test_simple(self):
        default_language = get_default_language()
        obj = SimpleModel.objects.create(foo='foo', bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            obj.bar = 'bar_%s' % lang
        set_default_language(default_language)
        obj.save()

        self.assertEqual(obj.foo, 'foo')
        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar_%s' % lang)
        set_default_language(default_language)

    def test_default(self):
        default_language = get_default_language()
        obj = SimpleModel.objects.create(foo='foo', bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(default_language)


class ABCInheritanceTest(TestCase):
    def test_inheritance(self):
        default_language = get_default_language()
        obj = ABCInheritanceTestModel.objects.create(foo='foo', bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(default_language)

    def test_inheritance2(self):
        default_language = get_default_language()
        obj = ABCInheritanceTestModel2.objects.create(foo='foo', bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(default_language)


class InheritanceTest(TestCase):
    def test_inheritance(self):
        default_language = get_default_language()
        obj = InheritanceTestModel.objects.create(foo='foo', bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(default_language)

    def test_inheritance2(self):
        default_language = get_default_language()
        obj = InheritanceTestModel2.objects.create(foo='foo', bar='bar')

        for lang, name in settings.LANGUAGES:
            set_default_language(lang)
            self.assertEqual(obj.bar, 'bar')
        set_default_language(default_language)
