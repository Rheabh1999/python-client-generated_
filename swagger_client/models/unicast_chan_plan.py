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


class UnicastChanPlan(object):
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
        'dwell_interval': 'int',
        'channel_function': 'int',
        'excluded_channel_range': 'list[int]',
        'excluded_channel_mask': 'list[int]'
    }

    attribute_map = {
        'dwell_interval': 'dwellInterval',
        'channel_function': 'channelFunction',
        'excluded_channel_range': 'excludedChannelRange',
        'excluded_channel_mask': 'excludedChannelMask'
    }

    def __init__(self, dwell_interval=None, channel_function=None, excluded_channel_range=None, excluded_channel_mask=None):  # noqa: E501
        """UnicastChanPlan - a model defined in Swagger"""  # noqa: E501

        self._dwell_interval = None
        self._channel_function = None
        self._excluded_channel_range = None
        self._excluded_channel_mask = None
        self.discriminator = None

        self.dwell_interval = dwell_interval
        self.channel_function = channel_function
        self.excluded_channel_range = excluded_channel_range
        self.excluded_channel_mask = excluded_channel_mask

    @property
    def dwell_interval(self):
        """Gets the dwell_interval of this UnicastChanPlan.  # noqa: E501

        Set as specified in TPS US-IE description.  # noqa: E501

        :return: The dwell_interval of this UnicastChanPlan.  # noqa: E501
        :rtype: int
        """
        return self._dwell_interval

    @dwell_interval.setter
    def dwell_interval(self, dwell_interval):
        """Sets the dwell_interval of this UnicastChanPlan.

        Set as specified in TPS US-IE description.  # noqa: E501

        :param dwell_interval: The dwell_interval of this UnicastChanPlan.  # noqa: E501
        :type: int
        """
        if dwell_interval is None:
            raise ValueError("Invalid value for `dwell_interval`, must not be `None`")  # noqa: E501

        self._dwell_interval = dwell_interval

    @property
    def channel_function(self):
        """Gets the channel_function of this UnicastChanPlan.  # noqa: E501

        Set as specified in TPS US-IE description.  # noqa: E501

        :return: The channel_function of this UnicastChanPlan.  # noqa: E501
        :rtype: int
        """
        return self._channel_function

    @channel_function.setter
    def channel_function(self, channel_function):
        """Sets the channel_function of this UnicastChanPlan.

        Set as specified in TPS US-IE description.  # noqa: E501

        :param channel_function: The channel_function of this UnicastChanPlan.  # noqa: E501
        :type: int
        """
        if channel_function is None:
            raise ValueError("Invalid value for `channel_function`, must not be `None`")  # noqa: E501

        self._channel_function = channel_function

    @property
    def excluded_channel_range(self):
        """Gets the excluded_channel_range of this UnicastChanPlan.  # noqa: E501

        An array of beginning-of-range/end-of-range channel pairs. Example [1, 10, 20, 25] indicates channels 1 through 10 are excluded and channels 20 through 25 are excluded. NOTE only one of excludedChannelRange OR excludedChannelMask may be specified, with Excluded Channel Control set accordingly, and the non specified exclusion MUST be indicated as an empty array.  # noqa: E501

        :return: The excluded_channel_range of this UnicastChanPlan.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_channel_range

    @excluded_channel_range.setter
    def excluded_channel_range(self, excluded_channel_range):
        """Sets the excluded_channel_range of this UnicastChanPlan.

        An array of beginning-of-range/end-of-range channel pairs. Example [1, 10, 20, 25] indicates channels 1 through 10 are excluded and channels 20 through 25 are excluded. NOTE only one of excludedChannelRange OR excludedChannelMask may be specified, with Excluded Channel Control set accordingly, and the non specified exclusion MUST be indicated as an empty array.  # noqa: E501

        :param excluded_channel_range: The excluded_channel_range of this UnicastChanPlan.  # noqa: E501
        :type: list[int]
        """
        if excluded_channel_range is None:
            raise ValueError("Invalid value for `excluded_channel_range`, must not be `None`")  # noqa: E501

        self._excluded_channel_range = excluded_channel_range

    @property
    def excluded_channel_mask(self):
        """Gets the excluded_channel_mask of this UnicastChanPlan.  # noqa: E501

        Each octet of the bit mask described in the FAN TPS is placed at the corresponding index of the integer array.  Octet 0 is placed at array[0], etc.  NOTE only one of excludedChannelRange OR excludedChannelMask may be specified, with Excluded Channel Control set accordingly, and the non specified exclusion MUST be indicated as an empty array.  # noqa: E501

        :return: The excluded_channel_mask of this UnicastChanPlan.  # noqa: E501
        :rtype: list[int]
        """
        return self._excluded_channel_mask

    @excluded_channel_mask.setter
    def excluded_channel_mask(self, excluded_channel_mask):
        """Sets the excluded_channel_mask of this UnicastChanPlan.

        Each octet of the bit mask described in the FAN TPS is placed at the corresponding index of the integer array.  Octet 0 is placed at array[0], etc.  NOTE only one of excludedChannelRange OR excludedChannelMask may be specified, with Excluded Channel Control set accordingly, and the non specified exclusion MUST be indicated as an empty array.  # noqa: E501

        :param excluded_channel_mask: The excluded_channel_mask of this UnicastChanPlan.  # noqa: E501
        :type: list[int]
        """
        if excluded_channel_mask is None:
            raise ValueError("Invalid value for `excluded_channel_mask`, must not be `None`")  # noqa: E501

        self._excluded_channel_mask = excluded_channel_mask

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
        if issubclass(UnicastChanPlan, dict):
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
        if not isinstance(other, UnicastChanPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
