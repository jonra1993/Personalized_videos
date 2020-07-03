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
    "audience_name" : "Testing JRTEC",
    "company" : "Jrtec",
    "address1" : "Los 2 Puentes",
    "city" :  "Quito",
    "state" : "UNo",
    "zip_code" : "593",
    "country" : "EC", # FOR SRI LANKA : USE LK
    "from_name" : "Tester1",
    "from_email" : "cristhianepncobos@gmail.com",
    "language" : "es"
}    
   
audience_creation = mpf.audience_creation_function(audience_creation_dictionary)
# add merge fields
merge_creation = mpf.add_mergefield('URLVIDEO','Video usuario', 'url','',audience_creation['id'])
print(merge_creation)
# =============================================================================
# add members to the existing audience 
# =============================================================================
data = pd.read_csv('inm.csv', sep=';', header=0)
k = data['Login_email']
n = k.size

my_list = []
first_name = []
last_name = []
Url_video = []
users_data = []

for i in range(n):
    my_list.append(data['Login_email'][i])
    first_name.append(data['First name'][i])
    last_name.append(data['Last name'][i])
    Url_video.append(data['URL'][i])
    i += 1

email_list = my_list
users_data = [first_name,last_name,Url_video,]
print(users_data[2])


print(email_list)

# audience_id = audience_creation['id']
# add the email list here



mpf.add_members_to_audience_function(
    audience_id = audience_creation['id'],
    email_list = email_list,
    users_data = users_data)

# =============================================================================
# campaign creation
# =============================================================================

campaign_name = 'Primera prueba de envio' #asunto
from_name = 'Tester 1' #mensaje de nombre
reply_to = 'cristhianepncobos@gmail.com' # test1@gmail.com  correo que envia el mensaje

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
