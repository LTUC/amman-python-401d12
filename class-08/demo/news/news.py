import requests
from rich import print

class News:

    _instance = None
    _main_url = "https://newsapi.org/v1/articles"
    _query_params = {
        "apiKey" : "da8a28f85868470f8ebbb65f1679bfd0"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(News, cls).__new__(cls)
            cls._instance._initalize()
        return cls._instance
    
    @staticmethod
    def instance():
        if News._instance is None:
            News()
        return News._instance
    
    def _initalize(self):
        try:
            # https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=da8a28f85868470f8ebbb65f1679bfd0
            response = requests.get(News._main_url, params={"source": "bbc-news", "sortBy": "top", **News._query_params})
            response.raise_for_status() # if the request did not succeed , this method will raise an HTTPErorr exception
            self._articles = response.json().get("articles", [])
        except requests.RequestExceptions as e:
            print("Error in fetching the data")
            self._articles = []
    

    def print_latest(self, news=None):
        if news is None:
            news = self._articles
        for article in news[:3]:
            print("[bold blue]===================================[/bold blue]")
            print(f"title: {article['title']}")
            print(f"description: {article['description']}")
            print(f"url: {article['url']}")

    def set_query(self,query):
        self._query = query

    def get_query(self):
        return self._query
    
    def set_country(self,country):
        self._country = country

    def get_country(self):
        return self._country
    
    def set_category(self, category):
        self._category = category

    def get_category(self):
        return self._category


    def search_news(self):
        #https://newsapi.org/v2/everything?q=apple&apiKey=da8a28f85868470f8ebbb65f1679bfd0
        try:
            url = "https://newsapi.org/v2/everything"
            response = requests.get(url, params = {"q":self._query, **News._query_params})
            self._searched_articles = response.json().get("articles", [])
            self.print_latest(self._searched_articles)
        except:
            print("[bold red]Error in fetching the data[/ bold red]")
            self._searched_articles = []

    def get_country_news(self):
        try:
            url="https://newsapi.org/v2/top-headlines"
            res = requests.get(url, params={"country":self._country, "category": self._category, **News._query_params})
            self._country_news = res.json().get("articles", [])
            self.print_latest(self._country_news)
        except:
            print("[bold red]Error in fetching the data[/ bold red]")
            self._country_news = []


    
# Testing

news_instance = News.instance()
# news_instance.print_latest()
# news_instance.set_query("car")
# news_instance.search_news()
news_instance.set_category("health")
news_instance.set_country("us")
news_instance.print_latest()

