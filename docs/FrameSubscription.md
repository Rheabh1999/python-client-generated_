# FrameSubscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_mode** | **str** | The listener starts or stops a frame subscription/forwarding. Start means start forwarding frames and Stop means cease forwarding frames.  If the node implements  /subscription/frames/hash, the node MUST maintain a SHA256 hash of all PCAPNG data forwarded between the acceptance of Start and Stop (inclusive), with this hash initialized to 0 upon reception of Start. | 
**fwd_address** | **str** | The IPv6 address of the listener. IPv6 address strings are formatted per RFC 5952. | 
**fwd_port** | **int** | The port number of the listener. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


