# NeighborTableEntry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eui64** | **str** | The EUI64 of the neighbor node. | 
**etx** | **int** | ETX EWMA of the neighbor node. | 
**rsl** | **int** | RSL EWMA of the neighbor node. | 
**rssi** | **int** | Raw RSSI for the neighbor node. | 
**pan_size** | **int** | The node&#39;s reported PAN size. | 
**routing_cost** | **int** | The node&#39;s reported routing cost. | 
**ip_addresses** | **list[str]** | The IP addresses of the neighbor node. IPv6 address strings are formatted per RFC 5952. | 
**time_since_last_rx** | **int** | msec since last Rx from the neighbor node. | 
**is_parent_status** | **int** | The RPL parent status of the neighbor. 0 means the neighbor is not a RPL parent, 1 means the neighbor is a RPL parent, 2 means the neighbor is the preferred RPL parent. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


