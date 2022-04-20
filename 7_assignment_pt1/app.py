# daniyal Tariq
from flask import Flask
import ghhops_server as hs

#notice, we import another file as a library
import geometry as geo

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/RandomGeometry",
    name = "Random Geometry",
    inputs=[
        hs.HopsInteger("Count", "Count", "Number of Random Points", hs.HopsParamAccess.ITEM, default= 4),
        hs.HopsNumber("X range of randomness", "X", "Maximum randomness in X directon", hs.HopsParamAccess.ITEM,default= 3),
        hs.HopsNumber("Y range of randomness", "Y", "Maximum randomness in Y directon", hs.HopsParamAccess.ITEM,default= 3),
        hs.HopsNumber("Z range of randomness", "Z", "Maximum randomness in Z directon", hs.HopsParamAccess.ITEM,default= 3 ),
        hs.HopsCurve("Curve", "Geo", "closed planar curve", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("add a height","height", "height of the extruded surface", hs.HopsParamAccess.ITEM, default= 3)

    ],
    outputs=[
        hs.HopsBrep("transformed geometry","Geometries"," breps", hs.HopsParamAccess.LIST),
        
        #hs.HopsLine("Story ","line"," volumetric breps", hs.HopsParamAccess.LIST)
    ]
)
def rmanyGeometry(count,rX, rY,rZ,Geo,height):

    shapes = geo.manyGeometry(count, rX, rY,rZ,Geo,height)
    return shapes


if __name__== "__main__":
    app.run(debug=True)