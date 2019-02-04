Mark and Maven's API v1 Python Library

The Mark and Maven API exposes features via a standardized programmatic interface. Please refer to the full documentation to learn more. This is the wrapper for the API. 

API version: 1.0.0
For more information, please visit https://www.markandmaven.com

Getting Started

Documentation for API Endpoints
All URIs are relative to https://api.markandmaven.com/v1 

Class, Method, HTTP request, Description 
AccountApi, get_account, GET /account, Get your account information, plans, and credits details 
AdminApi, create_account, POST /account, Create a user account
AdminApi, create_resume, POST /resume, Create a candidate resume
AdminApi, delete_account, DELETE /accounts/{email}, Deletes a contact
AdminApi, delete_resume, DELETE /resumes/{email}, Deletes a resume
DemosApi, get_demographics, GET /resumes/demographics, Lists all demographics
SkillsApi, get_skills, GET /resumes/skills, Lists all skills
AbilitiesApi, get_abilities, GET /resumes/abilities, Lists all abilities
AttributesApi, get_attributes, GET /resumes/attributes, Lists all attributes

Documentation For Models
CreateAccount
CreateResume
GetAccount
GetResume

Documentation For Authorization
api-key
Type: API key
API key parameter name: api-key
Location: HTTP header

Author
systems@markandmaven.com
