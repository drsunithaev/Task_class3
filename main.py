"""
class, object, constructor
inheritance
private, public, protected, abstraction
encaptulations
polymorpsim
package, modules

method overrridding

For all the concepts that we have discussed in our class point by point you have to write
atleast 10 examples

you have to make sure that use ineuron studnets , class , class type , number of courses
, affiliates , blog, internship , jobs as a reference example

"""
from ineuron import ineuron
from student import student
from blog import blog
import logging
from course import courses
from internship import internship



if __name__ == '__main__':
    try:
        logging.info("Creating object for ineuron class")
        i = ineuron("Sudhanshu", "Data Science")
        print(i.get_info())
        i.add_domain("Web Development")
        print(i.get_info())
        i.add_courses("Full Stack-1", 17000, 12)
        i.add_courses("Full Stack-2", 17000, 12)
        i.add_courses("Full Stack-3", 17000, 12)
        print(i.course_list())
    except Exception as e:
        logging.exception(e)

        logging.info("Creating object for student class")

        FSDS1 = student("Sunitha")
        print(FSDS1.get_stud_info())
        FSDS1.assign_regno(101)
        print(FSDS1.get_stud_info())

        logging.info("Creating a new blog")
        myblog = blog("Tourism", "www.blog.tourismblog.com\myblog")
        print(myblog.blog_info())
        myblog.write_content()
        print(myblog.blog_info())

