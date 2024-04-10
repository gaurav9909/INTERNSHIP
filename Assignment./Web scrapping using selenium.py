#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system(' pip install selenium')


# ##### 

# ##### 

# #  Question 1

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver = webdriver.Chrome()


# In[ ]:


driver.get("https://www.naukri.com/")


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,"suggestor-input ")
designation.send_keys("Data Scientist")


# In[ ]:


locations = driver.find_element(By.XPATH,"/html/body/div[1]/div[7]/div/div/div[5]/div/div/div/div[1]/div/input")
locations.send_keys("Delhi/NCR")


# In[ ]:


search=driver.find_element(By.CLASS_NAME,"qsbSubmit")
search.click()


# In[ ]:


job_title=[]
job_location=[]
compamy_name=[]
experience_requried=[]


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//div[@class="cust-job-tuple layout-wrapper lay-2 sjw__tuple "]/div/a')
for i in title_tags:
    title=i.text
    job_title.append(title)
job_title[:10]
    
locations_tags=driver.find_elements(By.XPATH,' //span[@ class="locWdth"]')
for i in locations_tags:
    locations=i.text
    job_location.append(locations)
job_location[:10]
    
company_tags=driver.find_elements(By.XPATH,'//div[@class=" row2"]/span/a[1]')
for i in company_tags:
    company=i.text
    compamy_name.append(company)
compamy_name[:10]
    
experience_tags=driver.find_elements(By.XPATH,'//span[@class="expwdth"]')
for i in experience_tags:
    exp=i.text
    experience_requried.append(exp)
experience_requried[:10]


# In[ ]:


print(len(job_title),len(job_location),len(compamy_name),len(experience_requried))


# In[ ]:


df=pd.DataFrame({'Title':job_title,'Location':job_location,'Company Name':compamy_name,'Experience':experience_requried})
df


# ##### 

# ##### 

# # Question 2

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome()
driver.get("https://www.shine.com/")


# In[ ]:


designation=driver.find_element(By.CLASS_NAME,"form-control  ")
designation.send_keys('Data Analyst')


# In[ ]:


locations = driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[1]/ul/li[2]/div/input")
locations.send_keys("Bangalore")


# In[ ]:


search=driver.find_element(By.XPATH,"/html/body/div/div[2]/div/div/div[1]/div[1]/div/div[2]/div/div/form/div/div[2]/div/button")
search.click()


# In[ ]:


job_title=[]
job_location=[]
company_name=[]
experience_required=[]


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
title_tags[0:10]
for i in title_tags[0:10]:
    title=i.text
    job_title.append(title)
    
location_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
location_tags[0:10]
for i in location_tags[0:10]:
    location=i.text
    job_location.append(location)
    
company_tags=driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
company_tags[0:10]
for i in company_tags[0:10]:
    company=i.text
    company_name.append(company)
    
experience_tags=driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
experience_tags[0:10]
for i in experience_tags[0:10]:
    experience=i.text
    experience_required.append(experience)


# In[ ]:


import pandas as pd
pd.DataFrame({'job_title':job_title,'job_location':job_location,'company_name':company_name,'experience_required':experience_required})


# ##### 

# ##### 

# # Question 3

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome()
driver.get("https://www.flipkart.com/")


# In[ ]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
search.send_keys('sneakers')


# In[ ]:


search_button=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button')
search_button.click()


# In[ ]:


Brands=[]
descriptions=[]
prices=[]


# In[ ]:


start=0
end=3
for page in range(start,end):
    Brand_tags=driver.find_elements(By.XPATH,'//div[@class="_2WkVRV"]')
    for i in Brand_tags:
        Brand=i.text
        Brands.append(Brand)
    description_tags=driver.find_elements(By.XPATH,'//a[@class="IRpwTa _2-ICcC" or @class="IRpwTa"]')
    for i in description_tags:
        description=i.text
        descriptions.append(description)
    price_tags=driver.find_elements(By.XPATH,'//div[@class="_30jeq3"]')
    for i in price_tags:
        price=i.text
        prices.append(price)
    next_button=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[2]/div[12]/div/div/nav/a[11]')
    next_button.click()
    time.sleep(3)


