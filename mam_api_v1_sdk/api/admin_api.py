"""
	Mark and Maven API
	Contact: systems@markandmaven.com
"""

import re
import six
from mam_api_v1_sdk.api_client import ApiClient

class AdminApi(object):

	def __init__(self, api_client=None):
		if api_client is None:
			api_client = ApiClient()
		self.api_client = api_client

	def create_account():
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_account_with_http_info(**kwargs)
        else:
            (data) = self.add_contact_to_list_with_http_info(**kwargs)
            return data

	def create_account_with_http_info(self, **kwargs):
		all_params = []
		all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        params = locals()

        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_account_with_http_info" % key
                )
            params[key] = val

        del params['kwargs']

        if ('list_id' not in params or params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `create_account_with_http_info`")

        collection_formats = {}
        path_params = {}
        query_params = []
        header_params = {}
        form_params = []
        local_var_files = {}
        body_params = None

        if 'user_email' in params:
            body_params = params['user_email']

        header_params['Accept'] = self.api_client.select_header_accept(['application/json'])
        header_params['Content-Type'] = self.api_client.select_header_content_type(['application/json'])
        auth_settings = ['api-key']

		return self.api_client.call_api(
			'/accounts', 'POST',
			path_params,
			query_params,
			header_params,
			body=body_params,
			post_params=form_params,
			files=local_var_files,
			response_type='CreateResume',
			auth_settings=auth_settings,
			async=params.get('async'),
			_return_http_data_only=params.get('_return_http_data_only'),
			_preload_content=params.get('_preload_content', True),
			_request_timeout=params.get('_request_timeout'),
			collection_formats=collection_formats
		)

	def create_resume():
		# code belongs here? who knows what it do __--_OO_--__
		return self.api_client.call_api(
			'/resumes', 'POST',
			path_params,
			query_params,
			header_params,
			body=body_params,
			post_params=form_params,
			files=local_var_files,
			response_type='CreateResume',
			auth_settings=auth_settings,
			async=params.get('async'),
			_return_http_data_only=params.get('_return_http_data_only'),
			_preload_content=params.get('_preload_content', True),
			_request_timeout=params.get('_request_timeout'),
			collection_formats=collection_formats
		)