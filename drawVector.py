import Rhino
import scriptcontext
import System

from Rhino.Geometry import Point3d
from Rhino.Geometry import Vector3d
import math as m

def drawVector(fromPoint, toPoint, color):
    attr = Rhino.DocObjects.ObjectAttributes()
    attr.ObjectDecoration = Rhino.DocObjects.ObjectDecoration.EndArrowhead
    attr.ObjectColor = System.Drawing.Color.FromArgb(color[0], color[1], color[2], color[3])
    attr.ColorSource = Rhino.DocObjects.ObjectColorSource.ColorFromObject
    scriptcontext.doc.Objects.AddLine(fromPoint, toPoint, attr)
def drawVector3d(vector, color = (0, 0, 0, 0)):
    fromPoint = Rhino.Geometry.Point3d.Origin
    toPoint = Rhino.Geometry.Point3d(vector.X, vector.Y, vector.Z)
    drawVector(fromPoint, toPoint, color)

v = Vector3d(10, 10, 0)
rotationAxis = Vector3d(0, 0, 1)

drawVector3d(v, (0, 255, 0, 0))
v.Rotate(m.pi/4, rotationAxis)
drawVector3d(v, (0, 0, 0, 255))

drawVector3d(rotationAxis)
