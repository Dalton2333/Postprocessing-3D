from shutil import copyfile
from math import ceil
import numpy as np
import time

def vertex_on_surface(vertex,nodes,ap):
    """
    This function tries to locate the vertex to its closest node.
    nodes is a list of coordinates: [[x0,y0,z0],[x1,y1,z1],[x2,y2,z2]]
    nodes is sorted in an ascending order.
    vertex is a point coordinates: [xa,ya,za]
    need to find the closest node to the vertex
    :param vertex:
    :param nodes:
    :return:
    """
    # time0 = time.time()
    print("checking vertex",vertex)
    # nodes.sort()
    # matching_point = [None,None,None]
    # time1 = time.time()
    gap = ap['element_size']*0.001
    # time2 = time.time()
    # nodes = np.array(nodes)
    # time3 = time.time()
    vertex = np.array(vertex)
    # time4 = time.time()
    dst = np.linalg.norm(np.subtract(nodes,vertex),axis=1)
    # time5 = time.time()
    dst_min = np.amin(dst)
    # time6 = time.time()
    # dst_min_size = np.linalg.norm(dst_min)
    # timers = [time1-time0,time2-time1,time3-time2,time4-time3,time5-time4,time6-time5]
    # with open(ap["test_dir_path"]+"timer.txt","a+") as f:
    #     f.write(str(timers).strip("[").strip("]")+"\n")
    if dst_min < gap:
        return True
    else:
        return False

def vertex_on_surface_1(vertex,nodes,ap):
    """
    This function tries to locate the vertex to its closest node.
    nodes is a list of coordinates: [[x0,y0,z0],[x1,y1,z1],[x2,y2,z2]]
    nodes is sorted in an ascending order.
    vertex is a point coordinates: [xa,ya,za]
    need to find the closest node to the vertex
    :param vertex:
    :param nodes:
    :return:
    """
    print("checking vertex",vertex)
    # nodes.sort()
    # matching_point = [None,None,None]
    gap = ap['element_size']*0.001
    nodes = np.array(nodes)
    vertex = np.array(vertex)
    dst = np.linalg.norm(np.subtract(nodes,vertex),axis=1)
    dst_min = np.amin(dst)
    # dst_min_size = np.linalg.norm(dst_min)
    if dst_min < gap:
        return True
    else:
        return False

def add_color(ap,surf_nodes):
    surf_nodes = np.array(surf_nodes)
    # obj_color_path = ap['test_dir_path']+ap['inp_name']+'c.obj'
    # copyfile(ap['obj_path'], obj_color_path)
    test_path = ap['test_dir_path']
    with open(test_path+ap['inp_name']+'.obj','r') as f:
        lines = f.readlines()
        f.close()

    with open(test_path+ap['inp_name']+'_c.obj','w') as f:
        for idx in range(len(lines)):
            line = lines[idx]
            if line[:2] == "v ":
                vertex = line.strip("v").strip().split()
                vertex = [float(vertex[0]), float(vertex[1]), float(vertex[2])]
                if vertex_on_surface(vertex, surf_nodes, ap):
                    lines[idx]=line.strip()+" 1 0 0"+"\n"
                else:
                    lines[idx]=line.strip()+" 0 0 0"+"\n"
            else:
                pass
        for line in lines:
            f.write(line)
        f.close()







