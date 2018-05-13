from parameterization import *

class Builder:
    def __init__(self):
        pass


class SpeculativeBubbleStrategy:
    pass


class RepresentativenessStrategy:
    def __init__(self, *args, **kwargs):
        # try to use named arguments by default
        try:
            self._macroeconomics = kwargs.get('macroeconomics', args[0])
            self._neighborhood = kwargs.get('neighborhood', args[1])
            self._production_suitability = kwargs.get('production_suitability', args[2])
            self._demographics = kwargs.get('demographics', args[3])
            self._production_capacity = kwargs.get('production_capacity', args[4])
            self._budget = kwargs.get('budget', args[5])
        except Exception as e:
            raise e
