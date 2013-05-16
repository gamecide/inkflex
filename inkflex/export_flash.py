#!/usr/bin/env python

import sys
import os

# We will use the inkex module with the predefined Effect base class.
import inkex
# The simplestyle module provides functions for style parsing.
from simplestyle import *

def export_to_flash(svg):

    filename = os.path.abspath("C:\\Users\\Andres\\Desktop\\test.as")
    f = open(filename, 'w')
    
    # Get document dimensions
    f.write("width " + svg.attrib['width'])
    f.write("height " + svg.attrib['height'])
    
    # or alternatively
    # svg = self.document.xpath('//svg:svg',namespaces=inkex.NSS)[0]