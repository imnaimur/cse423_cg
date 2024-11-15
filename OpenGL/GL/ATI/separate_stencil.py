'''OpenGL extension ATI.separate_stencil

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.separate_stencil to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides the ability to modify the stencil buffer
	differently based on the facing direction of the primitive that
	generated the fragment.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ATI/separate_stencil.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.ATI.separate_stencil import *
from OpenGL.raw.GL.ATI.separate_stencil import _EXTENSION_NAME

def glInitSeparateStencilATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION