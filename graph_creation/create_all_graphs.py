import file_util
from courseGraph import CourseGraph
import drawGraph
from create_all_major_prerequisites import create_all_major_prerequisites
from create_all_major_requirements import create_all_major_requirements



DRAW = False
TO_DOT = False
TO_PNG = True

path_in = "../data_collection/major_prerequisites/"

path_out = "../graphs/"





update_data = True


if __name__ == "__main__":
    if update_data:
        filepath_bdict = "../data_collection/big_dict.txt"
        path_major_requirements = "../data_collection/major_requirements/"
        path_major_prerequisites = "../data_collection/major_prerequisites/"
        create_all_major_requirements()
        create_all_major_prerequisites(filepath_bdict, path_major_requirements, path_major_prerequisites)
        
    
    
    majors_list = file_util.get_majors_list_from_file("../data_collection/major_names.txt")
    
    
    for major in majors_list:
        print("Creating graph for major: {}...".format(major))
        filename_in = major + '.txt'
        
        filename_out = major
        
        course_list = file_util.make_course_list_from_file(path_in + filename_in)
        
        g1 = CourseGraph([], [], course_list)
        
        if DRAW:
            drawGraph.draw_graph(g1)
        if TO_DOT:
            drawGraph.write_graph_to_dot(g1, path_out + filename_out)
        if TO_PNG:
            drawGraph.write_graph_to_png(g1, path_out + filename_out)
        
        print("Finished creating graph")

    print("All Finished!")

