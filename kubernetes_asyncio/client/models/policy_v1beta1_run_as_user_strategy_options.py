# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.10.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six



class PolicyV1beta1RunAsUserStrategyOptions(object):
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
        'ranges': 'list[PolicyV1beta1IDRange]',
        'rule': 'str'
    }

    attribute_map = {
        'ranges': 'ranges',
        'rule': 'rule'
    }

    def __init__(self, ranges=None, rule=None):  # noqa: E501
        """PolicyV1beta1RunAsUserStrategyOptions - a model defined in Swagger"""  # noqa: E501

        self._ranges = None
        self._rule = None
        self.discriminator = None

        if ranges is not None:
            self.ranges = ranges
        self.rule = rule

    @property
    def ranges(self):
        """Gets the ranges of this PolicyV1beta1RunAsUserStrategyOptions.  # noqa: E501

        Ranges are the allowed ranges of uids that may be used.  # noqa: E501

        :return: The ranges of this PolicyV1beta1RunAsUserStrategyOptions.  # noqa: E501
        :rtype: list[PolicyV1beta1IDRange]
        """
        return self._ranges

    @ranges.setter
    def ranges(self, ranges):
        """Sets the ranges of this PolicyV1beta1RunAsUserStrategyOptions.

        Ranges are the allowed ranges of uids that may be used.  # noqa: E501

        :param ranges: The ranges of this PolicyV1beta1RunAsUserStrategyOptions.  # noqa: E501
        :type: list[PolicyV1beta1IDRange]
        """

        self._ranges = ranges

    @property
    def rule(self):
        """Gets the rule of this PolicyV1beta1RunAsUserStrategyOptions.  # noqa: E501

        Rule is the strategy that will dictate the allowable RunAsUser values that may be set.  # noqa: E501

        :return: The rule of this PolicyV1beta1RunAsUserStrategyOptions.  # noqa: E501
        :rtype: str
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this PolicyV1beta1RunAsUserStrategyOptions.

        Rule is the strategy that will dictate the allowable RunAsUser values that may be set.  # noqa: E501

        :param rule: The rule of this PolicyV1beta1RunAsUserStrategyOptions.  # noqa: E501
        :type: str
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

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
        if not isinstance(other, PolicyV1beta1RunAsUserStrategyOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other