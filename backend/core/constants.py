
from decimal import Decimal
from datetime import datetime, date, time
from json import JSONEncoder
from collections import OrderedDict


DAYS_PER_YEAR = Decimal('365.25')

MONTHS_PER_YEAR = Decimal('12')



class GENDER(object):
    """Genders of the user.
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


class CATEGORIES(object):
    """Categories for products.
    """

    BREAD = 'B'
    DIARY = 'D'
    FRUITS = 'F'
    SEASONINGS = 'S'
    VEGETABLES = 'V'

    CHOICES = (
        (BREAD, 'Bread'),
        (DIARY, 'Diary'),
        (FRUITS, 'Fruits'),
        (SEASONINGS, 'Seasonings'),
        (VEGETABLES, 'Vegetables'),
    )

    DATA = {
        BREAD: {
            'label': 'Bread'
        },
        DIARY: {
            'label': 'Diary'
        },
        FRUITS: {
            'label': 'Fruits'
        },
        SEASONINGS: {
            'label': 'Seasonings'
        },
        VEGETABLES: {
            'label': 'Vegetables'
        }
    }