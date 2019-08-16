# -*- coding: utf-8 -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
# a = mdb.models['Model-1'].rootAssembly
# session.viewports['Viewport: 1'].setValues(displayedObject=a)

mdb.ModelFromInputFile(name='the_inp_name',
    inputFileName='the_inp_path')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['the_inp_name'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
p = mdb.models['the_inp_name'].parts['PART-1'.upper()]
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.writeOBJFile(fileName='the_test_dir_path'+'the_inp_name'+'.obj',
    canvasObjects= (session.viewports['Viewport: 1'], ))



