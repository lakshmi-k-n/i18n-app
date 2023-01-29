from django.conf import settings


def generate_l18n_schema(languages, default_lang=None):
    schema = {'type': 'dict',
        'keys': {}
    }
    keys = schema['keys']
    properties = {
            'type': 'string',
        }
    for key, value in languages:
        keys[key] = {}
        keys[key].update(properties)
        keys[key].update({'title': value})
    default_language_field = {}
    if default_lang:
        default_language_field = keys.get(
            default_lang
            )
    if default_language_field:
        default_language_field.update(
            {'required': True}
            )
    return schema


SCHEMA = generate_l18n_schema(
    settings.LANGUAGES,
    settings.LANGUAGE_CODE 
    )