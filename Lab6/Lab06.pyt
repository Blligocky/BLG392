# Import necessary libraries
import arcpy
import time 

class Toolbox(object):
    def __init__(self):
        self.label = "Toolbox"
        self.alias = "toolbox"

        # Tool classes
        self.tools = [RenderTool]

class RenderTool(object):
    def __init__(self):
        self.label = "Tool"
        self.description = " "
        self.canRunInBackground = False

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName = "Your working project",
            name = "workProject",
            datatype = "DEFile",
            parameterType = "Required",
            direction = "Input"
        )

        param1 = arcpy.Parameter(
            displayName = "Name of the layer to render",
            name = "layername",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input"
        )

        param2 = arcpy.Parameter(
            displayName = "Folder of the new project to save to",
            name = "newprojectfolder",
            datatype = "DEFolder",
            parameterType = "Required",
            direction = "Input"
        )

        param3 = arcpy.Parameter(
            displayName = "Name of the new project for saving the layer to",
            name = "newprojectname",
            datatype = "GPString",
            parameterType = "Required",
            direction = "Input"
        )

        params = [param0, param1, param2, param3]
        return params 

    def execute(self, parameters, messages):
        """The source code"""
        # Define vars
        readTime = 2.5
        start = 0
        maximum = 100
        step = 25

        # Set up progressor 
        arcpy.SetProgressor("step", "Checking project and layer", start, maximum, step)
        time.sleep(readTime)
        # Results message 
        arcpy.AddMessage("Checking project and layer...")

        # Reference project 
        aprxFileAddress = parameters[0].valueAsText
        project = arcpy.mp.ArcGISProject(aprxFileAddress)
        layername = parameters[1].valueAsText
        # Grab layer from proj
        if layername == "GarageParking":
            layer = project.listMaps('Map')[0].listLayers()[1]
            symbology = layer.symbology

            # Increment 
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("Start to update render...")
            time.sleep(readTime)
            arcpy.AddMessage("Start to update render...")

            # Update copy renderer 
            symbology.updateRenderer("GraduatedColorsRenderer")
            # Fiel to base off of 
            symbology.renderer.classificationField = "Shape_Area"

            # Increment 
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel("Setting renderer...")
            time.sleep(readTime)
            arcpy.AddMessage("Setting renderer...")

            # Set num classes
            symbology.renderer.breakCount = 5

            # Set color ramp 
            symbology.renderer.colorRamp = project.listColorRamps("Oranges (5 Classes)")[0]

            # Set actual layer equal to copy 
            layer.symbology = symbology 

            # Increment 
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("Saving project...")
            time.sleep(readTime)
            arcpy.AddMessage("Saving project...")

        if layername == "Structures":
            layer = project.listMaps('Map')[0].listLayers()[0]
            symbology = layer.symbology

            # Increment 
            arcpy.SetProgressorPosition(start + step)
            arcpy.SetProgressorLabel("Start to update render...")
            time.sleep(readTime)
            arcpy.AddMessage("Start to update render...")

            # Update copy renderer 
            symbology.updateRenderer("UniqueValueRenderer")
            
            # Increment 
            arcpy.SetProgressorPosition(start + step + step)
            arcpy.SetProgressorLabel("Setting renderer...")
            time.sleep(readTime)
            arcpy.AddMessage("Setting renderer...")

            # Set num classes
            symbology.renderer.fields = ["Type"]

            # Set actual layer equal to copy 
            layer.symbology = symbology 

            # Increment 
            arcpy.SetProgressorPosition(maximum)
            arcpy.SetProgressorLabel("Saving project...")
            time.sleep(readTime)
            arcpy.AddMessage("Saving project...")

        else:
            arcpy.AddMessage("We can't work with this layer.")

        newprojectpath = parameters[2].valueAsText + "\\" + parameters[3].valueAsText
        project.saveACopy(newprojectpath)
        arcpy.AddMessage("Done!")
        return