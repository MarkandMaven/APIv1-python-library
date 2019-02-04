"""
    Mark and Maven API
    Contact: systems@markandmaven.com
"""

import pprint
import re
import six





class GetContactDetails(object):
'''
Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
'''

    swagger_types = {
        'email': 'str',
        'id': 'int',
        'modified_at': 'datetime',

        'list_ids': 'list[int]',

        'list_unsubscribed': 'list[int]',

        'attributes': 'object'

    }



    attribute_map = {

        'email': 'email',

        'id': 'id',

        'email_blacklisted': 'emailBlacklisted',

        'sms_blacklisted': 'smsBlacklisted',

        'modified_at': 'modifiedAt',

        'list_ids': 'listIds',

        'list_unsubscribed': 'listUnsubscribed',

        'attributes': 'attributes'

    }



    def __init__(self, email=None, id=None, email_blacklisted=None, sms_blacklisted=None, modified_at=None, list_ids=None, list_unsubscribed=None, attributes=None):  # noqa: E501

        """GetContactDetails - a model defined in Swagger"""  # noqa: E501



        self._email = None

        self._id = None

        self._email_blacklisted = None

        self._sms_blacklisted = None

        self._modified_at = None

        self._list_ids = None

        self._list_unsubscribed = None

        self._attributes = None

        self.discriminator = None



        self.email = email

        self.id = id

        self.email_blacklisted = email_blacklisted

        self.sms_blacklisted = sms_blacklisted

        self.modified_at = modified_at

        self.list_ids = list_ids

        if list_unsubscribed is not None:

            self.list_unsubscribed = list_unsubscribed

        self.attributes = attributes



    @property

    def email(self):

        """Gets the email of this GetContactDetails.  # noqa: E501



        Email address of the contact for which you requested the details  # noqa: E501



        :return: The email of this GetContactDetails.  # noqa: E501

        :rtype: str

        """

        return self._email



    @email.setter

    def email(self, email):

        """Sets the email of this GetContactDetails.



        Email address of the contact for which you requested the details  # noqa: E501



        :param email: The email of this GetContactDetails.  # noqa: E501

        :type: str

        """

        if email is None:

            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501



        self._email = email



    @property

    def id(self):

        """Gets the id of this GetContactDetails.  # noqa: E501



        ID of the contact for which you requested the details  # noqa: E501



        :return: The id of this GetContactDetails.  # noqa: E501

        :rtype: int

        """

        return self._id



    @id.setter

    def id(self, id):

        """Sets the id of this GetContactDetails.



        ID of the contact for which you requested the details  # noqa: E501



        :param id: The id of this GetContactDetails.  # noqa: E501

        :type: int

        """

        if id is None:

            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501



        self._id = id



    @property

    def email_blacklisted(self):

        """Gets the email_blacklisted of this GetContactDetails.  # noqa: E501



        Blacklist status for email campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501



        :return: The email_blacklisted of this GetContactDetails.  # noqa: E501

        :rtype: bool

        """

        return self._email_blacklisted



    @email_blacklisted.setter

    def email_blacklisted(self, email_blacklisted):

        """Sets the email_blacklisted of this GetContactDetails.



        Blacklist status for email campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501



        :param email_blacklisted: The email_blacklisted of this GetContactDetails.  # noqa: E501

        :type: bool

        """

        if email_blacklisted is None:

            raise ValueError("Invalid value for `email_blacklisted`, must not be `None`")  # noqa: E501



        self._email_blacklisted = email_blacklisted



    @property

    def sms_blacklisted(self):

        """Gets the sms_blacklisted of this GetContactDetails.  # noqa: E501



        Blacklist status for SMS campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501



        :return: The sms_blacklisted of this GetContactDetails.  # noqa: E501

        :rtype: bool

        """

        return self._sms_blacklisted



    @sms_blacklisted.setter

    def sms_blacklisted(self, sms_blacklisted):

        """Sets the sms_blacklisted of this GetContactDetails.



        Blacklist status for SMS campaigns (true=blacklisted, false=not blacklisted)  # noqa: E501



        :param sms_blacklisted: The sms_blacklisted of this GetContactDetails.  # noqa: E501

        :type: bool

        """

        if sms_blacklisted is None:

            raise ValueError("Invalid value for `sms_blacklisted`, must not be `None`")  # noqa: E501



        self._sms_blacklisted = sms_blacklisted



    @property

    def modified_at(self):

        """Gets the modified_at of this GetContactDetails.  # noqa: E501



        Last modification UTC date-time of the contact (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501



        :return: The modified_at of this GetContactDetails.  # noqa: E501

        :rtype: datetime

        """

        return self._modified_at



    @modified_at.setter

    def modified_at(self, modified_at):

        """Sets the modified_at of this GetContactDetails.



        Last modification UTC date-time of the contact (YYYY-MM-DDTHH:mm:ss.SSSZ)  # noqa: E501



        :param modified_at: The modified_at of this GetContactDetails.  # noqa: E501

        :type: datetime

        """

        if modified_at is None:

            raise ValueError("Invalid value for `modified_at`, must not be `None`")  # noqa: E501



        self._modified_at = modified_at



    @property

    def list_ids(self):

        """Gets the list_ids of this GetContactDetails.  # noqa: E501





        :return: The list_ids of this GetContactDetails.  # noqa: E501

        :rtype: list[int]

        """

        return self._list_ids



    @list_ids.setter

    def list_ids(self, list_ids):

        """Sets the list_ids of this GetContactDetails.





        :param list_ids: The list_ids of this GetContactDetails.  # noqa: E501

        :type: list[int]

        """

        if list_ids is None:

            raise ValueError("Invalid value for `list_ids`, must not be `None`")  # noqa: E501



        self._list_ids = list_ids



    @property

    def list_unsubscribed(self):

        """Gets the list_unsubscribed of this GetContactDetails.  # noqa: E501





        :return: The list_unsubscribed of this GetContactDetails.  # noqa: E501

        :rtype: list[int]

        """

        return self._list_unsubscribed



    @list_unsubscribed.setter

    def list_unsubscribed(self, list_unsubscribed):

        """Sets the list_unsubscribed of this GetContactDetails.





        :param list_unsubscribed: The list_unsubscribed of this GetContactDetails.  # noqa: E501

        :type: list[int]

        """



        self._list_unsubscribed = list_unsubscribed



    @property

    def attributes(self):

        """Gets the attributes of this GetContactDetails.  # noqa: E501



        Set of attributes of the contact  # noqa: E501



        :return: The attributes of this GetContactDetails.  # noqa: E501

        :rtype: object

        """

        return self._attributes



    @attributes.setter

    def attributes(self, attributes):

        """Sets the attributes of this GetContactDetails.



        Set of attributes of the contact  # noqa: E501



        :param attributes: The attributes of this GetContactDetails.  # noqa: E501

        :type: object

        """

        if attributes is None:

            raise ValueError("Invalid value for `attributes`, must not be `None`")  # noqa: E501



        self._attributes = attributes



    def to_dict(self):

        """Returns the model properties as a dict"""

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

        """Returns the string representation of the model"""

        return pprint.pformat(self.to_dict())



    def __repr__(self):

        """For `print` and `pprint`"""

        return self.to_str()



    def __eq__(self, other):

        """Returns true if both objects are equal"""

        if not isinstance(other, GetContactDetails):

            return False



        return self.__dict__ == other.__dict__



    def __ne__(self, other):

        """Returns true if both objects are not equal"""

        return not self == other
