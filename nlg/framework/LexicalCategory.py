from nlg.framework.ElementCategory import ElementCategory

from enum import Enum


class LexicalCategory(ElementCategory):

    class LexicalCategoryEnum(Enum):
        ANY             = "ANY"
        SYMBOL          = "SYMBOL"
        NOUN            = "NOUN"
        ADJECTIVE       = "ADJECTIVE"
        ADVERB          = "ADVERB"
        VERB            = "VERB"
        DETERMINER      = "DETERMINER"
        PRONOUN         = "PRONOUN"
        CONJUNCTION     = "CONJUNCTION"
        PREPOSITION     = "PREPOSITION"
        COMPLEMENTISER  = "COMPLEMENTISER"
        MODAL           = "MODAL"
        AUXILIARY       = "AUXILIARY"

    def __init__(self, lexical_category: LexicalCategoryEnum):
        self._lexicalCategory = lexical_category

    def __eq__(self, other):
        match = False
        if other is not None:
            if isinstance(other, LexicalCategory):
                match = True
            else:
                match = self._lexicalCategory == str(other)
        return match
