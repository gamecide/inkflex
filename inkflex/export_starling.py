#!/usr/bin/env python

import sys
import os

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *

def export_to_starling(document):

    # Get access to the main SVG document
    svg = document.getroot()
    
    # Create folder if not exists
    folder = "C:\\Users\\Andres\\Desktop\\StarlingTest"
    if not os.path.exists(folder):
        os.makedirs(folder)
        
    # Generate Main.as document
    generate_main(folder, svg)

    # Generate Game.as document
    generate_game(folder, svg)
    
# Generate Main.as document    
def generate_main(folder, svg):
    
    # Create Main.as file
    filename = os.path.abspath(folder + "\\Main.as")
    f = open(filename, 'w')
    
    # Start to generate
    width = svg.attrib['width']
    height = svg.attrib['height']
    properties = svg.xpath('//*[@id="base"]', namespaces=inkex.NSS)[0]
    bgcolor = properties.attrib['pagecolor']
    
    f.write("import flash.display.Sprite;\nimport starling.core.Starling;\n\n[SWF(width=\"" + width + "\", height=\"" + height + "\", frameRate=\"60\", backgroundColor=\"" + bgcolor + "\")]\npublic class Startup extends Sprite\n{\n\tprivate var _starling:Starling;\n\n\tpublic function Startup()\n\t{\n\t\t_starling = new Starling(Game, stage);\n\t\t_starling.start();\n\t}\n}\n");

# Generate Game.as document    
def generate_game(folder, svg):

    # Create Game.as file
    filename = os.path.abspath(folder + "\\Game.as")
    f = open(filename, 'w')
    
    # Write imports
    f.write("import starling.display.Sprite;\n\n")

    # Write Game class
    f.write("public class Game extends Sprite\n{\n")
    
    # Generate constructor
    
    f.write("\tpublic function Game()\n\t{\n\t}\n")
    
    # End of Game class
    f.write("}\n")
