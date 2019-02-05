"""
    Mark and Maven API
    Contact: systems@markandmaven.com
"""

import pprint
import re
import six

class GetAccount(object):
'''
Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
'''

    swagger_types = {
        'email': 'str',
        'variables': 'object',
    }

    attribute_map = {
        'email': 'email',
        'variables': 'variables',
    }

    def __init__(self, email=None, id=None, modified_at=None, variables=None):
        self._email = None
        self._id = None
        self._modified_at = None
        self._variables = None
        self.discriminator = None
        self.email = email
        self.id = id
        self.modified_at = modified_at
        self.variables = variables

    @property
    def email(self):
        # Gets the email of the contact for whom you 
        # requested this Resume
        # :return: The email of this GetResume request
        # :rtype: str

    @email.setter
    def email(self, email):
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")
        self._email = email

    @property
    def id(self):
        # Gets the id of the contact for whom you 
        # requested this Resume
        # :return: The id of this GetResume request
        # :rtype: int
        return self._id

    @id.setter
    def id(self, id):
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        self._id = id

    @property
    def modified_at(self):
        # Gets the modified_at of the contact for whom you 
        # requested this Resume (Last modification UTC date-time of the contact)
        # :return: The modified_at of the Getresume request
        # :rtype: datetime
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        if modified_at is None:
            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501
        self._modified_at = modified_at

@property
    def variables(self):
        # Gets the variables of the contact for whom you 
        # requested this Resume
        # :return: The variables of this GetResume request
        # :rtype: object
        return self._attributes



    @attributes.setter
    def attributes(self, attributes):
        if attributes is None:
            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501
        self._attributes = attributes

    def to_dict(self):
        # Returns model properties as a dict
        result = {}
        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, GetContactDetails):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

