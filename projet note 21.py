#!/usr/bin/env python
# coding: utf-8

# In[3]:


if __name__ == '__main__':

    import json
    import pandas as pd
    import numpy as np
    import numpy as np
    import matplotlib.pyplot as plt
    
    
    with open('888.txt') as json_data:
         data_dict = json.load(json_data)

 ###JSON: permet de stocker les données de manière organisée et lisible par l'utilisateur tout en y facilitant l’accès.


# In[273]:



"""
ouvrir le texte des donnes sous forme json pour l'échange de données, comme le languague java script.
Parameters
----------
data_dict : STR

Returns
-------
data_dict : STR
"""


# In[4]:



   
humidity_dataframe = pd.DataFrame(
data={
    '1: 1m/30cm [kPa]':data_dict[0]['datasets']['data'] ,
    '2: 1cm/30cm [kPa]': data_dict[1]['datasets']['data'],
    '3: 1cm/30cm [kPa]': data_dict[2]['datasets']['data'],
    },
    index=data_dict[1]['labels'],
    dtype='float'
    )


humidity_dataframe.index = pd.to_datetime(humidity_dataframe.index)

humidity_dataframe


# In[31]:


"""
reecrire les donnees sous forme de tableau de quatre colones.
Parameters
----------
none

Returns
-------
humidity_dataframe: table
"""


# In[16]:


def clean_data(data):
    
    humidity_dataframe = humidity_dataframe.replace([200.0], np.nan)
    return humidity_dataframe

### clean_data(data) c'est pour remplacer la valeur 200.0 par np.nan dans le tableau precedent (humidity_dataframe)


# In[ ]:


"""
remplacer la valeur 200.0 par np.nan
Parameters
----------
none

Returns
-------
humidity_dataframe: table
"""


# In[17]:



    
    
    

   
    plt.fig, ((x1,x2,x3))= plt.subplots(nrows = 3, ncols = 1, figsize=(10,10))

    
    x = np.linspace(0.0,100,50)

    
    
    plt.xlim(0,650)
    plt.xticks(np.linspace(0,650,7))
    
    plt.ylim(0,200)
    plt.yticks(np.linspace(0,200,5))

    y1 = data_dict[0]['datasets']['data']
    y2 = data_dict[1]['datasets']['data']
    y3=  data_dict[2]['datasets']['data']
    
    x1.plot(y1)
    x2.plot(y2)
    x3.plot(y3)

    plt.title("irrigation June 2020")
    plt.show()
    plt.savefig('june.png')




# In[21]:



    
    

   
    plt.fig, ((x1,x2,x3))= plt.subplots(nrows = 3, ncols = 1, figsize=(10,10))

    
    x = np.linspace(0.0,100,50)

    
    
    plt.xlim(650,1387)
    plt.xticks(np.linspace(650,1387,7))
    
    plt.ylim(0,200)
    plt.yticks(np.linspace(0,200,5))

    y1 = data_dict[0]['datasets']['data']
    y2 = data_dict[1]['datasets']['data']
    y3=  data_dict[2]['datasets']['data']
    
    x1.plot(y1)
    x2.plot(y2)
    x3.plot(y3)

    plt.title("irrigation July 2020")
    plt.show()
    plt.savefig('july.png')



# In[19]:



    
    
    

   
    plt.fig, ((x1,x2,x3))= plt.subplots(nrows = 3, ncols = 1, figsize=(10,10))

    
    x = np.linspace(0.0,100,50)

    
    
    plt.xlim(1387,1910)
    plt.xticks(np.linspace(1387,1910,7))
    
    plt.ylim(0,200)
    plt.yticks(np.linspace(0,200,5))

    y1 = data_dict[0]['datasets']['data']
    y2 = data_dict[1]['datasets']['data']
    y3=  data_dict[2]['datasets']['data']
    
    x1.plot(y1)
    x2.plot(y2)
    x3.plot(y3)
    
    plt.title("irrigation August 2020")
    plt.show()
    plt.savefig('August.png')


# In[2]:


pwd

