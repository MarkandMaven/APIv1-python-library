# APIv1-python-library
Python tools for modern hiring

Mark and Maven's API exposes the library via a standardized programmatic interface.

This is the wrapper for the API. It implements all the features of the API v1.

This PYTHON package is reviewed and maintained by Mark and Maven:
API version: 1.0.0

For more information, please visit https://www.markandmaven.com

Requirements.
Python 2.7 and 3.4+

###
Installation & Usage
pip install
If the python package is hosted on Github, you can install directly from Github
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
(you may need to run pip with root permission: sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git)
Then import the package:
import sib_api_v3_sdk 
Setuptools
Install via Setuptools.
python setup.py install --user
(or sudo python setup.py install to install the package for all users)
Then import the package:
import sib_api_v3_sdk
Getting Started
Please follow the installation procedure and then run the following:
from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))

try:
    # Get your account informations, plans and credits details
    api_response = api_instance.get_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account: %s\n" % e)
