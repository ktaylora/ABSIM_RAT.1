from parameterization import *

class Builder:
    def __init__(self):
        pass


class SpeculativeBubbleStrategy:
    pass


class RepresentativenessStrategy:
    def __init__(self, *args):
        # args is a list-of-lists
        self._macroeconomics = Macroeconomics(args[0])
        self._neighborhood = Neighborhood(args[1])
        self._production_suitability = Neighborhood(args[2])
        self._demographics = ProducerDemographics(args[3])
        self._production_capacity = ProductionCapacity(args[4])
        self._budget = ProducerBudget(args[5])
