# coding: utf-8

"""
    TBU API

    Test Bed Unit API. NOTE all IPv6 address strings are formatted per RFC 5952.  # noqa: E501

    OpenAPI spec version: 1.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class GroupTransientKey(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'gtk': 'str'
    }

    attribute_map = {
        'gtk': 'gtk'
    }

    def __init__(self, gtk=None):  # noqa: E501
        """GroupTransientKey - a model defined in Swagger"""  # noqa: E501

        self._gtk = None
        self.discriminator = None

        self.gtk = gtk

    @property
    def gtk(self):
        """Gets the gtk of this GroupTransientKey.  # noqa: E501

        Group Transient Key  # noqa: E501

        :return: The gtk of this GroupTransientKey.  # noqa: E501
        :rtype: str
        """
        return self._gtk

    @gtk.setter
    def gtk(self, gtk):
        """Sets the gtk of this GroupTransientKey.

        Group Transient Key  # noqa: E501

        :param gtk: The gtk of this GroupTransientKey.  # noqa: E501
        :type: str
        """
        if gtk is None:
            raise ValueError("Invalid value for `gtk`, must not be `None`")  # noqa: E501

        self._gtk = gtk

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
        if issubclass(GroupTransientKey, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GroupTransientKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
