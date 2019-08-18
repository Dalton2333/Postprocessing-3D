"""
sample for selection function:
mlx.select.face_function(mesh0, function='(r0==255)||(r1==255)||(r2==255)')
"""

import meshlabxml as mlx
import os

def mesh_smoothing(ap):
    meshlabserver_path = 'C:\\Program Files\\VCG\\MeshLab'
    os.environ['PATH'] = meshlabserver_path + os.pathsep + os.environ['PATH']
    obj_in = ap["test_dir_path"]+ap["inp_name"]+"_c.obj"
    obj_out = ap["test_dir_path"]+ap["inp_name"]+"_smooth.obj"
    mesh0 = mlx.FilterScript(file_in=obj_in, file_out=obj_out, ml_version='2016.12')
    # mlx.select.vert_function(mesh0, function='(r==255)',strict_face_select=False)
    mlx.select.face_function(mesh0, function='(r0==255)||(r1==255)||(r2==255)')
    # mlx.select.face_function(mesh0, function='(fr==255)')
    # mlx.delete.selected(mesh0)
    # mlx.select.face_function(mesh0, function='(abs(fi-5000)<1000)')
    mlx.smooth.taubin(mesh0, iterations=10, selected=True)
    mlx.smooth.laplacian(mesh0,iterations=1,selected=True)
    mlx.smooth.taubin(mesh0,iterations=100,selected=True)
    # mlx.smooth.laplacian(mesh0,iterations=5,selected=True)
    mesh0.run_script(log=ap["test_dir_path"]+"mesh0Log.txt")
    # orange_cube = mlx.FilterScript(file_out='orange_cube.ply', ml_version='2016.12')
    # mlx.create.cube(orange_cube, size=[3.0, 4.0, 5.0], center=True, color='orange')
    # mlx.transform.rotate(orange_cube, axis='x', angle=45)
    # mlx.transform.rotate(orange_cube, axis='y', angle=45)
    # mlx.transform.translate(orange_cube, value=[0, 5.0, 0])
    # orange_cube.run_script()
    #
if __name__ == '__main__':
    ap = {"test_dir_path":os.getcwd()+"/../../Cant3D/",
          "inp_name":"Cant1-13"}
    mesh_smoothing(ap)
