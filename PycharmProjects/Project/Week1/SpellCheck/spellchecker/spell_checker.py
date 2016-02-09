#!/usr/bin/python
from pelix.ipopo.decorators import ComponentFactory, Provides, \
    Validate, Invalidate, Requires, BindField, UnbindField
import re

@ComponentFactory("checker_factory")
@Provides(spellchecker.SERVICE_CHECKER)
@Requires("_dictionaries", spellchecker.SERVICE_DICTIONARY, aggregate=True)
class SpellChecker(object):
    def __init__(self):
        self._dictionaries = []
        self.languages = {}

    @BindField('_dictionaries')
    def bind_dict(self, field, service, svc_ref):
        language = svc_ref.get_property('language')
        self.languages[language] = service

    @UnbindField('_dictionaries')
    def unbind_dict(self, field, service, svc_ref):
        language = svc_ref.get_property('language')
        del self.languages[language]

    def check(self, paragraph, language="EN"):
        checked_list = re.split(" ", paragraph)
        try:
            dictionary = self.languages[language]
        except KeyError:
            return None
        return [word for word in checked_list
                if not dictionary.check_word(word)]
