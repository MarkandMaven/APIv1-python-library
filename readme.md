Mark and Maven's API v1 Python Library

The Mark and Maven API exposes features via a standardized programmatic interface. Please refer to the full documentation to learn more. This is the wrapper for the API. 

Mark and Maven's API matches the OpenAPI v2 definition. The specification can be downloaded here.
# does it? wtf is this?

API version: 1.0.0
For more information, please visit https://www.markandmaven.com

Requirements.
Python 2.7 and 3.4+
# are these our reqs?

Installation & Usage
pip install
# how do you add a new API to pip? What's the alternative?

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
# how do we do all of this? I don't understand.

Getting Started

Please follow the installation procedure and then run the following:
from __future__ import print_function # what does this mean?
import time # do we need time?
import mam_api_v1_sdk # where does this directory point? What is an sdk? Have we / can we create one?
from mam_api_v1_sdk.rest import ApiException # what is the .rest suffix? do we have ApiException built in? How do we add it? Do we need it?
from pprint import pprint # wtf is pprint?

# Configure API key authorization: api-key
configuration = mam_api_v1_sdk.Configuration() # is a Configuration() f(x) somewhere in the codebase? will this work?
configuration.api_key['api-key'] = 'YOUR_API_KEY' # does this work? (maybe!)

# create an instance of the API class
api_instance = mam_api_v1_sdk.AccountApi(mam_api_v1_sdk.ApiClient(configuration)) # does the AccountApi() and ApiClient() f(x) exist?

try:
    # Get your account informations, plans and credits details
    api_response = api_instance.get_account()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account: %s\n" % e) # what does this bit of code mean? Esp. the %s

Documentation for API Endpoints
All URIs are relative to https://api.markandmaven.com/v1 # does this location exist? What creates it? How do we create it?

Class, Method, HTTP request, Description # what are the below for a fledgling MaM API?
AccountApi, get_account, GET /account, Get your account information, plans, and credits details 
AdminApi, create_account, POST /account, Create a user account
AdminApi, create_resume, POST /resume, Create a candidate resume
AdminApi, delete_account, DELETE /accounts/{email}, Deletes a contact
AdminApi, delete_resume, DELETE /resumes/{email}, Deletes a resume
DemosApi, get_demographics, GET /resumes/demographics, Lists all demographics
SkillsApi, get_skills, GET /resumes/skills, Lists all skills
AbilitiesApi, get_abilities, GET /resumes/abilities, Lists all abilities
AttributesApi, get_attributes, GET /resumes/attributes, Lists all attributes

Documentation For Models # what is this? what version of it do we want for Mam?
CreateAccount
CreateResume
GetAccount
GetResume

Documentation For Authorization # ???
api-key
Type: API key
API key parameter name: api-key
Location: HTTP header

Support and Feedback
Be sure to visit the Mark and Maven official documentation website for additional information about our API. # what IS our documentation website? 
If you find a bug, please post the issue on Github.

As always, if you need additional assistance, drop us a note here.

Author
systems@markandmaven.com