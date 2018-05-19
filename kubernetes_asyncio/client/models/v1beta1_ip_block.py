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


class V1beta1IPBlock(object):
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
        'cidr': 'str',
        '_except': 'list[str]'
    }

    attribute_map = {
        'cidr': 'cidr',
        '_except': 'except'
    }

    def __init__(self, cidr=None, _except=None):  # noqa: E501
        """V1beta1IPBlock - a model defined in Swagger"""  # noqa: E501

        self._cidr = None
        self.__except = None
        self.discriminator = None

        self.cidr = cidr
        if _except is not None:
            self._except = _except

    @property
    def cidr(self):
        """Gets the cidr of this V1beta1IPBlock.  # noqa: E501

        CIDR is a string representing the IP Block Valid examples are \"192.168.1.1/24\"  # noqa: E501

        :return: The cidr of this V1beta1IPBlock.  # noqa: E501
        :rtype: str
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this V1beta1IPBlock.

        CIDR is a string representing the IP Block Valid examples are \"192.168.1.1/24\"  # noqa: E501

        :param cidr: The cidr of this V1beta1IPBlock.  # noqa: E501
        :type: str
        """
        if cidr is None:
            raise ValueError("Invalid value for `cidr`, must not be `None`")  # noqa: E501

        self._cidr = cidr

    @property
    def _except(self):
        """Gets the _except of this V1beta1IPBlock.  # noqa: E501

        Except is a slice of CIDRs that should not be included within an IP Block Valid examples are \"192.168.1.1/24\" Except values will be rejected if they are outside the CIDR range  # noqa: E501

        :return: The _except of this V1beta1IPBlock.  # noqa: E501
        :rtype: list[str]
        """
        return self.__except

    @_except.setter
    def _except(self, _except):
        """Sets the _except of this V1beta1IPBlock.

        Except is a slice of CIDRs that should not be included within an IP Block Valid examples are \"192.168.1.1/24\" Except values will be rejected if they are outside the CIDR range  # noqa: E501

        :param _except: The _except of this V1beta1IPBlock.  # noqa: E501
        :type: list[str]
        """

        self.__except = _except

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
        if not isinstance(other, V1beta1IPBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other