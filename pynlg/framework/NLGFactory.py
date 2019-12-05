from pynlg.features.Feature import Feature
from pynlg.features.Gender import Gender
from pynlg.features.InternalFeature import InternalFeature
from pynlg.features.LexicalFeature import LexicalFeature
from pynlg.features.NumberAgreement import NumberAgreement
from pynlg.features.Person import Person
from pynlg.lexicon.Lexicon import Lexicon
from pynlg.phrasespec.AdjPhraseSpec import AdjPhraseSpec
from pynlg.phrasespec.AdvPhraseSpec import AdvPhraseSpec
from pynlg.phrasespec.NPPhraseSpec import NPPhraseSpec
from pynlg.phrasespec.PPPhraseSpec import PPPhraseSpec
from pynlg.phrasespec.SPhraseSpec import SPhraseSpec
from pynlg.phrasespec.VPPhraseSpec import VPPhraseSpec
from pynlg.framework.NLGElement import NLGElement
from pynlg.framework.PhraseElement import PhraseElement
from pynlg.framework.LexicalCategory import LexicalCategory

from typing import Union, List, Any


class NLGFactory:

    def __init__(self, lexicon: Lexicon = None):

        # The lexicon to be used in this factory
        self._lexicon = lexicon

        # List of English pronouns
        self.PRONOUNS: List[str] = ["I", "you", "he", "she", "it", "me", "you", "him", "her", "it", "myself", "yourself", "himself", "herself", "itself", "mine", "yours", "his", "hers", "its", "we", "you", "they", "they", "they", "us", "you", "them", "them", "them", "ourselves", "yourselves", "themselves", "themselves", "themselves", "ours", "yours", "theirs", "theirs", "theirs", "there"]

        # List of first-person English pronouns
        self.FIRST_PRONOUNS: List[str] = ["I", "me", "myself", "we", "us", "ourselves", "mine", "my", "ours", "our"]

        # List of second-person English pronouns
        self.SECOND_PRONOUNS: List[str] = ["you", "yourself", "yourselves", "yours", "your"]

        # List of reflexive English pronouns
        self.REFLEXIVE_PRONOUNS: List[str] = ["myself", "yourself", "himself", "herself", "itself", "ourselves", "yourselves", "themselves"]

        # List of masculine English pronouns
        self.MASCULINE_PRONOUNS: List[str] = ["he", "him", "himself", "his"]

        # List of feminine English pronouns
        self.FEMININE_PRONOUNS: List[str] = ["she", "her", "herself", "hers"]

        # List of possessive English pronouns
        self.POSEESSIVE_PRONOUNS: List[str] = ["mine", "ours", "yours", "his", "hers", "its", "theirs", "my", "our", "your", "her", "their"]

        # List of plural English pronouns 
        self.PLURAL_PRONOUNS: List[str] = []

        # List of English pronouns that can be either singular or plural
        self.EITHER_NUMBER_PRONOUNS = ["there"]

        # List of expletive English pronouns
        self.EXPLETIVE_PRONOUNS = ["there"]

        # Regex for determining if a string is a single word
        self.WORD_REGEX = "\\w*"

    def set_lexicon(self, lexicon: Lexicon = None):
        self._lexicon = lexicon

    def create_word(self, word: Union[str, NLGElement], category: LexicalCategory):
        word_element = None
        if isinstance(word, NLGElement):
            word_element = word
        elif isinstance(word, str):
            if self._lexicon is not None:
                word_element = self._lexicon.lookupWord(word, category)
                if word in self.PRONOUNS:
                    self.set_pronoun_features(word_element, word)
        return word_element

    def create_inflected_word(self, word: Union[str, NLGElement], category: LexicalCategory):
        pass

    def set_pronoun_features(self, word_element: NLGElement, word: str):
        pass

    def do_lexicon_lookup(self, category: LexicalCategory, word: str, word_element: NLGElement):
        pass

    def create_preposition_phrase(self, preposition: PhraseElement, complement: Any):
        # TODO - Finish implementing create_preposition_phrase
        pass

# TODO
# 	[] - Finish implementing base factory class
