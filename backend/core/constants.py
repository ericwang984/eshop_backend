
from decimal import Decimal
from datetime import datetime, date, time
from json import JSONEncoder
from collections import OrderedDict


DAYS_PER_YEAR = Decimal('365.25')

MONTHS_PER_YEAR = Decimal('12')



class GENDER(object):
    """Genders as required by Veda.
    """

    MALE = 'M'
    FEMALE = 'F'
    UNSPECIFIED = 'U'

    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNSPECIFIED, 'Unspecified'),
    )

    DATA = {
        MALE: {
            'label': 'Male'
        },
        FEMALE: {
            'label': 'Female'
        },
        UNSPECIFIED: {
            'label': 'Unspecified'
        }
    }