# In[ ]:


import pandas as pd
pd.DataFrame({'Brands':Brands,'descriptions':descriptions,'prices':prices})


# ##### 

# #### 

# # Question 5

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome()
driver.get("https://www.amazon.in/")


# In[ ]:


search=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input')
search.send_keys('Laptop')


# In[ ]:


search_button=driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input')
search_button.click()


# In[ ]:


Titles=[]
Ratings=[]
prices=[]


# In[ ]:


filter_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[8]/ul[19]/span/span[11]/li/span/a/div')
filter_button.click()


# In[ ]:


title_tags=driver.find_elements(By.XPATH,'//h2[@class="a-size-mini s-line-clamp-1"]/span')
title_tags[0:10]
for i in title_tags[0:10]:
    title=i.text
    Titles.append(title)
    
Ratings_tags=driver.find_elements(By.XPATH,'//a[@class="a-popover-trigger a-declarative"]/i[1]')
Ratings_tags[0:10]
for i in Ratings_tags[0:10]:
    Rating=i.text
    Ratings.append(Rating)
    
price_tags=driver.find_elements(By.XPATH,'//span[@class="a-price-whole"]')
price_tags[0:10]
for i in price_tags[0:10]:
    price=i.text
    prices.append(price)


# In[ ]:


import pandas as pd
pd.DataFrame({'Titles':Titles,'Ratings':Ratings,'prices':prices})


# ##### 

# ##### 

# # Question 6

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome()
driver.get("https://www.azquotes.com/")


# In[ ]:


search_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/div/div[3]/ul/li[5]/a')
search_button.click()


# In[ ]:


Quotes=[]
Authors=[]
Types=[]


# In[ ]:


start=0
end=3
for page in range(start,end):
    Quotes_tags=driver.find_elements(By.XPATH,'//ul[@class="list-quotes"]/li/div/p/a[2]')
    for i in Quotes_tags:
        Quote=i.text
        Quotes.append(Quote)
    Authors_tags=driver.find_elements(By.XPATH,'//div[@class="author"]')
    for i in Authors_tags:
        Author=i.text
        Authors.append(Author)
    Types_tags=driver.find_elements(By.XPATH,'//div[@class="tags"]')
    for i in Types_tags:
        Type=i.text
        Types.append(Type)
    next_button=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div/div/div[1]/div/div[3]/li[12]/a')
    next_button.click()
    time.sleep(3)


# In[ ]:


import pandas as pd
pd.DataFrame({'Quotes':Quotes,'Authors':Authors,'Types':Types})


# #### 

# ### 

# # Question 7

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome()
driver.get("https://www.jagranjosh.com/")


# In[ ]:


search_button=driver.find_element(By.XPATH,'/html/body/div/header/nav/div/div/div[3]/ul/li[3]/a')
search_button.click()


# In[ ]:


PM_list=driver.find_element(By.XPATH,'//a[@title="List of All Prime Ministers of India (1947-2024)"]')
PM_list.click()


# In[ ]:


PM_List=[]


# In[ ]:


PM_tags=driver.find_elements(By.XPATH,'//td[2][@valign="top"]')
for i in PM_tags:
    PM=i.text
    PM_List.append(PM)


# In[ ]:


import pandas as pd
pd.DataFrame({'PM_List':PM_List})


# ##### 

# #### 

# # Question 8

# In[ ]:


import selenium
import pandas as pd
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By
import time


# In[ ]:


driver=webdriver.Chrome()
driver.get("https://www.motor1.com/")


# In[ ]:


search_button=driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/input')
search_button.send_keys('’50 most expensive cars')


# In[ ]:


search=driver.find_element(By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/div/div/form/button[1]')
search.click()

After clicking above search query received output like content you are looking does not exist.
# In[ ]:


cars=[]


# In[ ]:


Car_tags=driver.find_elements(By.XPATH,'/html/body/div[1]/main/div[1]/div[1]/article/div[3]/div[5]/div/table/tbody/tr[6]/td[2]/div/strong/a')
for i in Car_tags:
    Car=i.text
    cars.append(Car)


# #### 
