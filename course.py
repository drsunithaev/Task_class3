import logging

class courses:
    def __init__(self, cname, fee, duration):
        self.__cname = cname
        self.__fee = fee
        self.__duration = duration
        self.enrolled = []

    def change_fee(self, new_fee):
        """
        Change the fee amount
        :param new_fee: new fee amount
        :return: null
        """
        logging.info(f"Change the fee amount to {new_fee}")
        self.__fee = new_fee

    def change_duration(self, new_duration):
        """
        Change the duration of the course
        :param new_duration: New duration of the course
        :return: null
        """
        logging.info(f"Change the duration of the course to {new_duration}")
        self.__duration = new_duration

    def course_info(self):
        """
        Returns course information Name, Fee and Duration
        :return: Course name, fee, duration
        """
        logging.info(f"Returns course information Name: {self.__cname}, Fee: {self.__fee} and Duration: {self.__duration} ")
        return (self.__cname, self.__fee, self.__duration)

    def enroll(self,s):
        """
        Enroll students to the course
        :param s: student
        :return: null
        """
        logging.info(f"enroll students{s.name} to course {self.__cname}")
        self.enrolled.append(s)
