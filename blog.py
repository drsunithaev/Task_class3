import logging

class blog:
    def __init__(self, title, url):
        """
        set Title and URL for the blog
        :param title: title of the Blog
        :param url: URL of the Blog
        """
        logging.info(f"Set title and url of the blog : {title}, {url}")
        self.__title = title
        self.__url = url
        self.content ="Welcome"

    def write_content(self):
        """
        Write content to the Blog
        :return: null
        """
        logging.info("write content for the blog")
        content = input("type the content here. DONT press enter till you finish")
        self.content = content

    def blog_info(self):
        """
        Returns blog information
        :return: Returns blog information
        """
        logging.info(f"Returns blog information {self.__title}, {self.__url}, {self.content}")
        return (self.__title, self.__url, self.content)
