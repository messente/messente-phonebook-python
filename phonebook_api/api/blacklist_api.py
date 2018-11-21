# coding: utf-8

"""
    Phonebook API

    RESTful API for Messente phonebook  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: messente@messente.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from phonebook_api.api_client import ApiClient


class BlacklistApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_to_blacklist(self, number_to_blacklist, **kwargs):  # noqa: E501
        """add_to_blacklist  # noqa: E501

        Adds a phone number to the blacklist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_to_blacklist(number_to_blacklist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NumberToBlacklist number_to_blacklist: Phone number to be blacklisted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_to_blacklist_with_http_info(number_to_blacklist, **kwargs)  # noqa: E501
        else:
            (data) = self.add_to_blacklist_with_http_info(number_to_blacklist, **kwargs)  # noqa: E501
            return data

    def add_to_blacklist_with_http_info(self, number_to_blacklist, **kwargs):  # noqa: E501
        """add_to_blacklist  # noqa: E501

        Adds a phone number to the blacklist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_to_blacklist_with_http_info(number_to_blacklist, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NumberToBlacklist number_to_blacklist: Phone number to be blacklisted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['number_to_blacklist']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_to_blacklist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'number_to_blacklist' is set
        if ('number_to_blacklist' not in local_var_params or
                local_var_params['number_to_blacklist'] is None):
            raise ValueError("Missing the required parameter `number_to_blacklist` when calling `add_to_blacklist`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'number_to_blacklist' in local_var_params:
            body_params = local_var_params['number_to_blacklist']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phonebook/blacklist', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_blacklist(self, **kwargs):  # noqa: E501
        """fetch_blacklist  # noqa: E501

        Returns all blacklisted phone numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_blacklist(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FetchBlacklistSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.fetch_blacklist_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.fetch_blacklist_with_http_info(**kwargs)  # noqa: E501
            return data

    def fetch_blacklist_with_http_info(self, **kwargs):  # noqa: E501
        """fetch_blacklist  # noqa: E501

        Returns all blacklisted phone numbers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_blacklist_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: FetchBlacklistSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_blacklist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phonebook/blacklist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FetchBlacklistSuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_from_blacklist(self, phone_number, **kwargs):  # noqa: E501
        """remove_from_blacklist  # noqa: E501

        Removes a phone number from the blacklist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_from_blacklist(phone_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone_number: The phone number to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.remove_from_blacklist_with_http_info(phone_number, **kwargs)  # noqa: E501
        else:
            (data) = self.remove_from_blacklist_with_http_info(phone_number, **kwargs)  # noqa: E501
            return data

    def remove_from_blacklist_with_http_info(self, phone_number, **kwargs):  # noqa: E501
        """remove_from_blacklist  # noqa: E501

        Removes a phone number from the blacklist.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_from_blacklist_with_http_info(phone_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str phone_number: The phone number to be deleted (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['phone_number']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_from_blacklist" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'phone_number' is set
        if ('phone_number' not in local_var_params or
                local_var_params['phone_number'] is None):
            raise ValueError("Missing the required parameter `phone_number` when calling `remove_from_blacklist`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'phone_number' in local_var_params:
            path_params['phone_number'] = local_var_params['phone_number']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/phonebook/blacklist/{phone_number}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)