"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "pnourian"
__version__ = "2020.08.24"

import Rhino as rh
a=rh.RhinoDoc.ActiveDoc.Objects.Find(id).PointCloudGeometry