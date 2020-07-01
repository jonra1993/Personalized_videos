
import pandas as pd 
import mailchimp_python_function as mpf

client = MailChimp(
    mc_api='5c7105acb2d0019d9c5e30fb7a2da49d-us10', mc_user='JennyCGT')

data = pd.read_csv('inm.csv', sep=';', header = 0)

#print(data['Login_email'][1])

k = data['Login_email']
n = k.size
print(n)



for i in range(n):
    l = data['Login_email'][i]
    i += 1
    print(l)



#print(len(data['Login_email']))




#print(data.columns.tolist())
