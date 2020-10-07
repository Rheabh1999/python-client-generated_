# UDPDatagram

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**src_address** | **str** | The source address to be used by the sender.  Must be one of the LL, ULA, GUA, or mcast addresses configured on the node.  IPv6 address strings are formatted per RFC 5952. | 
**src_port** | **int** | The port from which the datagram will be sent. | 
**dest_address** | **str** | The destination address to which the datagram will be sent.  IPv6 address strings are formatted per RFC 5952. | 
**dest_port** | **int** | The port to which the datagram will be sent. | 
**data** | **str** | The body of the UDP datagram encoded as a string of ASCII characters. | 
**frame_exchange_pattern** | **int** | Set to 0 if DFE is to be used, set to 1 if EDFE is to be used. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


