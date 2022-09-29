# as the returning output will be in the form of a dictionary so I will convert it into a pandas DataFrame

from GoogleNews import GoogleNews
news = GoogleNews(period='1d')
news.search("Argentina")
result = news.result()
import pandas as pd
data = pd.DataFrame.from_dict(result)
data = data.drop(columns=["img"])
data.head() 


#click on the links to read the complete news
for i in result:
    print("Title : ", i["title"])
    print("News : ", i["desc"])
    print("Read Full News : ", i["link"])
