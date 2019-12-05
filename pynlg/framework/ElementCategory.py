class ElementCategory:
    """
    This is the base class for defining categories for the sub classes of
    NLGElement. Each type of category that is used must implement this class.
    """

    def __int__(self):
        pass

    def __eq__(self, other):
        raise NotImplemented