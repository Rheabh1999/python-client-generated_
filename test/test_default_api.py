# coding: utf-8

"""
    TBU API

    Test Bed Unit API. NOTE all IPv6 address strings are formatted per RFC 5952.  # noqa: E501

    OpenAPI spec version: 1.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.default_api import DefaultApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_config_border_router_gtks_put(self):
        """Test case for config_border_router_gtks_put

        """
        pass

    def test_config_border_router_key_lifetimes_put(self):
        """Test case for config_border_router_key_lifetimes_put

        """
        pass

    def test_config_border_router_put(self):
        """Test case for config_border_router_put

        """
        pass

    def test_config_border_router_revoke_keys_put(self):
        """Test case for config_border_router_revoke_keys_put

        """
        pass

    def test_config_chan_plan_bcast_put(self):
        """Test case for config_chan_plan_bcast_put

        """
        pass

    def test_config_chan_plan_explicit_put(self):
        """Test case for config_chan_plan_explicit_put

        """
        pass

    def test_config_chan_plan_fixed_put(self):
        """Test case for config_chan_plan_fixed_put

        """
        pass

    def test_config_chan_plan_reg_op_put(self):
        """Test case for config_chan_plan_reg_op_put

        """
        pass

    def test_config_chan_plan_unicast_put(self):
        """Test case for config_chan_plan_unicast_put

        """
        pass

    def test_config_dodag_routes_get(self):
        """Test case for config_dodag_routes_get

        """
        pass

    def test_config_ip_addresses_get(self):
        """Test case for config_ip_addresses_get

        """
        pass

    def test_config_neighbor_table_get(self):
        """Test case for config_neighbor_table_get

        """
        pass

    def test_config_phy_put(self):
        """Test case for config_phy_put

        """
        pass

    def test_config_preferred_parent_get(self):
        """Test case for config_preferred_parent_get

        """
        pass

    def test_config_router_put(self):
        """Test case for config_router_put

        """
        pass

    def test_config_security_keys_get(self):
        """Test case for config_security_keys_get

        """
        pass

    def test_config_whitelist_put(self):
        """Test case for config_whitelist_put

        """
        pass

    def test_run_mode_mode_put(self):
        """Test case for run_mode_mode_put

        """
        pass

    def test_subscription_frames_hash_get(self):
        """Test case for subscription_frames_hash_get

        """
        pass

    def test_subscription_frames_put(self):
        """Test case for subscription_frames_put

        """
        pass

    def test_transmitter_icmpv6_echo_put(self):
        """Test case for transmitter_icmpv6_echo_put

        """
        pass

    def test_transmitter_udp_put(self):
        """Test case for transmitter_udp_put

        """
        pass


if __name__ == '__main__':
    unittest.main()
