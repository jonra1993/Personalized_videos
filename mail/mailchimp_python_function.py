# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:08:48 2020

@author: sherangagamwasam
"""
import configure

from mailchimp3 import MailChimp
from string import Template

# =============================================================================
# authentication
# =============================================================================

MC_API_KEY = configure.MC_API_KEY
MC_USER_NAME = configure.MC_USER_NAME

client = MailChimp(
        mc_api = MC_API_KEY,
        mc_user = MC_USER_NAME)



# =============================================================================
#a audience creation
# =============================================================================
 

def audience_creation_function(audience_creation_dictionary, client=client):
        
        audience_creation = ''
        audience_creation_dictionary = audience_creation_dictionary
        print(audience_creation_dictionary)

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
            audience_creation = client.lists.create(data = audience_list)
        except Exception as error:
            print(error)
            
        return audience_creation


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

    return client.lists.merge_fields.create(list_id, data)


# =============================================================================
# add members to the existing audience function
# =============================================================================
def add_members_to_audience_function(
        audience_id, 
        email_list, 
        users_data,
        client=client):
        
        audience_id = audience_id
        email_list = email_list
        users_data = users_data

        if len(email_list)!=0:
            i=0
            for email_iteration in email_list:
                i += 1
                try:
                    data = {
                        "status": "subscribed",
                        "email_address": email_iteration,
                         'merge_fields': {
                             'FNAME': users_data[0][i-1],
                             'LNAME': users_data[1][i-1],
                             'URLVIDEO': users_data[2][i-1]
                            },
                    }

                    client.lists.members.create(list_id=audience_id, data=data)

                    print('{} has been successfully added to the {} audience'.format(email_iteration, audience_id))

                 

                except Exception as error:
                    print(error)
            

        else:
            print('Email list is empty')


# =============================================================================
# campaign creation function
# =============================================================================
def campaign_creation_function(campaign_name, audience_id, from_name, reply_to, client=client):
        
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
                "reply_to": reply_to
            },
            "type": "regular"
        }

        new_campaign = client.campaigns.create(data=data)
        
        return new_campaign
    
# =============================================================================
# 
# =============================================================================

def customized_template(html_code, campaign_id, client = client):
        
        html_code = html_code
        campaign_id = campaign_id

        string_template = Template(html_code).safe_substitute()
        
        try:
            client.campaigns.content.update(
                    campaign_id=campaign_id,
                    data={'message': 'Campaign message', 'html': string_template}
                    )
        except Exception as error:
            print(error)

# =============================================================================
# 
# =============================================================================

def send_mail(campaign_id, client = client):
        
        try:
            client.campaigns.actions.send(
                    campaign_id = campaign_id
                )
        except Exception as error:
            print(error)
