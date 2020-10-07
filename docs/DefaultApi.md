# swagger_client.DefaultApi

All URIs are relative to *https://localhost/Wi-SUN/TBU/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**config_border_router_gtks_put**](DefaultApi.md#config_border_router_gtks_put) | **PUT** /config/borderRouter/gtks | 
[**config_border_router_key_lifetimes_put**](DefaultApi.md#config_border_router_key_lifetimes_put) | **PUT** /config/borderRouter/keyLifetimes | 
[**config_border_router_put**](DefaultApi.md#config_border_router_put) | **PUT** /config/borderRouter | 
[**config_border_router_revoke_keys_put**](DefaultApi.md#config_border_router_revoke_keys_put) | **PUT** /config/borderRouter/revokeKeys | 
[**config_chan_plan_bcast_put**](DefaultApi.md#config_chan_plan_bcast_put) | **PUT** /config/chanPlan/bcast | 
[**config_chan_plan_explicit_put**](DefaultApi.md#config_chan_plan_explicit_put) | **PUT** /config/chanPlan/explicit | 
[**config_chan_plan_fixed_put**](DefaultApi.md#config_chan_plan_fixed_put) | **PUT** /config/chanPlan/fixed | 
[**config_chan_plan_reg_op_put**](DefaultApi.md#config_chan_plan_reg_op_put) | **PUT** /config/chanPlan/regOp | 
[**config_chan_plan_unicast_put**](DefaultApi.md#config_chan_plan_unicast_put) | **PUT** /config/chanPlan/unicast | 
[**config_dodag_routes_get**](DefaultApi.md#config_dodag_routes_get) | **GET** /config/dodagRoutes | 
[**config_ip_addresses_get**](DefaultApi.md#config_ip_addresses_get) | **GET** /config/ipAddresses | 
[**config_neighbor_table_get**](DefaultApi.md#config_neighbor_table_get) | **GET** /config/neighborTable | 
[**config_phy_put**](DefaultApi.md#config_phy_put) | **PUT** /config/phy | 
[**config_preferred_parent_get**](DefaultApi.md#config_preferred_parent_get) | **GET** /config/preferredParent | 
[**config_router_put**](DefaultApi.md#config_router_put) | **PUT** /config/router | 
[**config_security_keys_get**](DefaultApi.md#config_security_keys_get) | **GET** /config/securityKeys | 
[**config_whitelist_put**](DefaultApi.md#config_whitelist_put) | **PUT** /config/whitelist | 
[**run_mode_mode_put**](DefaultApi.md#run_mode_mode_put) | **PUT** /runMode/{mode} | 
[**subscription_frames_hash_get**](DefaultApi.md#subscription_frames_hash_get) | **GET** /subscription/frames/hash | 
[**subscription_frames_put**](DefaultApi.md#subscription_frames_put) | **PUT** /subscription/frames | 
[**transmitter_icmpv6_echo_put**](DefaultApi.md#transmitter_icmpv6_echo_put) | **PUT** /transmitter/icmpv6Echo | 
[**transmitter_udp_put**](DefaultApi.md#transmitter_udp_put) | **PUT** /transmitter/udp | 


# **config_border_router_gtks_put**
> config_border_router_gtks_put(body)



Configure Border Router GTKs. This method may only be issued to a Border Router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.GroupTransientKeys() # GroupTransientKeys | 

try:
    api_instance.config_border_router_gtks_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_border_router_gtks_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupTransientKeys**](GroupTransientKeys.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_border_router_key_lifetimes_put**
> config_border_router_key_lifetimes_put(body)



Configure Border Router key lifetimes. This method may only be issued to a Border Router.  If non-default key lifetimes are needed, this call MUST be issued before setting the GTKs with /config/borderRouter/gtks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.KeyLifetimes() # KeyLifetimes | 

try:
    api_instance.config_border_router_key_lifetimes_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_border_router_key_lifetimes_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KeyLifetimes**](KeyLifetimes.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_border_router_put**
> config_border_router_put(body)



Configure Border Router specific settings.  This method may only be issued to a Border Router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.BorderRouterConfig() # BorderRouterConfig | 

try:
    api_instance.config_border_router_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_border_router_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BorderRouterConfig**](BorderRouterConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_border_router_revoke_keys_put**
> config_border_router_revoke_keys_put(body)



This method may only be issued to a Border Router (supporting operation described in Step 3 of TPS section 6.5.2.5 Revocation of Node Access).  The Border Router destroys all GTKs except the currently active GTK, modifies the lifetime of the currently active GTK to be (lifetime / REVOCATION_LIFETIME_REDUCTION), and installs the new GTK provided by this API method.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.GroupTransientKey() # GroupTransientKey | 

try:
    api_instance.config_border_router_revoke_keys_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_border_router_revoke_keys_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupTransientKey**](GroupTransientKey.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_chan_plan_bcast_put**
> config_chan_plan_bcast_put(body)



Configure the broadcast channel plan. This method may only be issued to a Border Router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.BcastChanPlan() # BcastChanPlan | 

try:
    api_instance.config_chan_plan_bcast_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_chan_plan_bcast_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BcastChanPlan**](BcastChanPlan.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_chan_plan_explicit_put**
> config_chan_plan_explicit_put(body)



Configure both the unicast and bcast channel plan using ch0, channel spacing, and number of channels.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ChanPlanExplicit() # ChanPlanExplicit | 

try:
    api_instance.config_chan_plan_explicit_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_chan_plan_explicit_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChanPlanExplicit**](ChanPlanExplicit.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_chan_plan_fixed_put**
> config_chan_plan_fixed_put(body)



Configure both the unicast and bcast channel plan to a single fixed channel.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ChanPlanFixed() # ChanPlanFixed | 

try:
    api_instance.config_chan_plan_fixed_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_chan_plan_fixed_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChanPlanFixed**](ChanPlanFixed.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_chan_plan_reg_op_put**
> config_chan_plan_reg_op_put(body)



Configure both the unicast and bcast channel plan using Regulatory Domain and Operating Class.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ChanPlanRegOp() # ChanPlanRegOp | 

try:
    api_instance.config_chan_plan_reg_op_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_chan_plan_reg_op_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChanPlanRegOp**](ChanPlanRegOp.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_chan_plan_unicast_put**
> config_chan_plan_unicast_put(body)



Configure the unicast channel plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UnicastChanPlan() # UnicastChanPlan | 

try:
    api_instance.config_chan_plan_unicast_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_chan_plan_unicast_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UnicastChanPlan**](UnicastChanPlan.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_dodag_routes_get**
> list[DodagRouteEntry] config_dodag_routes_get()



Return the DODAG downward routes populated on a Border Router.  This method may only be issued to a Border Router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.config_dodag_routes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->config_dodag_routes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DodagRouteEntry]**](DodagRouteEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_ip_addresses_get**
> list[str] config_ip_addresses_get()



Returns all unicast IPv6 addresses configured on the node's FAN interface (LL, ULA, GUA).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.config_ip_addresses_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->config_ip_addresses_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_neighbor_table_get**
> list[NeighborTableEntry] config_neighbor_table_get()



Return the Neighbor Table populated on a Router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.config_neighbor_table_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->config_neighbor_table_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[NeighborTableEntry]**](NeighborTableEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_phy_put**
> config_phy_put(body)



Configure the PHY layer of the FAN stack

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.PhyConfig() # PhyConfig | 

try:
    api_instance.config_phy_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_phy_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PhyConfig**](PhyConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_preferred_parent_get**
> str config_preferred_parent_get(ip_address)



Return the preferred parent of a specific FAN node. This method may only be issued to a Border Router.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ip_address = 'ip_address_example' # str | The IPv6 address of the node to be queried for its preferred parent, formatted per RFC 5952.

try:
    api_response = api_instance.config_preferred_parent_get(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->config_preferred_parent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The IPv6 address of the node to be queried for its preferred parent, formatted per RFC 5952. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_router_put**
> config_router_put(body)



Configure Router specific settings.  This method may be issued to any Router node (including Border Routers).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.RouterConfig() # RouterConfig | 

try:
    api_instance.config_router_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_router_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RouterConfig**](RouterConfig.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_security_keys_get**
> GroupTransientKeys config_security_keys_get()



Return the security keys populated on the node.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.config_security_keys_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->config_security_keys_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GroupTransientKeys**](GroupTransientKeys.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **config_whitelist_put**
> config_whitelist_put(body)



Configure a node's whitelist. When a node is configured with a non-empty whitelist, only frames received from EUI64 addresses within the whitelist are passed up to the MAC layer for processing. If an empty whitelist is configured, the node's whitelist is disabled.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.MacAddresses() # MacAddresses | 

try:
    api_instance.config_whitelist_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->config_whitelist_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MacAddresses**](MacAddresses.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_mode_mode_put**
> run_mode_mode_put(mode)



Set the run mode of the TBU's FAN stack

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
mode = 56 # int | 0 = Stop, 1 = Start.  NOTE successful execution of Stop means that any TBU API  configuration previously issued is cleared AND any transient run-time state (neighbor tables, etc.) is cleared. One must explicitly configure any TBU API parameters required prior to a subsequent Start.

try:
    api_instance.run_mode_mode_put(mode)
except ApiException as e:
    print("Exception when calling DefaultApi->run_mode_mode_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode** | **int**| 0 &#x3D; Stop, 1 &#x3D; Start.  NOTE successful execution of Stop means that any TBU API  configuration previously issued is cleared AND any transient run-time state (neighbor tables, etc.) is cleared. One must explicitly configure any TBU API parameters required prior to a subsequent Start. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_frames_hash_get**
> str subscription_frames_hash_get()



Get current value of the subscription session hash.  Support for this method is OPTIONAL.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.subscription_frames_hash_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->subscription_frames_hash_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_frames_put**
> subscription_frames_put(body)



Forward MAC frames to a specified destination (subscribe to a frame stream).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.FrameSubscription() # FrameSubscription | 

try:
    api_instance.subscription_frames_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->subscription_frames_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FrameSubscription**](FrameSubscription.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transmitter_icmpv6_echo_put**
> transmitter_icmpv6_echo_put(body)



Transmit an ICMPv6 Echo message.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ICMPv6Echo() # ICMPv6Echo | 

try:
    api_instance.transmitter_icmpv6_echo_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->transmitter_icmpv6_echo_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ICMPv6Echo**](ICMPv6Echo.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transmitter_udp_put**
> transmitter_udp_put(body)



Transmit a UDP datagram.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UDPDatagram() # UDPDatagram | 

try:
    api_instance.transmitter_udp_put(body)
except ApiException as e:
    print("Exception when calling DefaultApi->transmitter_udp_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UDPDatagram**](UDPDatagram.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

