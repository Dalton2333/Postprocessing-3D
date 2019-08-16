import os
import numpy

dir_path = os.path.dirname(os.path.realpath(__file__))
#dir_path = os.getcwd()
test_dir_path = dir_path+'/'
code_dir_path = test_dir_path + 'code_pack/'

# ------------Following are parameters for Impeller-------------
inp_name = 'Cant1-13'
inp_path = test_dir_path + inp_name+'.inp'
obj_path = test_dir_path + inp_name+'.obj'
cae_name = 'CRing_Circles.cae'
jnl_name = 'CRing_Circles.jnl'
initial_model_name = 'Model-1'
part_name = "Part-1"
cross_section_set_name = 'cross_section'
keep_set_name = 'keep_set'
# cross_section_normal = numpy.array([1,0,0])
cross_section_normal = None
element_shape = 'C3D8R'
element_size = 1
element_layers = 'single_layer'  # 'single_layer'  or  'multi_layer'
model_dimension = 32.863
initial_step_length = model_dimension*0.05
# Following is the model info of containment ring
boundary_points = [(0,0),(15,0),(15,36),(13,34),(11,34),(10,36),
                   (8,36),(8,35),(7,35),(7,31),(6,31),(6,36),
                   (4,36),(4,30),(3,30),(3,36),(0,36)]
voids_list = [[1, 11.333, 30.167, 1.382, 0, 0],
              [2, 6.5, 28.5, 0.564, 0, 0],
              [3, 11.3, 26.1, 1.262, 0, 0],
              [4, 8.5, 24.5, 0.564, 0, 0],
              [5, 11.167, 19.833, 0.977, 0, 0],
              [6, 9.333, 15.333, 1.382, 0, 0],
              [7, 9, 9.5, 1.382, 0, 0],
              [8, 5.667, 2.167, 1.382, 0, 0],
              [9, 10.5, 3, 0.798, 0, 0]]
# list of all voids in [[no,x,y,r,global_max_stress,round_count],[no,x,y,r,stress,round_count]] format
penalty_factor = 0.6
group_size = 8 # number of tests in one parallel simulation
min_step_length = 0.1 #mm
void_dst = 1
starting_dimension = 12


# -----------------------Following are parameters for Cantilever------------------------
# inp_path = test_dir_path + 'Cant4.inp'
# cae_name = 'CRing_Circles.cae'
# jnl_name = 'CRing_Circles.jnl'
# initial_model_name = 'Model-1'
# part_name = "PART-1"
# cross_section_set_name = 'cross_section'
# # cross_section_normal = numpy.array([1,0,0])
# cross_section_normal = None
# element_shape = 'C3D8R'
# element_layers = 'single_layer'  # 'single_layer'  or  'multi_layer'
#
# model_dimension = 32.863
# initial_step_length = model_dimension*0.05
# # Following is the model info of containment ring
# boundary_points = [(0,0),(15,0),(15,36),(13,34),(11,34),(10,36),
#                    (8,36),(8,35),(7,35),(7,31),(6,31),(6,36),
#                    (4,36),(4,30),(3,30),(3,36),(0,36)]
#
# voids_list = [[1, 11.333, 30.167, 1.382, 0, 0],
#               [2, 6.5, 28.5, 0.564, 0, 0],
#               [3, 11.3, 26.1, 1.262, 0, 0],
#               [4, 8.5, 24.5, 0.564, 0, 0],
#               [5, 11.167, 19.833, 0.977, 0, 0],
#               [6, 9.333, 15.333, 1.382, 0, 0],
#               [7, 9, 9.5, 1.382, 0, 0],
#               [8, 5.667, 2.167, 1.382, 0, 0],
#               [9, 10.5, 3, 0.798, 0, 0]]
# # list of all voids in [[no,x,y,r,global_max_stress,round_count],[no,x,y,r,stress,round_count]] format
# penalty_factor = 0.6
# group_size = 8 # number of tests in one parallel simulation
# min_step_length = 0.1 #mm
# void_dst = 1
# starting_dimension = 12

ap = {'dir_path':dir_path,
      'test_dir_path':test_dir_path,
      'code_dir_path':code_dir_path,
      'inp_name':inp_name,
      'inp_path':inp_path,
      'obj_path':obj_path,
      'model_space':'3D',
      'cae_name':cae_name,
      'jnl_name':jnl_name,
      'initial_model_name':initial_model_name,
      'part_name':part_name,
      'cross_section_set_name':cross_section_set_name,
      'keep_set_name':keep_set_name,
      'cross_section_normal':cross_section_normal,
      'element_shape':element_shape,
      'element_layers': element_layers,
      'element_size':element_size,
      'model_dimension':model_dimension,
      'initial_step_length':initial_step_length,
      'boundary_points':boundary_points,
      'voids_list':voids_list,
      'penalty_factor':penalty_factor,
      'group_size':group_size,
      'min_step_length':min_step_length,
      'void_dst':void_dst,
      'starting_dimension':starting_dimension}

if __name__ == '__main__':
    print(dir_path)
    print(test_dir_path)
    print(code_dir_path)
