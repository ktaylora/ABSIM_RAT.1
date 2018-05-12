class Macroeconomics:
    def __init__(self):
        """ These macroeconomic parameters are broadly tracked by commodity market investors and businesses.
        In particular, they were selected for simulating two producer heuristics by producers : (1) the 
        'representativeness heuristic' and (2) 'shiller speculative bubble'. These can be used mechanistically 
        or modeled with data -- such as with decision trees. See the builder interface(s) for implementations. """
        self._ten_year_crb_range = []            # Thomson Reuters/CoreCommodity CRB Commodity Index (Annualized)
        self._crb = []                           # Thomson Reuters/CoreCommodity CRB Commodity Index (Annualized)
        self._ten_year_global_cattle_range = []  # global cattle price high
        self._global_cattle_price = None         # this year's average global cattle price
        self._regional_cattle_price = None       # this year's average regional cattle price
        self._ten_year_global_crop_range = []    # global crop price low and high 
        self._global_crop_prices = []            # proxy for belief about aggregate global demand for crops
        self._regional_crop_prices = []          # proxy for belief about aggregate local (i.e., metropolitian) demand
        self._inflation = []                     # us inflation rate (annualized mean)
        self._ten_year_gdp_range = []            # high and low of (annualized) US GDP
        self._us_gdp = None                      # This year's (annualized mean) GDP

class Neighborhood:
    def __init__(self):
        """ Neighborhood effects on a producer. By design, the neighborhood in our analyses is typically the size of
        a US county though larger sample sizes are not inconceivable
        """
        self._size = None                # maximum distance from existing operation you are willing to purchase new land
        self._number_of_parcels = None   # total number of parcels available for purchase
        self._crop_suitabilities = []    # index of each neighbor's crop suitabilites
        self._cattle_suitabilities = []  # index of each neighbor's cattle suitabilities
        self._seller_interest = []       # index of each neighbor's interest in selling their parcel to you
        self._buyer_interest = []        # index of each neighbor's interest in buying a parcel from you


class LandUnitProductionSuitability:
    def __init__(self):
        """ Production suitability is a per-unit index (0-100) representing probability that an area is used
        for production. The expectation is that a unit with an index value greater than 50 is more likely to be used
        than a unit with an index of less than 50. Suitability indices are often generated from data using a statistical
        model such as a generalized linear model"""
        self._using_grazing_rotations= False
        self._using_crop_rotations = True
        self._years_under_production = 0
        self._unit_crop_suitability = 0
        self._unit_cattle_suitability = 0


class ProducerDemographics:
    def __init__(self):
        """ Producer demographics (e.g., producer age, gender, number of children """
        pass


class ProductionCapacity:
    def __init__(self):
        self._heavy_equipment = None
        self._projected_yield = None
        self._number_of_employees = None

class ProducerBudget:
    def __init__(self):
        """ Represents the annual budget for a given producer (agent) in our model. ProducerBudget should capture
        the bulk of decisions on whether to grow, how much to grow,
        """
        self._annual_operating_cost = None   # Annual cost for maintaining production
        self._median_household_income = None # Median household income target for this producer
        self._acreage_owned = None           # Total acerage under production
        self._crops_managed = []             # Types of crops planted by this producer
        self._cattle_managed = None          # Number of cattle managed by this producer
        self._savings = None                 # How much money do you have in the bank
        self._annual_tax_rate = None

    @property
    def annual_operating_cost(self):
        return self._annual_operating_cost

    @annual_operating_cost.setter
    def annual_operating_cost(self, *args):
        self._annual_operating_cost = args[0]


