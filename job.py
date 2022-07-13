import logging

class jobs:
    def __init__(self, title, salary):
        logging.info(f"Job Profile : {title}, {salary}")
        self.__title = title
        self.__salary = salary
    def increment(self, hike):
        """
        Increment in salary
        :param hike:
        :return:
        """
        logging.info(f"Increment in salary by the amount {hike}")
        self.__salary = self.__salary+hike
    def job_info(self):
        """
        Returns job information (title, salary)
        :return:  (title, salary)
        """
        logging.info(f"Returns job information (title: {self.__title}, salary : {self.__salary})")
        return (self.__title, self.__salary)

