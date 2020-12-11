# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:08:48 2020

@author: sherangagamwasam
"""

import apps.send_email.configure as configure

# from mailchimp3 import MailChimp
from string import Template
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
import os
from dotenv import load_dotenv

load_dotenv()
# =============================================================================
# authentication
# =============================================================================

MC_API_KEY = os.getenv('MC_API_KEY'),
MC_USER_NAME = os.getenv('MC_USER_NAME')
MC_SERVER = os.getenv('MC_SERVER')

mailchimp =Client()
mailchimp.set_config({
  "api_key": os.getenv('MC_API_KEY'),
  "server": os.getenv('MC_SERVER')
})


# response = mailchimp.ping()
# print(response)

# =============================================================================
#a audience creation
# =============================================================================
 

def audience_creation_function(audience_creation_dictionary, client=mailchimp):
        # audience_creation = ''
        # audience_creation_dictionary = audience_creation_dictionary
        # print(audience_creation_dictionary)

        audience_list = {
            "name": audience_creation_dictionary['audience_name'],
            "contact":
            {
                "company": audience_creation_dictionary['company'],
                "address1": audience_creation_dictionary['address1'],
                "city": audience_creation_dictionary['city'],
                "state": audience_creation_dictionary['state'],
                "zip": audience_creation_dictionary['zip_code'],
                "country": audience_creation_dictionary['country']
            },
            "permission_reminder": audience_creation_dictionary['audience_name'],
            "campaign_defaults":
            {
                "from_name": audience_creation_dictionary['from_name'],
                "from_email": audience_creation_dictionary['from_email'],
                "subject": "",
                "language": audience_creation_dictionary['language']
            },
            
                     
            "email_type_option": False
        }


        try:
            response = mailchimp.lists.create_list(audience_list)
            print("Response: {}".format(response))
            return response
        except ApiClientError as error:
            print("An exception occurred: {}".format(error.text))
            return error
    # try:
        #     audience_creation = client.lists.create_list(audience_list)

        # except Exception as error:
        #     print(error)
            


# =============================================================================
# add merge fields
# =============================================================================
def add_mergefield(tag,name,field_type,default_value,list_id):

    list_id=list_id
    data = {
            "name": name,
            "type": field_type,
            "tag": tag,
            "public": True,
            "default_value": default_value,
        }
    try:
        response = mailchimp.lists.add_list_merge_field(list_id,data)
        print("Response: {}".format(response))
        return response
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        return None


# =============================================================================
# add members to the existing audience function
# =============================================================================

def add_members_to_audience_function(audience_id, member):

    try:
            # print(member1)
        response = mailchimp.lists.add_list_member(audience_id, member)
        print("response: {}".format(response))
        return response
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        return error
        

# =============================================================================
# campaign creation function
# =============================================================================
def campaign_creation_function(campaign_name, audience_id, from_name, reply_to, template_id,client=mailchimp):
        
    campaign_name = campaign_name
    audience_id = audience_id
    from_name = from_name
    reply_to = reply_to

    data = {
        "recipients" :
        {
            "list_id": audience_id
        },
        "settings":
        {
            "subject_line": campaign_name,
            "from_name": from_name,
            "reply_to": reply_to,
            "template_id": template_id
        },
        "type": "regular"
    }

    try:
        new_campaign = client.campaigns.create(data)
        # print(response)
        return new_campaign
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        return error


    
    
# =============================================================================
# 
# =============================================================================

def customized_template(html_code, name):
        
    html_code = html_code

    string_template = Template(html_code).safe_substitute()
    
    try:
        response = mailchimp.templates.create({"name": name, "html": html_code})
        # print(response)
        return response
    except ApiClientError as error:
        print("Error: {}".format(error.text))           

# =============================================================================
# 
# =============================================================================

def send_mail(campaign_id, client = mailchimp):
        
    try:
        response = client.campaigns.send(campaign_id)
        # print(response)
        
    except ApiClientError as error:
        print(error)

def delete_audience(audience_id, client = mailchimp):
    try:
        response = client.lists.delete_list(audience_id)
        # print(response)
        
    except ApiClientError as error:
        print(error)
