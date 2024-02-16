from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi"

response=requests.get(url)
htmlcontent=response.content

soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify())
# print(soup.title.string)
# for image in soup.find_all('img'):
#print(image.get('src'))

titles=[]
prices=[]

images=[]
data_list = []

for d in soup.find_all('div',attrs={'class':'_2kHMtA'}):

    title=d.find('div',attrs={'class':'_4rR01T'})
    print(title.string)

    price=d.find('div',attrs={'class':'_30jeq3 _1_WHN1'})
    print(price.string)



    image=d.find('img',attrs={'class':'_396cs4'})
    print(image.get('src'))

    titles.append(title.string)
    prices.append(price.string)

    images.append(image.get('src'))

    # print(titles)
    # print(prices)
    # print(images)

    data = {'Title': titles, 'Price': prices, 'Image': images}
    df = pd.DataFrame(data)
    df.to_excel('scraped_data.xlsx', index=False)

    print("Data saved to scraped_data.xlsx")