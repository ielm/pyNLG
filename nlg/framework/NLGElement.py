from nlg.features.Feature import Feature
from nlg.features.NumberAgreement import NumberAgreement
from nlg.features.Tense import Tense
from nlg.framework.ElementCategory import ElementCategory
from nlg.framework.NLGFactory import NLGFactory

from typing import Any, List


class NLGElement:

    def __init__(self, category: ElementCategory = None, features: dict = None, factory: NLGFactory = None):
        self._category = category
        self._features = features
        self._factory = factory

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

    # TODO
    #     [] - Implement get feature for long
    #     [] - Implement get feature for float
    #     [] - Implement get feature for double
    #     [] - Implement get feature for bool
    #     [] - Implement get feature for element
    #     [] - Implement get feature for all features
















