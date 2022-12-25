import re


operators = [
    '095',
    '066',
    '097',
    '063',
    '093',
    '096',
    '098',
    '068',
    '067',
    '050',
    '099',
    '073',
]


def number_validate(data):
    """Check phone number to format '<operator>xxxxxxx'.
    <operator> == 066/095/097/063/093/096/098/068/067/050/099/073/
    """
    if data[:3] not in operators:
        return False
    res = re.search(r'\d{10}', data)
    return res

