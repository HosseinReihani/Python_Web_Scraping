#Importing necessary libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd

#Adding the URL of the Wiki page viewed on Feb 21, 2024
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

#After inspecting through the browser, I locate the companies table That
#I was looking for. Adding it's html code to "table"
table = soup.find_all('table')[0]

#Finding col names, after inspection through the web browser, it seems like "th"
#is the key locating the table headers
col_names = table.find_all('th')

#clean the html-related jargons to get the values
col_names_clean = [nm.text.strip() for nm in col_names]

#turned out that the first column (Rannk) is also coded as
#table header, and thus, I have to exclude them from the col_names
#print(col_names_clean[1:13])

#There's still one more step to do before finishing with the headers,
#and that is taking care of empty header values, and "USD millions"
# being put there as a header name
col_names_clean_filter = [item for item in col_names_clean[1:13] if item.strip() and item != 'USD millions' and item != 'Ref.']
col_names_clean_filter =[item.replace('[note 1]', '') for item in col_names_clean_filter]
col_names_clean = col_names_clean_filter


#checking wether the columns names are as they supposed to
#print(col_names_clean)

#Good! now making a data frame with these columns
df = pd.DataFrame(columns= col_names_clean)


#now I need to extract the actual data from the "table"
# seems like they can be flagged by "tr" as in table row
col_data = table.find_all('tr')




#this for-loop will append each table row ("tr") to our "df"
for row in col_data[2:]:
    row_data = row.find_all('td')
    each_row_data = [data.text.strip() for data in row_data]
    #taking out the Ref. useless data point
    each_row_data = each_row_data[:7] + each_row_data[8:]
    #turning the check and X marks into "yes" and "No" text values
    if row.find(class_="table-yes2"):
        each_row_data[6] = "Yes"
    elif row.find(class_="table-no2"):
        each_row_data[6] = "No"
    length = len(df)
    df.loc[length] = each_row_data


#now saving it to a csv file
df.to_csv(r'F:\Business Analytics\Knowledge\Py\Web Scrapping\Largest Companies Wiki\CSV result\Largest_Co_Wiki.csv')
