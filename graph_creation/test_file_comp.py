import file_util

filepath_bdict = "../data_collection/big_dict.txt"
filepath_major = "../data_collection/major_requirements/donaldbrenschoolofinformationandcomputersciencesdepartmentofcomputerscience.txt"
filepath_new = "../data_collection/major_prerequisites/donaldbrenschoolofinformationandcomputersciencesdepartmentofcomputerscience.txt"





        
if __name__ == "__main__":
    
    
    
    
    
    bdict = open(filepath_bdict, 'r')
    major = open(filepath_major, 'r')
    major_prerequisites = open(filepath_new, 'w')
    
    
    
    bdict_line_list = []
    major_line_list = []
    
    
    for bdict_line in bdict:
        bdict_line_split = bdict_line.split(':')
        
        bdict_line_list.append(bdict_line_split)
        
        major_line_scoped = ""
        for major_line in major:
            major_line = major_line.strip()
            major_line_scoped = major_line.replace("\n", "")
            major_line_scoped = major_line.replace(" ", "")
            major_line_scoped = major_line.replace(" ", "")
            
            major_line_list.append(major_line_scoped)
            
            
        
    
    major.close()
    bdict.close()
    
    
    for bdict_line in bdict_line_list:
        for major_line in major_line_list:
            if bdict_line[0] == major_line:
                prerequisite_string = file_util.remove_spaces(bdict_line[1])
                major_prerequisites.write(bdict_line[0] + ":" + prerequisite_string)
    
    
    
    major_prerequisites.close()
    
    








