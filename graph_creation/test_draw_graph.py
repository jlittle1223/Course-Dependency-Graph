import file_util
from courseGraph import CourseGraph
import drawGraph
from course import Course
import networkx as nx



filename_in = "TEST.txt"
path_in = ""

filename_out = "simple_graph"
path_out = "../graphs/" + filename_out

DRAW = True
TO_DOT = False
TO_PNG = True


if __name__ == "__main__":
    
    course_list = file_util.make_course_list_from_file(path_in + filename_in)
    
    g1 = CourseGraph([], [], course_list)
    
    
    
    if DRAW:
        drawGraph.draw_graph(g1)
        
    if TO_DOT:
        drawGraph.write_graph_to_dot(g1, path_out)
    if TO_PNG:
        drawGraph.write_graph_to_png(g1, path_out)



