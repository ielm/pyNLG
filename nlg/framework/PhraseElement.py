from nlg.features.ClauseStatus import ClauseStatus
from nlg.features.DiscourseFunction import DiscourseFunction
from nlg.features.Feature import Feature
from nlg.features.InternalFeature import InternalFeature
from nlg.framework.NLGFactory import NLGFactory
from nlg.framework.NLGElement import NLGElement
from nlg.framework.StringElement import StringElement
from nlg.framework.PhraseCategory import PhraseCategory
from nlg.phrasespec.NPPhraseSpec import NPPhraseSpec

from typing import List, Union


class PhraseElement(NLGElement):

    def __init__(self, category: PhraseCategory, features: dict = None, factory: NLGFactory = None):
        super().__init__(category=category, features=features, factory=factory)

        if self._features is None:
            self.set_feature(Feature.ELIDED, False)

    def get_children(self) -> List[NLGElement]:
        pass

    def set_head(self, new_head: Union[str, NLGElement, StringElement] = None):
        if new_head is None:
            self.remove_feature(InternalFeature.HEAD)
        if isinstance(new_head, NLGElement):
            self.set_feature(InternalFeature.HEAD, new_head)
        elif isinstance(new_head, StringElement):
            self.set_feature()
        elif isinstance(new_head, str):
            self.set_feature(InternalFeature.HEAD, StringElement(new_head))
        else:
            raise TypeError("must be NLGElement, StringElement, or str")

    def get_head(self) -> NLGElement:
        return self.get_feature_as_element(InternalFeature.HEAD)

    def add_complement(self, new_complement: Union[NLGElement, str] = None):
        pass

    def set_complement(self, new_complement: Union[NLGElement, str] = None):
        pass

    def remove_complements(self, function: DiscourseFunction = None):
        pass

    def add_post_modifier(self, new_post_modifier: Union[NLGElement, str] = None):
        pass

    def set_post_modifier(self, new_post_modifier: Union[NLGElement, str] = None):
        pass

    def add_front_modifier(self, new_front_modifier: Union[NLGElement, str] = None):
        pass

    def set_front_modifier(self, new_front_modifier: Union[NLGElement, str] = None):
        pass

    def add_pre_modifier(self, new_pre_modifier: Union[NLGElement, str] = None):
        pass

    def set_pre_modifier(self, new_pre_modifier: Union[NLGElement, str] = None):
        pass

    def add_modifier(self, new_modifier: Union[NLGElement, str] = None):
        pass

    def set_modifier(self, new_modifier: Union[NLGElement, str] = None):
        pass

    def get_post_modifier(self):
        pass

    def get_front_modifier(self):
        pass

    def get_pre_modifier(self):
        pass

    def print_tree(self, indent: str = None):
        pass

    def clear_complements(self):
        self.remove_feature(InternalFeature.COMPLEMENTS)
