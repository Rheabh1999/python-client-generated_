# BcastChanPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bcast_interval** | **int** | Set as specified in TPS BS-IE description. | 
**bcast_schedule_id** | **int** | Set as specified in TPS BS-IE description. | 
**dwell_interval** | **int** | Set as specified in TPS BS-IE description. | 
**channel_function** | **int** | Set as specified in TPS BS-IE description. | 
**excluded_channel_range** | **list[int]** | An array of beginning-of-range/end-of-range channel pairs. Example [1, 10, 20, 25] indicates channels 1 through 10 are excluded and channels 20 through 25 are excluded. NOTE only one of excludedChannelRange OR excludedChannelMask may be specified, with Excluded Channel Control set accordingly, and the non specified exclusion MUST be indicated as an empty array. | 
**excluded_channel_mask** | **list[int]** | Each octet of the bit mask described in the FAN TPS is placed at the corresponding index of the integer array.  Octet 0 is placed at array[0], etc.  NOTE only one of excludedChannelRange OR excludedChannelMask may be specified, with Excluded Channel Control set accordingly, and the non specified exclusion MUST be indicated as an empty array. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


