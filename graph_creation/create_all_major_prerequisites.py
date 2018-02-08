import file_util

filepath_bdict = "../data_collection/big_dict.txt"


path_major_requirements = "../data_collection/major_requirements/"
path_major_prerequisites = "../data_collection/major_prerequisites/"




def create_all_major_prerequisites(filepath_bdict, path_major_requirements, path_major_prerequisites):
    print("Creating Major Prerequisites...")
    majors_list = file_util.get_majors_list_from_file("../data_collection/major_names.txt")
    
    for major in majors_list:
        filename_in = major
        
        filename_out = major
        
        
        bdict = open(filepath_bdict, 'r')
        major_requirements = open(path_major_requirements + major + '.txt', 'r')
        major_prerequisites = open(path_major_prerequisites + major + '.txt', 'w')
        
        
        
        bdict_line_list = []
        major_line_list = []
        
        
        for bdict_line in bdict:
            bdict_line_split = bdict_line.split(':')
            
            bdict_line_list.append(bdict_line_split)
            
            major_line_scoped = ""
            for major_line in major_requirements:
                major_line = major_line.strip()
                major_line_scoped = major_line.replace("\n", "")
                major_line_scoped = major_line.replace(" ", "")
                major_line_scoped = major_line.replace(" ", "")
                
                major_line_list.append(major_line_scoped)
                
                
            
        
        major_requirements.close()
        bdict.close()
        
        
        for bdict_line in bdict_line_list:
            for major_line in major_line_list:
                if bdict_line[0] == major_line:
                    prerequisite_string = file_util.remove_spaces(bdict_line[1])
                    major_prerequisites.write(bdict_line[0] + ":" + prerequisite_string)
        
        
        
        major_prerequisites.close()
        
    print("Finished Creating Major Prerequisites")


