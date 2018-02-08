import bs4 as bs
import urllib.request
import re
import file_util



def write_majors_to_file(filepath, majors_string):
    file = open(filepath, 'w')
    majors_list = majors_string.split('\n')
    for i in range(len(majors_list)):
        major_url = majors_list[i].split('/')
        major_name = major_url[3] + major_url[4]
        file.write(major_name + "\n")
        
    file.close()
    


def create_all_major_requirements(filepath = "../data_collection/major_requirements/"):
    print("Creating Major Requirements...")
    
    string = file_util.get_string_from_file("../data_collection/major_requirements_urls.txt")
    
    write_majors_to_file("../data_collection/major_names.txt", string)
    
    path = filepath
    for url in string.split('\n'):
        temp = url.split('/')
        file_name = temp[3] + temp[4]+ '.txt'
        print("Creating Requirements For Major: {}".format(file_name))
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source, 'lxml')
        
        f = open(path + file_name,'w')

        L = []
        flag = False
        for line in soup.body:
            line = str(line)
            temp = line.split('<')
            for i in temp:
                if ('Requirements for the B.' in i):
                    flag = True
                if flag:
                    L.append(i)

        courses = set()
        for i in L:
            if 'showCourse(this, ' in i:
                pattern = re.compile('title=\"([a-zA-z0-9\s&;]+)')
                m = pattern.search(i)
                if m:
                    courses.add(m.group(1))
                    
        for i in sorted(courses):
            i = i.replace('\\', '')
            i = i.replace('\xa0', '')
            i = i.replace('&amp;', '&')
            i = i.replace(' ', '')
            f.write(i + '\n')
        f.close()
            
    print("Finished Creating Major Requirements")
    
        
    

