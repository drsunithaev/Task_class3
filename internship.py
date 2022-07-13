import logging

class internship:
    def __init__(self):
        self.project = "Data Science"
        self.team = ["abc", "xyz"]
        self.start = '01.07.2022'
        self.end = '30.07.2022'

    def join_internship(self, p, t, s, e):
        """
        Join internship by providing the necessary information
        :param p: project name
        :param t: team members list
        :param s: start date
        :param e: end date
        :return: null
        """
        logging.info(f"Join internship by providing the necessary information {p},{t},{s}, {e}")
        self.project = p
        self.team = t
        self.start = s
        self.end = e
