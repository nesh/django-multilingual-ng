from django.core.management.base import AppCommand
from django.db import models
from django.utils.importlib import import_module
from django.conf import settings
from django.db import connection
from django.core.management import call_command
from multilingual.utils import is_multilingual_model
from multilingual.languages import get_language_choices
from inspect import isclass
from south.db import db


def get_code_by_id(lid):
    return settings.LANGUAGES[lid-1][0]

class Command(AppCommand):
    """
    Migrate the data from an id base translation table to a code based table.
    """    
    def handle(self, *args, **kwargs):
        if self.are_you_sure():
            super(Command, self).handle(*args, **kwargs)
            print self.style.HTTP_SUCCESS('Done.')
        else:
            print self.style.NOTICE('Aborted.')
        
    def are_you_sure(self):
        n = self.style.NOTICE
        e = self.style.ERROR
        print e("WARNING!") + n(" This command will ") + e("delete") + n(""" data from your database! All language_id  
columns in all multilingual tables of the apps you specified will be deleted.
Their values will be converted to the new language_code format. Please make a
backup of your database before running this command.""")
        answer = raw_input("Are you sure you want to continue? [yes/no]\n")
        if answer.lower() == 'yes':
            return True
        elif answer.lower() == 'no':
            return False
        while True:
            answer = raw_input("Please answer with either 'yes' or 'no'\n")
            if answer.lower() == 'yes':
                return True
            elif answer.lower() == 'no':
                return False
        
    def handle_app(self, app, **options):
        appname = app.__name__
        print 'handling app %s' % appname
        for obj in [getattr(app, name) for name in dir(app)]:
            if not isclass(obj):
                continue
            if not issubclass(obj, models.Model):
                continue
            if not is_multilingual_model(obj):
                continue
            print 'altering model %s' % obj
            table = obj._meta.translation_model._meta.db_table
            db.debug = True
            db.add_column(table, 
                'language_code',
                models.CharField(max_length=15, blank=True,
                    choices=get_language_choices(), db_index=True)
            )
            # migrate the model
            # This is TERRIBLE for performance, but whatever...
            print 'migrating data'
            tempfield = models.IntegerField(blank=False, null=False,
                choices=get_language_choices(), db_index=False)
            tempfield.contribute_to_class(obj._meta.translation_model, 'language_id')
            for row in obj.objects.all():
                for translation in row.translations.all():
                    translation.language_code = get_code_by_id(translation.language_id)
                    translation.save()
            db.create_index(table, ['language_code', 'master_id'])
            print 'deleting language_id column'
            db.delete_unique(table, ['language_id', 'master_id'])
            db.delete_column(table, 'language_id')