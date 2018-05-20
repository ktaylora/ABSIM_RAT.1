import math

from .parameterization import *
from .downloaders import *

class Builder:
    def __init__(self):
        pass


class _SpeculativeBubbleStrategy:
    pass


class EmpiricalSpeculativeBubbleStrategy(_SpeculativeBubbleStrategy):
    pass


class MechanisticSpeculativeBubbleStrategy(_SpeculativeBubbleStrategy):
    pass


class _RepresentativenessStrategy:
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


class EmpiricalRepresentativenessStrategy(_RepresentativenessStrategy):
    pass


class MechanisticRepresentativenessStrategy(_RepresentativenessStrategy):
    def marco_decision(self):
        """fit a beta coefficient to our ten-year commodity market median
        and use the curve to predict favorability"""
        beta = math.log(0.5) / self._macroeconomics._ten_year_crb_median