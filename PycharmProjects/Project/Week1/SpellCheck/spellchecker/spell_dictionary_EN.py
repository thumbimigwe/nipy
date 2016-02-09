#!/usr/bin/python3

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, Validate, Invalidate

@ComponentFactory("dictionary_en_factory")
@Provides(spellchecker.SERVICE_DICTIONARY)
@Property("_language", "language", "EN")

class SpellDictionary(object):
    def __init__(self):
        self._dictionary = None
        self._language = None

    @Validate
    def validate(self, context):
        self._dictionary = {"hello","world","welcome","to","Moringa","School"}

    @Invalidate
    def invalidate(self):
        self._dictionary = None

    def check_word(self, word):
        word = word.lower().strip()
        return not word or word in self._dictionary