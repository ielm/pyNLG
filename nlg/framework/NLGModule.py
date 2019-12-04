from nlg.lexicon.Lexicon import Lexicon
from nlg.framework.NLGElement import NLGElement

from typing import Union, List


class NLGModule:

    def __init__(self, lexicon: Lexicon = None):
        self._lexicon = lexicon
        raise NotImplemented

    def realize(self, element: Union[List[NLGElement], NLGElement]):
        raise NotImplemented

    def set_lexicon(self, lexicon: Lexicon):
        self._lexicon = lexicon

    def get_lexicon(self):
        return self._lexicon
