#!/usr/bin/python

from pelix.ipopo.decorators import ComponentFactory, Provides, Property, \
    Validate, Invalidate, Requires
from pelix.utilities import to_str

import pelix.remote
try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

@ComponentFactory("spell_client_factory")
@Provides(specifications='pelix.http.servlet')
@Property('_path', 'pelix.http.path', "/spellchecker")
@Requires("_checker", "checker_service")
@Property('_reject', pelix.remote.PROP_EXPORT_REJECT, ['pelix.http.servlet'])
class SpellClient(object):
    def __init__(self):
        self._path = None
        self._checker = None

        def do_GET(self, request, response):
            """
            Handle a GET
            """
            query = request.get_path()
            query = query[query.rfind('?')+1:]
            data = urlparse.parse_qs(query)
            paragraph = ""
            language = ""
            result = ""
            try:
                paragraph = data['paragraph'][0]
                language = data['language'][0]
                language = language.upper()
                misspelled_words = self._checker.check(paragraph, language)
                if misspelled_words is None:
                    result = 'Dictionary provider for this language is not installed!'
                else:
                    if not misspelled_words:
                        result = 'All words are well spelled !'
                    else:
                        result = "<b>The misspelled words are: </b>"
                        result += "<span style='color:red;'>"
                        result += " ".join(misspelled_words) + "</span>"
            except (KeyError, IndexError):
                result = "Fill the language and paragraph inputs!"
            content = """
            <html><head><title>SpellChecker</title></head><body>
                <h2>Spellchecker Demo</h2>
                <hr/>
                <form action="/spellchecker" method="get" >
                    Language: <input type="radio" name="language" value="EN">EN
                    <input type="radio" name="language" value="FR">FR
                    <input type="radio" name="language" value="CN">CN<br/>
                    Paragraph: <input type="text" name="paragraph" size="50"/><br/>
                    <input type="submit" value="Check"/>
                </form>
                <hr/>
                {result}
                <hr/>
            </body></html>
            """.format(result=result)
            response.send_content(200, content)