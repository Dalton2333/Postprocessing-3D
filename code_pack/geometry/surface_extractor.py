"""
Created 29/07/2019
author@Dedao
This module extract the surface elements and nodes from the part.
"""

import geometry.constants
import geometry.flat_geometry

def get_keep_set(ap, part):
    keep_set_name = ap['keep_set_name']
    keep_set = geometry.flat_geometry.get_set(keep_set_name, "nset", part)
    return keep_set.data


def get_surface_elements(ap,part):
    """
    Extract elements with neighbours<faces
    Problem: how to
    :param ap:
    :param part:
    :return:
    """
    surface_elements = []
    for el_label in part.elements:
        el = part.elements[el_label]
        for el_n_lbl in el.neighbours:
            el_n = part.elements[el_n_lbl]
            if el_n.initially_active:
                pass
            else:
                surface_elements.append(el_label)
    surface_elements = list(set(surface_elements))
    return surface_elements


def get_surface_nodes(ap,part):
    import itertools
    surface_nodes = {}
    surface_nodes_coords_list = []
    surface_elements = get_surface_elements(ap,part)
    for element_label in surface_elements:
        el = part.elements[element_label]
        for nd_label in el.nodes:
            nd = part.nodes[nd_label]
            # surface_nodes[nd_label] = nd.coordinates
            # surface_nodes_list.append(nd_label)
            coord = nd.coordinates
            surface_nodes_coords_list.append(list(coord))

    surface_nodes_coords_list.sort()
    surface_nodes_coords_list = list(k for k,_ in itertools.groupby(surface_nodes_coords_list))
    return surface_nodes, surface_nodes_coords_list



if __name__ == '__main__':
    pass

