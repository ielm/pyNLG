from pynlg.features.Feature import Feature
from pynlg.features.NumberAgreement import NumberAgreement
from pynlg.features.Tense import Tense
from pynlg.framework.ElementCategory import ElementCategory
from pynlg.framework.NLGFactory import NLGFactory

from typing import Any


class NLGElement:

    def __init__(self, category: ElementCategory = None, features: dict = None, factory: NLGFactory = None):
        self._category = category
        self._features = features
        self._factory = factory

        self._parent = NLGElement()

    def set_category(self, category: ElementCategory):
        self._category = category

    def get_category(self) -> ElementCategory:
        return self._category

    def set_feature(self, feature_name: str = None, feature_value: Any = None):
        if feature_name is not None:
            if feature_value is None:
                del self._features[feature_name]
            else:
                self._features[feature_name] = feature_value

    def get_feature(self, feature_name: str = None) -> Any:
        if feature_name is not None:
            return self._features[feature_name]

    def get_feature_as_string(self, feature_name: str = None) -> str:
        if feature_name is not None:
            return str(self._features[feature_name])

    def get_feature_as_element_list(self, feature_name: str = None):
        values = []

        value = self.get_feature(feature_name=feature_name)
        if isinstance(value, NLGElement):
            values.append(value)
        elif isinstance(value, list):
            for obj in value:
                if isinstance(obj, NLGElement):
                    values.append(obj)

        return values

    def get_feature_as_list(self, feature_name: str = None):
        values = []

        value = self.get_feature(feature_name=feature_name)
        if value is not None:
            if isinstance(value, list):
                for obj in value:
                    values.append(obj)
            else:
                values.append(value)

        return values

    def get_feature_as_string_list(self, feature_name: str = None):
        values = []

        value = self.get_feature(feature_name=feature_name)
        if value is not None:
            if isinstance(value, list):
                for obj in value:
                    values.append(str(obj))
            else:
                values.append(str(value))

        return values

    def get_feature_as_long(self, feature_name: str = None):
        pass

    def get_feature_as_float(self, feature_name: str = None):
        pass

    def get_feature_as_double(self, feature_name: str = None):
        pass

    def get_feature_as_bool(self, feature_name: str = None):
        pass

    def get_feature_as_element(self, feature_name: str = None):
        pass

    def get_all_features(self):
        pass

    def has_feature(self, feature_name: str = None) -> bool:
        pass

    def remove_feature(self, feature_name: str = None):
        pass

    def clear_all_features(self):
        self._features = {}

    def set_parent(self, new_parent: 'NLGElement' = None):
        self._parent = new_parent
        pass

    def get_parent(self) -> 'NLGElement':
        return self._parent

    def set_realization(self, realized: str = None):
        pass

    def get_realization(self):
        pass

    def to_string(self):
        pass

    def is_a(self, category: ElementCategory = None) -> bool:
        pass

    def get_chidren(self):
        raise NotImplemented

    def get_all_feature_names(self):
        return self._features.keys()

    def print_tree(self, indent: str = None):
        pass

    def set_plural(self, is_plural: bool = None):
        if is_plural:
            self.set_feature(Feature.NUMBER, NumberAgreement.PLURAL)
        else:
            self.set_feature(Feature.NUMBER, NumberAgreement.SINGULAR)

    def is_plural(self) -> bool:
        return NumberAgreement.PLURAL == self.get_feature(Feature.NUMBER)

    def get_tense(self):
        pass

    @DeprecationWarning
    def get_tense(self):
        pass

    @DeprecationWarning
    def set_tense(self, tense: Tense = None):
        if tense is not None:
            self.set_feature(Feature.TENSE, tense)

    @DeprecationWarning
    def set_negated(self, is_negated: bool = None):
        pass

    @DeprecationWarning
    def is_negated(self):
        pass

    def get_factory(self):
        return self._factory

    def set_factory(self, factory: NLGFactory):
        self._factory = factory

    def __eq__(self, element_realization):
        pass
