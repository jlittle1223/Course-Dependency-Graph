
import Courses
import bs4 as bs
import urllib.request
import re
import file_util


def write_big_dict(filepath = "big_dict.txt"):
    
    
    string = file_util.get_string_from_file("major_courses_urls.txt")
    
    ignore = ["Placement", "Satisfactory", "Satisfaction", "One", "Basic", "C++", "An", "Undergraduate-level", "Successful", "Prior",
              "Limited", "Three", "Completion", "Two", "High", "Recommended", "Advancement", "Prerequisites",
              "Student", "Prerequisite", "Corequisite", "Recommended:", "AP"]
    
    words_to_replace = [("I&C SCI", "I&CSCI"), ("Prerequisite: ", ''), ('\xa0', ''), ("I&amp;CSCI","I&CSCI")]
    
    
    f = open(filepath,"w")
    
    for url in string.split('\n'):
            source = urllib.request.urlopen(url).read()
    
            soup = bs.BeautifulSoup(source, 'lxml')
    
            tags = soup.find_all('p')
    
            course_list = []
            name = ''
            flag = False
            for tag in tags:
                if 'courseblocktitle' in str(tag):
                    pattern = re.compile('>([&;a-zA-Z0-9\s]+).')
                    m = pattern.search(str(tag))
                    name = str(m.group(1))
                    for pair in words_to_replace:
                        name = name.replace(pair[0], pair[1])
                if 'Prerequisite: ' in str(tag):
                    preq = tag.text
                    if "Corequisite" in preq:
                        print("COREQUISITE FOUND:", preq)
                        preq = preq.split('\n')[1]
                    for pair in words_to_replace:
                        preq = preq.replace(pair[0], pair[1])
                    
                    print("preq.split()[0] = {}".format(preq.split()[0]))
                    if preq.split()[0] in ignore:
                        print("{} IGNORED".format(preq.split()[0]))
                        pass
                    else:
                        course = Courses.Course(name, preq.rstrip('\n'))
                        course_list.append(course)
            for course in course_list:
                print("return info = {}".format(course.return_info()))
                f.write(course.return_info())
    
    f.close()
        
        

