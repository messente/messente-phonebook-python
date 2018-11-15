# phonebook_api.BlacklistApi

All URIs are relative to *https://api.messente.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_to_blacklist**](BlacklistApi.md#add_to_blacklist) | **POST** /phonebook/blacklist | 
[**fetch_blacklist**](BlacklistApi.md#fetch_blacklist) | **GET** /phonebook/blacklist | 
[**remove_from_blacklist**](BlacklistApi.md#remove_from_blacklist) | **DELETE** /phonebook/blacklist/{phone_number} | 


# **add_to_blacklist**
> add_to_blacklist(number_to_blacklist)



Adds a phone number to the blacklist.

### Example

* Basic Authentication (basicAuth): 
```python
from __future__ import print_function
import time
import phonebook_api
from phonebook_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = phonebook_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = phonebook_api.BlacklistApi(phonebook_api.ApiClient(configuration))
number_to_blacklist = phonebook_api.NumberToBlacklist() # NumberToBlacklist | Phone number to be blacklisted

try:
    api_instance.add_to_blacklist(number_to_blacklist)
except ApiException as e:
    print("Exception when calling BlacklistApi->add_to_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number_to_blacklist** | [**NumberToBlacklist**](NumberToBlacklist.md)| Phone number to be blacklisted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch_blacklist**
> FetchBlacklistSuccess fetch_blacklist()



Returns all blacklisted phone numbers.

### Example

* Basic Authentication (basicAuth): 
```python
from __future__ import print_function
import time
import phonebook_api
from phonebook_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = phonebook_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = phonebook_api.BlacklistApi(phonebook_api.ApiClient(configuration))

try:
    api_response = api_instance.fetch_blacklist()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BlacklistApi->fetch_blacklist: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FetchBlacklistSuccess**](FetchBlacklistSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_from_blacklist**
> remove_from_blacklist(phone_number)



Removes a phone number from the blacklist.

### Example

* Basic Authentication (basicAuth): 
```python
from __future__ import print_function
import time
import phonebook_api
from phonebook_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = phonebook_api.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = phonebook_api.BlacklistApi(phonebook_api.ApiClient(configuration))
phone_number = 'phone_number_example' # str | The phone number to be deleted

try:
    api_instance.remove_from_blacklist(phone_number)
except ApiException as e:
    print("Exception when calling BlacklistApi->remove_from_blacklist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone_number** | **str**| The phone number to be deleted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

