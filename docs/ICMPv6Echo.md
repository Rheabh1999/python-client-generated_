# ICMPv6Echo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_address** | **str** | The source address to be used by the sender.  Must be one of the LL, ULA, GUA, or mcast addresses configured on the node. IPv6 address strings are formatted per RFC 5952. | 
**dest_address** | **str** | The destination address to which the ICMPv6Echo message will be sent. IPv6 address strings are formatted per RFC 5952. | 
**hop_limit** | **int** | The hop limit value to be set in the IPv6 header. | 
**echo_body** | **str** | The body of the ICMPv6Echo message encoded as a string of ASCII characters. | 
**frame_exchange_pattern** | **int** | Set to 0 if DFE is to be used, set to 1 if EDFE is to be used. | 
**identifier** | **int** | Value to be placed in the ICMPv6 Echo Identifier field. | 
**sequence_number** | **int** | Value to be placed in the ICMPv6 Echo Sequence Number field. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


