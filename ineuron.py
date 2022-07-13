import logging
import log.log_file
from course import courses

class ineuron:
    #constructor
    def __init__(self, ceo, domain):
        """
        creating ineuron object
        :param ceo:
        :param domain:
        """
        logging.info(f"iNeuron info-> ceo : {ceo}, domain : {domain}")
        self.__ceo = ceo             #private member
        self._domain = domain       #protected member
        self.course = []

    def change_ceo(self, new_ceo):
        """
        change the name of ceo
        :param new_ceo:
        :return:
        """
        logging.info(f"New CEO --> {new_ceo}")
        self.__ceo = new_ceo

    def add_domain(self, new_domain):
        """
        Add a new domain for the company
        :param new_domain:
        :return:
        """
        logging.info(f"new domain --> {new_domain}")
        #self._domain = list(self._domain)
        self._domain= self._domain+" and "+new_domain

    def get_info(self):
        """
        returns the company information
        :return:
        """
        logging.info(f"returns the company info {self.__ceo}, {self._domain}")
        return (self.__ceo, self._domain)

    def add_courses(self,n,f,d):
        """
        Add a new course to iNeuron
        :param n: course name
        :param f: course fee
        :param d: course duration in months
        :return: null
        """
        logging.info(f"New course details : {n},{f},{d}")
        obj=courses(n,f,d)
        print("New Course",obj)
        print("type of course :",type(self.course))
        self.course.append(obj)
        for i in self.course:
            print(i.course_info())


    def course_list(self):
        """
        Return list of courses offered by iNeuron
        :return: list of courses
        """
        logging.info(f"Return list of courses offered by iNeuron {self.course}")
        return self.course