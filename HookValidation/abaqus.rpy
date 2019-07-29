# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 2018 replay file
# Internal Version: 2017_11_08-04.21.41 127140
# Run by dliu81 on Tue May 21 11:31:18 2019
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=235.539566040039, 
    height=269.875)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='HD6-33.odb')
#: Model: C:/Users/dliu81/Google Drive/AdditiveManufacturing/PostProcessing_2D/HookValidation/HD6-33.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       8
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=131.522, 
    farPlane=141.793, width=67.256, height=30.7595, viewOffsetX=1.64256, 
    viewOffsetY=-1.1359)
o1 = session.openOdb(
    name='C:/Users/dliu81/Google Drive/AdditiveManufacturing/PostProcessing_2D/HookValidation/HD6-47.odb')
session.viewports['Viewport: 1'].setValues(displayedObject=o1)
#: Model: C:/Users/dliu81/Google Drive/AdditiveManufacturing/PostProcessing_2D/HookValidation/HD6-47.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     1
#: Number of Meshes:             1
#: Number of Element Sets:       7
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.odbs['C:/Users/dliu81/Google Drive/AdditiveManufacturing/PostProcessing_2D/HookValidation/HD6-33.odb'].close(
    )
#: 
#: Node: PART-1-1.874
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.45000e+01,  0.00000e+00,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PART-1-1.873
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.40000e+01,  0.00000e+00,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PART-1-1.874
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.45000e+01,  0.00000e+00,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PART-1-1.875
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.50000e+01,  0.00000e+00,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PART-1-1.876
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.55000e+01,  0.00000e+00,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PART-1-1.7597
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.50163e+01,  9.93433e-01,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
#: 
#: Node: PART-1-1.7449
#:                                         1             2             3        Magnitude
#: Base coordinates:                  1.45172e+01,  4.83632e-01,  5.00000e-01,      -      
#: No deformed coordinates for current plot.
