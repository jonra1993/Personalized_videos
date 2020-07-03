# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 08:05:48 2020

@author: sherangagamwasam
"""
import mailchimp_python_function as mpf
import newsletter_template
import pandas as pd 

# =============================================================================
# audience creation
# =============================================================================

audience_creation_dictionary = {
    "audience_name" : "Test1",
    "company" : "ENter",
    "address1" : "Tumbaco",
    "city" :  "QUito",
    "state" : "UNo",
    "zip_code" : "593",
    "country" : "EC", # FOR SRI LANKA : USE LK
    "from_name" : "Dario",
    "from_email" : "41latino.forever@gmail.com",
    "language" : "en"
}    
    
audience_creation = mpf.audience_creation_function(audience_creation_dictionary)

# =============================================================================
# add members to the existing audience 
# =============================================================================
data = pd.read_csv('inm.csv', sep=';', header=0)
k = data['Login_email']
n = k.size

my_list = []

for i in range(n):
    my_list.append(data['Login_email'][i])
    i += 1

email_list = my_list

audience_id = audience_creation['id']
# add the email list here



print(email_list)

mpf.add_members_to_audience_function(
    audience_id = audience_creation['id'],
    email_list = email_list)

# =============================================================================
# campaign creation
# =============================================================================

campaign_name = 'Bienvenida'
from_name = 'Dario'
reply_to = '41latino.foreverdc@gmail.com' # test1@gmail.com

campaign = mpf.campaign_creation_function(campaign_name=campaign_name,
                                      audience_id=audience_creation['id'],
                                      from_name=from_name,
                                      reply_to=reply_to)
                                    

# =============================================================================
# news letter tempates creation
# =============================================================================

html_code = newsletter_template.html_code           

mpf.customized_template(html_code=html_code, 
                    campaign_id=campaign['id'])

# =============================================================================
# send the mail campaign
# =============================================================================

mpf.send_mail(campaign_id=campaign['id'])           
