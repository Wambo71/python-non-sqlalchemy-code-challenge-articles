class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
        Article.all.append(self)#append the instance to the class level list

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed after initialization")
        if not isinstance(value, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(value.strip()) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    #setter prop
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value

     
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, "_name"):
            return
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if len(value.strip()) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        mags = self.magazines()
        if not mags:
            return None
        return list(set(mag.category for mag in mags))

class Magazine:
    #class variable
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(value.strip()) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value.strip()) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
      
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
      
        arts = self.articles()
        if not arts:
            return None
        return [art.title for art in arts]

    def contributing_authors(self):
      
        authors = self.contributors()
        result = [author for author in authors if len([a for a in self.articles() if a.author == author]) > 2] #return authors who have written more than 2 articles
        return result or None #return none if none exist

    @classmethod
    def top_publisher(cls): #returns magazines with most articles
        if not Article.all:
            return None    #returns none if no magazine that exist
        return max(cls.all, key=lambda mag: len(mag.articles()))