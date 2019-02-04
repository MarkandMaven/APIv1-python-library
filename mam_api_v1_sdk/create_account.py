"""
    Mark and Maven API
    Contact: systems@markandmaven.com
"""


import pprint
import re
import six

class CreateAccount(object):
    # swagger_types (dict): key is attribute name, value is attribute type
    # attributes_map (dict): key is attribute name and value is json key in definition
    swagger_types = {
        'email': 'str',
        'variables': 'object',
    }

    attribute_map = {
        'email': 'email',
        'variables': 'variables',
    }

    def __init__(self, email=None, variables=None):
        self._email = None
        self._variables = None
        if email is not None:
            self.email = email
        if variables is not None:
            self._variables = variables

    @property
    def email(self):
        return self._email 

    @email.setter
    def email(self, email):
        self.email = email

    @property
    def variables(self):
        return self._variables 

    @variables.setter
    def variables(self, email):
        self.variables = variables

    def to_dict(self):
        # returns model properties as a dict
        result = {}
        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                )
            )

            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()

            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                    )
                )

            else:
                result[attr] = value

        return result

    def to_str(self):
        # returns string representation of the model
        return pprint.pformat(self.to_dict())

class CreateContact(object):

    def __repr__(self):
        # For 'print' and 'pprint'
        return self.to_str()

    def __eq__(self, other):
        # Returns true if both objects are equal
        if not isinstance(other, CreateContact):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        # Returns true if both object are not equal
        return not self == other