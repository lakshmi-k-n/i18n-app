from django.test import TestCase
from django.utils.translation import gettext_lazy as _
import pytest
from .utils import generate_l18n_schema
from books.models import Book


class TestGeneratel18nSchema(object):

    def test_generate_l18n_schema(self):
        expected_schema_1 = {
            'type': 'dict', 
            'keys': { 
                'ml': {
                    'type': 'string',
                    'title': 'Malayalam',
                },
                'en': {
                    'type': 'string',
                    'title': 'English',
                    'required': True
                },
                'hi': {
                    'type': 'string',
                    'title': 'Hindi',
                },
                'ar': {
                    'type': 'string',
                    'title': 'Algerian Arabic',
                },
            }
        }
        expected_schema_2 = {
            'type': 'dict', 
            'keys': { 
                'en': {
                    'type': 'string',
                    'title': 'English',
                    'required': True
                },
                'hi': {
                    'type': 'string',
                    'title': 'Hindi',
                },
                'ar': {
                    'type': 'string',
                    'title': 'Algerian Arabic',
                },
            }
        }
        expected_schema_3 = {
            'type': 'dict', 
            'keys': { 
                'en': {
                    'type': 'string',
                    'title': 'English',
                },
                'hi': {
                    'type': 'string',
                    'title': 'Hindi',
                },
                'ar': {
                    'type': 'string',
                    'title': 'Algerian Arabic',
                },
            }
        }
        expected_schema_4 = {'type':'dict', 'keys':{}}
        languages = [
            ("en", _("English")),
            ("ar", _("Algerian Arabic")),
            ("hi", _("Hindi")),
            ("ml", _("Malayalam")),
            ]
        test_function = generate_l18n_schema
        assert test_function(languages, "en") == expected_schema_1
        languages.pop()
        assert test_function(languages, "en") == expected_schema_2
        assert test_function(languages) == expected_schema_3
        # Passing a language code that does not exist in `languages`
        # parameter
        assert test_function(languages, "kn") == expected_schema_3
        # Passing a languages as an empty list
        assert test_function([], "hi") == expected_schema_4
