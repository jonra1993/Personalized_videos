
import pandas as pd 

data = pd.read_csv('inm.csv', sep=';', header = 0)

#print(data['Login_email'][1])

k = data['Login_email']
n = k.size
print(n)

my_list = []

for i in range(n):
    my_list.append(data['Login_email'][i])
    i += 1

my_love = my_list
a = len(my_love)
print(a) 



#print(len(data['Login_email']))




#print(data.columns.tolist())
