# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def export_obj():
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
    a = mdb.models['Model-1'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.ModelFromInputFile(name='Cant1-13', 
        inputFileName='C:/Postprocessing-3D/Cant3D/Cant1-13.inp')
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
    a = mdb.models['Cant1-13'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    p = mdb.models['Cant1-13'].parts['PART-1']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.writeOBJFile(fileName='C:/Postprocessing-3D/Cant3D/Cant1-13_auto.obj', 
        canvasObjects= (session.viewports['Viewport: 1'], ))


