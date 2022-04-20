#we import all the libraries that our functions need here too
import random as r
import rhino3dm as rg

def manyGeometry(count,rX, rY,rZ,Geo, height):

    shapes =[]
    cubes1=[]
    #lines= []
    for i in range(count):

        #in each itereation generate some random points
        random_x = r.uniform(-rX, rX)
        random_y = r.uniform(-rY, rY)
        random_z = r.uniform(-rZ, rZ)

        #create a point with rhino3dm
        random_pt = rg.Vector3d(random_x*i, random_y*i, random_z*i)
        vec=rg.Vector3d(0,0,height)
        #second_pt=rg.Point3d(random_x*i, random_y*i, random_z*3*i)
        #first_pt=rg.Point3d(random_x,random_y,random_z)
        #line=rg.Line(first_pt,second_pt)
        base = rg.Extrusion.Create(Geo,height, True)
        bCopy = base.Duplicate()
        bCopy.Translate(random_pt)
        bCopy.Translate(vec)
        bCopy.Scale(i*3) 
        
        
        

        
        

        #add point to the list
        shapes.append(bCopy)
        
        
    return shapes
    

