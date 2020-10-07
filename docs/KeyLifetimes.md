# KeyLifetimes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmk_lifetime** | **str** | PMK lifetime (minutes). | [optional] 
**ptk_lifetime** | **str** | PTK lifetime (minutes). | [optional] 
**gtk_lifetime** | **str** | GTK lifetime (minutes) for all GTKs. | [optional] 
**gtk_new_activation_time** | **int** | The time at which the Border Router activates the next GTK prior to expiration of the currently activated GTK.  Calculated as (1/gtkNewActivationTime) * GTK_EXPIRE_OFFSET. | [optional] 
**revocation_lifetime_reduction** | **int** | Factor by which the active GTK lifetime is reduced during node revocation procedures.  Reduced lifetime is calculated as (1/revocationLifetimeReduction) * original lifetime. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


