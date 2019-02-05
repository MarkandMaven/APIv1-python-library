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
		# code belongs here? who knows what it do __--_OO_--__
		return self.api_client.call_api(
			'/accounts', 'POST',
			path_params,
			query_params,
			header_params,
			body=body_params,
			post_params=form_params,
			files=local_var_files,
			response_type='CreateAccount',
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