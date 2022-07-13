import logging

class student:

    __regNo = 0

    # constructor
    def __init__(self, name):
        """
        creating student object
        :param name: Student name
        :param course: Course info
        """
        logging.info(f"Student info-> name : {name}")
        self.name = name  # public members


    def assign_regno(self, rno):
        """
        Assign register number for the student
        :param rno: Register number
        :return: null
        """
        logging.info(f"Assign register number for the student : {rno}")
        self.__regNo = rno

    def get_stud_info(self):
        """
        :return: Return student's information
        """
        logging.info(f"Return student's information : {self.__regNo}, {self.name}")
        return (self.__regNo, self.name)


