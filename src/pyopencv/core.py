#!/usr/bin/env python
# PyOpenCV - A Python wrapper for OpenCV 2.0 using Boost.Python and NumPy

# Copyright (c) 2009, Minh-Tri Pham
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

#    * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
#    * Neither the name of pyopencv's copyright holders nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

#THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# For further inquiries, please contact Minh-Tri Pham at pmtri80@gmail.com.
# ----------------------------------------------------------------------------
"""PyOpenCV - A Python wrapper for OpenCV 2.0 using Boost.Python and NumPy

Copyright (c) 2009, Minh-Tri Pham
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

   * Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
   * Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
   * Neither the name of pyopencv's copyright holders nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

For further inquiries, please contact Minh-Tri Pham at pmtri80@gmail.com.
"""

# Try to import numpy
try:
    import numpy as _NP
except ImportError:
    raise ImportError("NumPy is not found in your system. Please install NumPy of version at least 1.2.0.")
    
if _NP.version.version < '1.2.0':
    raise ImportError("NumPy is installed but its version is too old (%s detected). Please install NumPy of version at least 1.2.0." % _NP.version.version)
    
    
# Try to import pyopencvext
import config as _C
if _C.path_ext:
    import os as _os
    _seperator = ';' if _os.name == 'nt' else ':'
    _old_sys_path = _os.environ['PATH']
    _sys_path = _old_sys_path
    import config as _C
    for x in _C.path_ext:
        _sys_path = x + _seperator + _sys_path
    _os.environ['PATH'] = _sys_path
    # print("New path=",_sys_path)
    from pyopencvext import *
    import pyopencvext as _PE
    _os.environ['PATH'] = _old_sys_path
else:
    from pyopencvext import *
    import pyopencvext as _PE
    

import math as _Math
import ctypes as _CT


#=============================================================================
# cvver.h
#=============================================================================

CV_MAJOR_VERSION    = 2
CV_MINOR_VERSION    = 0
CV_SUBMINOR_VERSION = 0
CV_VERSION          = "2.0.0"





#=============================================================================
# cxerror.h
#=============================================================================


    
CV_StsOk                   =  0  # everithing is ok                
CV_StsBackTrace            = -1  # pseudo error for back trace     
CV_StsError                = -2  # unknown /unspecified error      
CV_StsInternal             = -3  # internal error (bad state)      
CV_StsNoMem                = -4  # insufficient memory             
CV_StsBadArg               = -5  # function arg/param is bad       
CV_StsBadFunc              = -6  # unsupported function            
CV_StsNoConv               = -7  # iter. didn't converge           
CV_StsAutoTrace            = -8  # tracing                         

CV_HeaderIsNull            = -9  # image header is NULL            
CV_BadImageSize            = -10 # image size is invalid           
CV_BadOffset               = -11 # offset is invalid               
CV_BadDataPtr              = -12 #
CV_BadStep                 = -13 #
CV_BadModelOrChSeq         = -14 #
CV_BadNumChannels          = -15 #
CV_BadNumChannel1U         = -16 #
CV_BadDepth                = -17 #
CV_BadAlphaChannel         = -18 #
CV_BadOrder                = -19 #
CV_BadOrigin               = -20 #
CV_BadAlign                = -21 #
CV_BadCallBack             = -22 #
CV_BadTileSize             = -23 #
CV_BadCOI                  = -24 #
CV_BadROISize              = -25 #

CV_MaskIsTiled             = -26 #

CV_StsNullPtr                = -27 # null pointer 
CV_StsVecLengthErr           = -28 # incorrect vector length 
CV_StsFilterStructContentErr = -29 # incorr. filter structure content 
CV_StsKernelStructContentErr = -30 # incorr. transform kernel content 
CV_StsFilterOffsetErr        = -31 # incorrect filter ofset value 

#extra for CV 
CV_StsBadSize                = -201 # the input/output structure size is incorrect  
CV_StsDivByZero              = -202 # division by zero 
CV_StsInplaceNotSupported    = -203 # in-place operation is not supported 
CV_StsObjectNotFound         = -204 # request can't be completed 
CV_StsUnmatchedFormats       = -205 # formats of input/output arrays differ 
CV_StsBadFlag                = -206 # flag is wrong or not supported   
CV_StsBadPoint               = -207 # bad CvPoint  
CV_StsBadMask                = -208 # bad format of mask (neither 8uC1 nor 8sC1)
CV_StsUnmatchedSizes         = -209 # sizes of input/output structures do not match 
CV_StsUnsupportedFormat      = -210 # the data format/type is not supported by the function
CV_StsOutOfRange             = -211 # some of parameters are out of range 
CV_StsParseError             = -212 # invalid syntax/structure of the parsed file 
CV_StsNotImplemented         = -213 # the requested function/feature is not implemented 
CV_StsBadMemBlock            = -214 # an allocated block has been corrupted 
CV_StsAssert                 = -215 # assertion failed 



    
#=============================================================================
# cxtypes.h
#=============================================================================


    
#-----------------------------------------------------------------------------
# Common macros and inline functions
#-----------------------------------------------------------------------------

CV_PI = _Math.pi
CV_LOG2 = 0.69314718055994530941723212145818

    
#-----------------------------------------------------------------------------
# Random number generation
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Matrix type (CvMat) 
#-----------------------------------------------------------------------------

# Matrix type (CvMat)
CV_CN_MAX = 64
CV_CN_SHIFT = 3
CV_DEPTH_MAX = (1 << CV_CN_SHIFT)

CV_8U = 0
CV_8S = 1
CV_16U = 2
CV_16S = 3
CV_32S = 4
CV_32F = 5
CV_64F = 6
CV_USRTYPE1 = 7

def CV_MAKETYPE(depth,cn):
    return ((depth) + (((cn)-1) << CV_CN_SHIFT))
CV_MAKE_TYPE = CV_MAKETYPE

CV_8UC1 = CV_MAKETYPE(CV_8U,1)
CV_8UC2 = CV_MAKETYPE(CV_8U,2)
CV_8UC3 = CV_MAKETYPE(CV_8U,3)
CV_8UC4 = CV_MAKETYPE(CV_8U,4)

CV_8SC1 = CV_MAKETYPE(CV_8S,1)
CV_8SC2 = CV_MAKETYPE(CV_8S,2)
CV_8SC3 = CV_MAKETYPE(CV_8S,3)
CV_8SC4 = CV_MAKETYPE(CV_8S,4)

CV_16UC1 = CV_MAKETYPE(CV_16U,1)
CV_16UC2 = CV_MAKETYPE(CV_16U,2)
CV_16UC3 = CV_MAKETYPE(CV_16U,3)
CV_16UC4 = CV_MAKETYPE(CV_16U,4)

CV_16SC1 = CV_MAKETYPE(CV_16S,1)
CV_16SC2 = CV_MAKETYPE(CV_16S,2)
CV_16SC3 = CV_MAKETYPE(CV_16S,3)
CV_16SC4 = CV_MAKETYPE(CV_16S,4)

CV_32SC1 = CV_MAKETYPE(CV_32S,1)
CV_32SC2 = CV_MAKETYPE(CV_32S,2)
CV_32SC3 = CV_MAKETYPE(CV_32S,3)
CV_32SC4 = CV_MAKETYPE(CV_32S,4)

CV_32FC1 = CV_MAKETYPE(CV_32F,1)
CV_32FC2 = CV_MAKETYPE(CV_32F,2)
CV_32FC3 = CV_MAKETYPE(CV_32F,3)
CV_32FC4 = CV_MAKETYPE(CV_32F,4)

CV_64FC1 = CV_MAKETYPE(CV_64F,1)
CV_64FC2 = CV_MAKETYPE(CV_64F,2)
CV_64FC3 = CV_MAKETYPE(CV_64F,3)
CV_64FC4 = CV_MAKETYPE(CV_64F,4)

CV_AUTOSTEP = 0x7fffffff
CV_WHOLE_ARR  = _PE.Range( 0, 0x3fffffff )

CV_MAT_CN_MASK = ((CV_CN_MAX - 1) << CV_CN_SHIFT)
def CV_MAT_CN(flags):
    return ((((flags) & CV_MAT_CN_MASK) >> CV_CN_SHIFT) + 1)
CV_MAT_DEPTH_MASK = (CV_DEPTH_MAX - 1)
def CV_MAT_DEPTH(flags):
    return ((flags) & CV_MAT_DEPTH_MASK)
CV_MAT_TYPE_MASK = (CV_DEPTH_MAX*CV_CN_MAX - 1)
def CV_MAT_TYPE(flags):
    ((flags) & CV_MAT_TYPE_MASK)
CV_MAT_CONT_FLAG_SHIFT = 9
CV_MAT_CONT_FLAG = (1 << CV_MAT_CONT_FLAG_SHIFT)
def CV_IS_MAT_CONT(flags):
    return ((flags) & CV_MAT_CONT_FLAG)
CV_IS_CONT_MAT = CV_IS_MAT_CONT
CV_MAT_TEMP_FLAG_SHIFT = 10
CV_MAT_TEMP_FLAG = (1 << CV_MAT_TEMP_FLAG_SHIFT)
def CV_IS_TEMP_MAT(flags):
    return ((flags) & CV_MAT_TEMP_FLAG)

CV_MAGIC_MASK = 0xFFFF0000
CV_MAT_MAGIC_VAL = 0x42420000
CV_TYPE_NAME_MAT = "opencv-matrix"


#-----------------------------------------------------------------------------
# Multi-dimensional dense array (CvMatND)
#-----------------------------------------------------------------------------

CV_MATND_MAGIC_VAL    = 0x42430000
CV_TYPE_NAME_MATND    = "opencv-nd-matrix"

CV_MAX_DIM = 32
CV_MAX_DIM_HEAP = (1 << 16)


#-----------------------------------------------------------------------------
# Multi-dimensional sparse array (CvSparseMat) 
#-----------------------------------------------------------------------------

CV_SPARSE_MAT_MAGIC_VAL    = 0x42440000
CV_TYPE_NAME_SPARSE_MAT    = "opencv-sparse-matrix"


    
#-----------------------------------------------------------------------------
# Other supplementary data type definitions
#-----------------------------------------------------------------------------

# CV_TERMCRIT_ITER    = 1
# CV_TERMCRIT_NUMBER  = CV_TERMCRIT_ITER
# CV_TERMCRIT_EPS     = 2

CV_WHOLE_SEQ_END_INDEX = 0x3fffffff
CV_WHOLE_SEQ = _PE.Range(0, CV_WHOLE_SEQ_END_INDEX)


    
#-----------------------------------------------------------------------------
# Dynamic Data structures
#-----------------------------------------------------------------------------

CV_STORAGE_MAGIC_VAL = 0x42890000

CV_TYPE_NAME_SEQ             = "opencv-sequence"
CV_TYPE_NAME_SEQ_TREE        = "opencv-sequence-tree"

CV_SET_ELEM_IDX_MASK   = ((1 << 26) - 1)
CV_SET_ELEM_FREE_FLAG  = (1 << (_CT.sizeof(_CT.c_int)*8-1))

# Checks whether the element pointed by ptr belongs to a set or not
def CV_IS_SET_ELEM(ptr):
    return cast(ptr, CvSetElem_p)[0].flags >= 0

CV_TYPE_NAME_GRAPH = "opencv-graph"


    
CvMemStorage._ownershiplevel = 0

def _CvMemStorage__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseMemStorage(self)
CvMemStorage.__del__ = _CvMemStorage__del__

#-----------------------------------------------------------------------------
# Sequence types
#-----------------------------------------------------------------------------

#Viji Periapoilan 5/21/2007(start)

CV_SEQ_MAGIC_VAL            = 0x42990000

#define CV_IS_SEQ(seq) #    ((seq) != NULL && (((CvSeq*)(seq))->flags & CV_MAGIC_MASK) == CV_SEQ_MAGIC_VAL)

CV_SET_MAGIC_VAL           = 0x42980000
#define CV_IS_SET(set) #    ((set) != NULL && (((CvSeq*)(set))->flags & CV_MAGIC_MASK) == CV_SET_MAGIC_VAL)

CV_SEQ_ELTYPE_BITS         = 9
CV_SEQ_ELTYPE_MASK         =  ((1 << CV_SEQ_ELTYPE_BITS) - 1)
CV_SEQ_ELTYPE_POINT        =  CV_32SC2  #/* (x,y) */
CV_SEQ_ELTYPE_CODE         = CV_8UC1   #/* freeman code: 0..7 */
CV_SEQ_ELTYPE_GENERIC      =  0
CV_SEQ_ELTYPE_PTR          =  CV_USRTYPE1
CV_SEQ_ELTYPE_PPOINT       =  CV_SEQ_ELTYPE_PTR  #/* &(x,y) */
CV_SEQ_ELTYPE_INDEX        =  CV_32SC1  #/* #(x,y) */
CV_SEQ_ELTYPE_GRAPH_EDGE   =  0  #/* &next_o, &next_d, &vtx_o, &vtx_d */
CV_SEQ_ELTYPE_GRAPH_VERTEX =  0  #/* first_edge, &(x,y) */
CV_SEQ_ELTYPE_TRIAN_ATR    =  0  #/* vertex of the binary tree   */
CV_SEQ_ELTYPE_CONNECTED_COMP= 0  #/* connected component  */
CV_SEQ_ELTYPE_POINT3D      =  CV_32FC3  #/* (x,y,z)  */

CV_SEQ_KIND_BITS           = 3
CV_SEQ_KIND_MASK           = (((1 << CV_SEQ_KIND_BITS) - 1)<<CV_SEQ_ELTYPE_BITS)


# types of sequences
CV_SEQ_KIND_GENERIC        = (0 << CV_SEQ_ELTYPE_BITS)
CV_SEQ_KIND_CURVE          = (1 << CV_SEQ_ELTYPE_BITS)
CV_SEQ_KIND_BIN_TREE       = (2 << CV_SEQ_ELTYPE_BITS)

#Viji Periapoilan 5/21/2007(end)

# types of sparse sequences (sets)
CV_SEQ_KIND_GRAPH       = (3 << CV_SEQ_ELTYPE_BITS)
CV_SEQ_KIND_SUBDIV2D    = (4 << CV_SEQ_ELTYPE_BITS)

CV_SEQ_FLAG_SHIFT       = (CV_SEQ_KIND_BITS + CV_SEQ_ELTYPE_BITS)

# flags for curves
CV_SEQ_FLAG_CLOSED     = (1 << CV_SEQ_FLAG_SHIFT)
CV_SEQ_FLAG_SIMPLE     = (2 << CV_SEQ_FLAG_SHIFT)
CV_SEQ_FLAG_CONVEX     = (4 << CV_SEQ_FLAG_SHIFT)
CV_SEQ_FLAG_HOLE       = (8 << CV_SEQ_FLAG_SHIFT)

# flags for graphs
CV_GRAPH_FLAG_ORIENTED = (1 << CV_SEQ_FLAG_SHIFT)

CV_GRAPH               = CV_SEQ_KIND_GRAPH
CV_ORIENTED_GRAPH      = (CV_SEQ_KIND_GRAPH|CV_GRAPH_FLAG_ORIENTED)

# point sets
CV_SEQ_POINT_SET       = (CV_SEQ_KIND_GENERIC| CV_SEQ_ELTYPE_POINT)
CV_SEQ_POINT3D_SET     = (CV_SEQ_KIND_GENERIC| CV_SEQ_ELTYPE_POINT3D)
CV_SEQ_POLYLINE        = (CV_SEQ_KIND_CURVE  | CV_SEQ_ELTYPE_POINT)
CV_SEQ_POLYGON         = (CV_SEQ_FLAG_CLOSED | CV_SEQ_POLYLINE )
CV_SEQ_CONTOUR         = CV_SEQ_POLYGON
CV_SEQ_SIMPLE_POLYGON  = (CV_SEQ_FLAG_SIMPLE | CV_SEQ_POLYGON  )

# chain-coded curves
CV_SEQ_CHAIN           = (CV_SEQ_KIND_CURVE  | CV_SEQ_ELTYPE_CODE)
CV_SEQ_CHAIN_CONTOUR   = (CV_SEQ_FLAG_CLOSED | CV_SEQ_CHAIN)

# binary tree for the contour
CV_SEQ_POLYGON_TREE    = (CV_SEQ_KIND_BIN_TREE  | CV_SEQ_ELTYPE_TRIAN_ATR)

# sequence of the connected components
CV_SEQ_CONNECTED_COMP  = (CV_SEQ_KIND_GENERIC  | CV_SEQ_ELTYPE_CONNECTED_COMP)

# sequence of the integer numbers
CV_SEQ_INDEX           = (CV_SEQ_KIND_GENERIC  | CV_SEQ_ELTYPE_INDEX)

# CV_SEQ_ELTYPE( seq )   = ((seq)->flags & CV_SEQ_ELTYPE_MASK)
# CV_SEQ_KIND( seq )     = ((seq)->flags & CV_SEQ_KIND_MASK )

def CV_GET_SEQ_ELEM(TYPE, seq, index):
    result = cvGetSeqElem(seq, index)
    return cast(result, POINTER(TYPE))


    
#-----------------------------------------------------------------------------
# Data structures for persistence (a.k.a serialization) functionality
#-----------------------------------------------------------------------------

CV_STORAGE_READ = 0
CV_STORAGE_WRITE = 1
CV_STORAGE_WRITE_TEXT = CV_STORAGE_WRITE
CV_STORAGE_WRITE_BINARY = CV_STORAGE_WRITE
CV_STORAGE_APPEND = 2

CV_NODE_NONE        = 0
CV_NODE_INT         = 1
CV_NODE_INTEGER     = CV_NODE_INT
CV_NODE_REAL        = 2
CV_NODE_FLOAT       = CV_NODE_REAL
CV_NODE_STR         = 3
CV_NODE_STRING      = CV_NODE_STR
CV_NODE_REF         = 4 # not used
CV_NODE_SEQ         = 5
CV_NODE_MAP         = 6
CV_NODE_TYPE_MASK   = 7

def CV_NODE_TYPE(flags):
    return flags & CV_NODE_TYPE_MASK

# file node flags
CV_NODE_FLOW        = 8 # used only for writing structures to YAML format
CV_NODE_USER        = 16
CV_NODE_EMPTY       = 32
CV_NODE_NAMED       = 64

def CV_NODE_IS_INT(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_INT
    
def CV_NODE_IS_REAL(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_REAL
    
def CV_NODE_IS_STRING(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_STRING
    
def CV_NODE_IS_SEQ(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_SEQ
    
def CV_NODE_IS_MAP(flags):
    return CV_NODE_TYPE(flags) == CV_NODE_MAP
    
def CV_NODE_IS_COLLECTION(flags):
    return CV_NODE_TYPE(flags) >= CV_NODE_SEQ
    
def CV_NODE_IS_FLOW(flags):
    return bool(flags & CV_NODE_FLOW)
    
def CV_NODE_IS_EMPTY(flags):
    return bool(flags & CV_NODE_EMPTY)
    
def CV_NODE_IS_USER(flags):
    return bool(flags & CV_NODE_USER)
    
def CV_NODE_HAS_NAME(flags):
    return bool(flags & CV_NODE_NAMED)

CV_NODE_SEQ_SIMPLE = 256
def CV_NODE_SEQ_IS_SIMPLE(seq):
    return bool(seq[0].flags & CV_NODE_SEQ_SIMPLE)


    
CvFileStorage._ownershiplevel = 0

def _CvFileStorage__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseFileStorage(self)
CvFileStorage.__del__ = _CvFileStorage__del__

#=============================================================================
# cxcore.h
#=============================================================================


    
#-----------------------------------------------------------------------------
# Array allocation, deallocation, initialization and access to elements
#-----------------------------------------------------------------------------


    
CV_MAX_ARR = 10

CV_NO_DEPTH_CHECK     = 1
CV_NO_CN_CHECK        = 2
CV_NO_SIZE_CHECK      = 4

    
#-----------------------------------------------------------------------------
# Arithmetic, logic and comparison operations
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Math operations
#-----------------------------------------------------------------------------


CV_RAND_UNI = 0
CV_RAND_NORMAL = 1

    
    
#-----------------------------------------------------------------------------
# Matrix operations
#-----------------------------------------------------------------------------


CV_COVAR_SCRAMBLED = 0
CV_COVAR_NORMAL = 1
CV_COVAR_USE_AVG = 2
CV_COVAR_SCALE = 4
CV_COVAR_ROWS = 8
CV_COVAR_COLS = 16

CV_PCA_DATA_AS_ROW = 0
CV_PCA_DATA_AS_COL = 1
CV_PCA_USE_AVG = 2

    
#-----------------------------------------------------------------------------
# Array Statistics
#-----------------------------------------------------------------------------

    
CV_REDUCE_SUM = 0
CV_REDUCE_AVG = 1
CV_REDUCE_MAX = 2
CV_REDUCE_MIN = 3


#-----------------------------------------------------------------------------
# Discrete Linear Transforms and Related Functions
#-----------------------------------------------------------------------------

    

#-----------------------------------------------------------------------------
# Dynamic Data Structure
#-----------------------------------------------------------------------------

    
CV_FRONT = 1
CV_BACK = 0


    
CvGraphScanner._ownershiplevel = 0

def _CvGraphScanner__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseGraphScanner(self)
CvGraphScanner.__del__ = _CvGraphScanner__del__

#-----------------------------------------------------------------------------
# Drawing Functions
#-----------------------------------------------------------------------------

    
CV_FILLED = -1
CV_AA = 16

# Constructs a color value
def CV_RGB(r, g, b):
    return Scalar(b, g, r)

    
    
#-----------------------------------------------------------------------------
# System Functions
#-----------------------------------------------------------------------------

    
# Sets the error mode
CV_ErrModeLeaf = 0
CV_ErrModeParent = 1
CV_ErrModeSilent = 2


    
#-----------------------------------------------------------------------------
# Data Persistence
#-----------------------------------------------------------------------------

    

    
#=============================================================================
# cxcore.hpp
#=============================================================================

    
_str = "\n    Creates a Vec6d view on an ndarray instance."
if Vec6d.from_ndarray.__doc__ is None:
    Vec6d.from_ndarray.__doc__ = _str
else:
    Vec6d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec6d that shares the same data with an ndarray instance, use:\n        'Vec6d.from_ndarray(a)' or 'asVec6d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec6d.__doc__ is None:
    Vec6d.__doc__ = _str
else:
    Vec6d.__doc__ += _str
    
def _Vec6d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec6d.__getitem__ = _Vec6d__getitem__
            
def _Vec6d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec6d.__setitem__ = _Vec6d__setitem__
            
def _Vec6d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec6d.__getslice__ = _Vec6d__getslice__
            
def _Vec6d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec6d.__setslice__ = _Vec6d__setslice__
        
def _Vec6d__repr__(self):
    return "Vec6d(" + self.ndarray.__str__() + ")"
Vec6d.__repr__ = _Vec6d__repr__
        
_str = "\n    Creates a Vec2d view on an ndarray instance."
if Vec2d.from_ndarray.__doc__ is None:
    Vec2d.from_ndarray.__doc__ = _str
else:
    Vec2d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec2d that shares the same data with an ndarray instance, use:\n        'Vec2d.from_ndarray(a)' or 'asVec2d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2d.__doc__ is None:
    Vec2d.__doc__ = _str
else:
    Vec2d.__doc__ += _str
    
def _Vec2d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2d.__getitem__ = _Vec2d__getitem__
            
def _Vec2d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2d.__setitem__ = _Vec2d__setitem__
            
def _Vec2d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2d.__getslice__ = _Vec2d__getslice__
            
def _Vec2d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2d.__setslice__ = _Vec2d__setslice__
        
def _Vec2d__repr__(self):
    return "Vec2d(" + self.ndarray.__str__() + ")"
Vec2d.__repr__ = _Vec2d__repr__
        
_str = "\n    Creates a Vec6f view on an ndarray instance."
if Vec6f.from_ndarray.__doc__ is None:
    Vec6f.from_ndarray.__doc__ = _str
else:
    Vec6f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec6f that shares the same data with an ndarray instance, use:\n        'Vec6f.from_ndarray(a)' or 'asVec6f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec6f.__doc__ is None:
    Vec6f.__doc__ = _str
else:
    Vec6f.__doc__ += _str
    
def _Vec6f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec6f.__getitem__ = _Vec6f__getitem__
            
def _Vec6f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec6f.__setitem__ = _Vec6f__setitem__
            
def _Vec6f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec6f.__getslice__ = _Vec6f__getslice__
            
def _Vec6f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec6f.__setslice__ = _Vec6f__setslice__
        
def _Vec6f__repr__(self):
    return "Vec6f(" + self.ndarray.__str__() + ")"
Vec6f.__repr__ = _Vec6f__repr__
        
_str = "\n    Creates a Vec4f view on an ndarray instance."
if Vec4f.from_ndarray.__doc__ is None:
    Vec4f.from_ndarray.__doc__ = _str
else:
    Vec4f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec4f that shares the same data with an ndarray instance, use:\n        'Vec4f.from_ndarray(a)' or 'asVec4f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4f.__doc__ is None:
    Vec4f.__doc__ = _str
else:
    Vec4f.__doc__ += _str
    
def _Vec4f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4f.__getitem__ = _Vec4f__getitem__
            
def _Vec4f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4f.__setitem__ = _Vec4f__setitem__
            
def _Vec4f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4f.__getslice__ = _Vec4f__getslice__
            
def _Vec4f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4f.__setslice__ = _Vec4f__setslice__
        
def _Vec4f__repr__(self):
    return "Vec4f(" + self.ndarray.__str__() + ")"
Vec4f.__repr__ = _Vec4f__repr__
        
_str = "\n    Creates a Vec4i view on an ndarray instance."
if Vec4i.from_ndarray.__doc__ is None:
    Vec4i.from_ndarray.__doc__ = _str
else:
    Vec4i.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec4i that shares the same data with an ndarray instance, use:\n        'Vec4i.from_ndarray(a)' or 'asVec4i(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4i.__doc__ is None:
    Vec4i.__doc__ = _str
else:
    Vec4i.__doc__ += _str
    
def _Vec4i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4i.__getitem__ = _Vec4i__getitem__
            
def _Vec4i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4i.__setitem__ = _Vec4i__setitem__
            
def _Vec4i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4i.__getslice__ = _Vec4i__getslice__
            
def _Vec4i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4i.__setslice__ = _Vec4i__setslice__
        
def _Vec4i__repr__(self):
    return "Vec4i(" + self.ndarray.__str__() + ")"
Vec4i.__repr__ = _Vec4i__repr__
        
_str = "\n    Creates a Vec3i view on an ndarray instance."
if Vec3i.from_ndarray.__doc__ is None:
    Vec3i.from_ndarray.__doc__ = _str
else:
    Vec3i.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec3i that shares the same data with an ndarray instance, use:\n        'Vec3i.from_ndarray(a)' or 'asVec3i(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3i.__doc__ is None:
    Vec3i.__doc__ = _str
else:
    Vec3i.__doc__ += _str
    
def _Vec3i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3i.__getitem__ = _Vec3i__getitem__
            
def _Vec3i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3i.__setitem__ = _Vec3i__setitem__
            
def _Vec3i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3i.__getslice__ = _Vec3i__getslice__
            
def _Vec3i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3i.__setslice__ = _Vec3i__setslice__
        
def _Vec3i__repr__(self):
    return "Vec3i(" + self.ndarray.__str__() + ")"
Vec3i.__repr__ = _Vec3i__repr__
        
_str = "\n    Creates a Vec4w view on an ndarray instance."
if Vec4w.from_ndarray.__doc__ is None:
    Vec4w.from_ndarray.__doc__ = _str
else:
    Vec4w.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec4w that shares the same data with an ndarray instance, use:\n        'Vec4w.from_ndarray(a)' or 'asVec4w(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4w.__doc__ is None:
    Vec4w.__doc__ = _str
else:
    Vec4w.__doc__ += _str
    
def _Vec4w__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4w.__getitem__ = _Vec4w__getitem__
            
def _Vec4w__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4w.__setitem__ = _Vec4w__setitem__
            
def _Vec4w__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4w.__getslice__ = _Vec4w__getslice__
            
def _Vec4w__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4w.__setslice__ = _Vec4w__setslice__
        
def _Vec4w__repr__(self):
    return "Vec4w(" + self.ndarray.__str__() + ")"
Vec4w.__repr__ = _Vec4w__repr__
        
_str = "\n    Creates a Vec3w view on an ndarray instance."
if Vec3w.from_ndarray.__doc__ is None:
    Vec3w.from_ndarray.__doc__ = _str
else:
    Vec3w.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec3w that shares the same data with an ndarray instance, use:\n        'Vec3w.from_ndarray(a)' or 'asVec3w(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3w.__doc__ is None:
    Vec3w.__doc__ = _str
else:
    Vec3w.__doc__ += _str
    
def _Vec3w__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3w.__getitem__ = _Vec3w__getitem__
            
def _Vec3w__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3w.__setitem__ = _Vec3w__setitem__
            
def _Vec3w__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3w.__getslice__ = _Vec3w__getslice__
            
def _Vec3w__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3w.__setslice__ = _Vec3w__setslice__
        
def _Vec3w__repr__(self):
    return "Vec3w(" + self.ndarray.__str__() + ")"
Vec3w.__repr__ = _Vec3w__repr__
        
_str = "\n    Creates a Vec2w view on an ndarray instance."
if Vec2w.from_ndarray.__doc__ is None:
    Vec2w.from_ndarray.__doc__ = _str
else:
    Vec2w.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec2w that shares the same data with an ndarray instance, use:\n        'Vec2w.from_ndarray(a)' or 'asVec2w(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2w.__doc__ is None:
    Vec2w.__doc__ = _str
else:
    Vec2w.__doc__ += _str
    
def _Vec2w__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2w.__getitem__ = _Vec2w__getitem__
            
def _Vec2w__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2w.__setitem__ = _Vec2w__setitem__
            
def _Vec2w__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2w.__getslice__ = _Vec2w__getslice__
            
def _Vec2w__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2w.__setslice__ = _Vec2w__setslice__
        
def _Vec2w__repr__(self):
    return "Vec2w(" + self.ndarray.__str__() + ")"
Vec2w.__repr__ = _Vec2w__repr__
        
_str = "\n    Creates a Vec4s view on an ndarray instance."
if Vec4s.from_ndarray.__doc__ is None:
    Vec4s.from_ndarray.__doc__ = _str
else:
    Vec4s.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec4s that shares the same data with an ndarray instance, use:\n        'Vec4s.from_ndarray(a)' or 'asVec4s(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4s.__doc__ is None:
    Vec4s.__doc__ = _str
else:
    Vec4s.__doc__ += _str
    
def _Vec4s__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4s.__getitem__ = _Vec4s__getitem__
            
def _Vec4s__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4s.__setitem__ = _Vec4s__setitem__
            
def _Vec4s__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4s.__getslice__ = _Vec4s__getslice__
            
def _Vec4s__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4s.__setslice__ = _Vec4s__setslice__
        
def _Vec4s__repr__(self):
    return "Vec4s(" + self.ndarray.__str__() + ")"
Vec4s.__repr__ = _Vec4s__repr__
        
_str = "\n    Creates a Vec3s view on an ndarray instance."
if Vec3s.from_ndarray.__doc__ is None:
    Vec3s.from_ndarray.__doc__ = _str
else:
    Vec3s.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec3s that shares the same data with an ndarray instance, use:\n        'Vec3s.from_ndarray(a)' or 'asVec3s(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3s.__doc__ is None:
    Vec3s.__doc__ = _str
else:
    Vec3s.__doc__ += _str
    
def _Vec3s__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3s.__getitem__ = _Vec3s__getitem__
            
def _Vec3s__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3s.__setitem__ = _Vec3s__setitem__
            
def _Vec3s__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3s.__getslice__ = _Vec3s__getslice__
            
def _Vec3s__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3s.__setslice__ = _Vec3s__setslice__
        
def _Vec3s__repr__(self):
    return "Vec3s(" + self.ndarray.__str__() + ")"
Vec3s.__repr__ = _Vec3s__repr__
        
_str = "\n    Creates a Vec2s view on an ndarray instance."
if Vec2s.from_ndarray.__doc__ is None:
    Vec2s.from_ndarray.__doc__ = _str
else:
    Vec2s.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec2s that shares the same data with an ndarray instance, use:\n        'Vec2s.from_ndarray(a)' or 'asVec2s(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2s.__doc__ is None:
    Vec2s.__doc__ = _str
else:
    Vec2s.__doc__ += _str
    
def _Vec2s__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2s.__getitem__ = _Vec2s__getitem__
            
def _Vec2s__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2s.__setitem__ = _Vec2s__setitem__
            
def _Vec2s__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2s.__getslice__ = _Vec2s__getslice__
            
def _Vec2s__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2s.__setslice__ = _Vec2s__setslice__
        
def _Vec2s__repr__(self):
    return "Vec2s(" + self.ndarray.__str__() + ")"
Vec2s.__repr__ = _Vec2s__repr__
        
_str = "\n    Creates a Vec4b view on an ndarray instance."
if Vec4b.from_ndarray.__doc__ is None:
    Vec4b.from_ndarray.__doc__ = _str
else:
    Vec4b.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec4b that shares the same data with an ndarray instance, use:\n        'Vec4b.from_ndarray(a)' or 'asVec4b(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4b.__doc__ is None:
    Vec4b.__doc__ = _str
else:
    Vec4b.__doc__ += _str
    
def _Vec4b__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4b.__getitem__ = _Vec4b__getitem__
            
def _Vec4b__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4b.__setitem__ = _Vec4b__setitem__
            
def _Vec4b__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4b.__getslice__ = _Vec4b__getslice__
            
def _Vec4b__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4b.__setslice__ = _Vec4b__setslice__
        
def _Vec4b__repr__(self):
    return "Vec4b(" + self.ndarray.__str__() + ")"
Vec4b.__repr__ = _Vec4b__repr__
        
_str = "\n    Creates a Vec3b view on an ndarray instance."
if Vec3b.from_ndarray.__doc__ is None:
    Vec3b.from_ndarray.__doc__ = _str
else:
    Vec3b.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec3b that shares the same data with an ndarray instance, use:\n        'Vec3b.from_ndarray(a)' or 'asVec3b(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3b.__doc__ is None:
    Vec3b.__doc__ = _str
else:
    Vec3b.__doc__ += _str
    
def _Vec3b__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3b.__getitem__ = _Vec3b__getitem__
            
def _Vec3b__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3b.__setitem__ = _Vec3b__setitem__
            
def _Vec3b__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3b.__getslice__ = _Vec3b__getslice__
            
def _Vec3b__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3b.__setslice__ = _Vec3b__setslice__
        
def _Vec3b__repr__(self):
    return "Vec3b(" + self.ndarray.__str__() + ")"
Vec3b.__repr__ = _Vec3b__repr__
        
_str = "\n    Creates a Vec2b view on an ndarray instance."
if Vec2b.from_ndarray.__doc__ is None:
    Vec2b.from_ndarray.__doc__ = _str
else:
    Vec2b.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec2b that shares the same data with an ndarray instance, use:\n        'Vec2b.from_ndarray(a)' or 'asVec2b(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2b.__doc__ is None:
    Vec2b.__doc__ = _str
else:
    Vec2b.__doc__ += _str
    
def _Vec2b__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2b.__getitem__ = _Vec2b__getitem__
            
def _Vec2b__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2b.__setitem__ = _Vec2b__setitem__
            
def _Vec2b__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2b.__getslice__ = _Vec2b__getslice__
            
def _Vec2b__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2b.__setslice__ = _Vec2b__setslice__
        
def _Vec2b__repr__(self):
    return "Vec2b(" + self.ndarray.__str__() + ")"
Vec2b.__repr__ = _Vec2b__repr__
        
_str = "\n    Creates a Vec3d view on an ndarray instance."
if Vec3d.from_ndarray.__doc__ is None:
    Vec3d.from_ndarray.__doc__ = _str
else:
    Vec3d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec3d that shares the same data with an ndarray instance, use:\n        'Vec3d.from_ndarray(a)' or 'asVec3d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3d.__doc__ is None:
    Vec3d.__doc__ = _str
else:
    Vec3d.__doc__ += _str
    
def _Vec3d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3d.__getitem__ = _Vec3d__getitem__
            
def _Vec3d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3d.__setitem__ = _Vec3d__setitem__
            
def _Vec3d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3d.__getslice__ = _Vec3d__getslice__
            
def _Vec3d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3d.__setslice__ = _Vec3d__setslice__
        
def _Vec3d__repr__(self):
    return "Vec3d(" + self.ndarray.__str__() + ")"
Vec3d.__repr__ = _Vec3d__repr__
        
_str = "\n    Creates a Vec3f view on an ndarray instance."
if Vec3f.from_ndarray.__doc__ is None:
    Vec3f.from_ndarray.__doc__ = _str
else:
    Vec3f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec3f that shares the same data with an ndarray instance, use:\n        'Vec3f.from_ndarray(a)' or 'asVec3f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec3f.__doc__ is None:
    Vec3f.__doc__ = _str
else:
    Vec3f.__doc__ += _str
    
def _Vec3f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec3f.__getitem__ = _Vec3f__getitem__
            
def _Vec3f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec3f.__setitem__ = _Vec3f__setitem__
            
def _Vec3f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec3f.__getslice__ = _Vec3f__getslice__
            
def _Vec3f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec3f.__setslice__ = _Vec3f__setslice__
        
def _Vec3f__repr__(self):
    return "Vec3f(" + self.ndarray.__str__() + ")"
Vec3f.__repr__ = _Vec3f__repr__
        
_str = "\n    Creates a Vec4d view on an ndarray instance."
if Vec4d.from_ndarray.__doc__ is None:
    Vec4d.from_ndarray.__doc__ = _str
else:
    Vec4d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec4d that shares the same data with an ndarray instance, use:\n        'Vec4d.from_ndarray(a)' or 'asVec4d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec4d.__doc__ is None:
    Vec4d.__doc__ = _str
else:
    Vec4d.__doc__ += _str
    
def _Vec4d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec4d.__getitem__ = _Vec4d__getitem__
            
def _Vec4d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec4d.__setitem__ = _Vec4d__setitem__
            
def _Vec4d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec4d.__getslice__ = _Vec4d__getslice__
            
def _Vec4d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec4d.__setslice__ = _Vec4d__setslice__
        
def _Vec4d__repr__(self):
    return "Vec4d(" + self.ndarray.__str__() + ")"
Vec4d.__repr__ = _Vec4d__repr__
        
_str = "\n    Creates a Vec2f view on an ndarray instance."
if Vec2f.from_ndarray.__doc__ is None:
    Vec2f.from_ndarray.__doc__ = _str
else:
    Vec2f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec2f that shares the same data with an ndarray instance, use:\n        'Vec2f.from_ndarray(a)' or 'asVec2f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2f.__doc__ is None:
    Vec2f.__doc__ = _str
else:
    Vec2f.__doc__ += _str
    
def _Vec2f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2f.__getitem__ = _Vec2f__getitem__
            
def _Vec2f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2f.__setitem__ = _Vec2f__setitem__
            
def _Vec2f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2f.__getslice__ = _Vec2f__getslice__
            
def _Vec2f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2f.__setslice__ = _Vec2f__setslice__
        
def _Vec2f__repr__(self):
    return "Vec2f(" + self.ndarray.__str__() + ")"
Vec2f.__repr__ = _Vec2f__repr__
        
_str = "\n    Creates a Vec2i view on an ndarray instance."
if Vec2i.from_ndarray.__doc__ is None:
    Vec2i.from_ndarray.__doc__ = _str
else:
    Vec2i.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Vec2i that shares the same data with an ndarray instance, use:\n        'Vec2i.from_ndarray(a)' or 'asVec2i(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Vec2i.__doc__ is None:
    Vec2i.__doc__ = _str
else:
    Vec2i.__doc__ += _str
    
def _Vec2i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Vec2i.__getitem__ = _Vec2i__getitem__
            
def _Vec2i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Vec2i.__setitem__ = _Vec2i__setitem__
            
def _Vec2i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Vec2i.__getslice__ = _Vec2i__getslice__
            
def _Vec2i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Vec2i.__setslice__ = _Vec2i__setslice__
        
def _Vec2i__repr__(self):
    return "Vec2i(" + self.ndarray.__str__() + ")"
Vec2i.__repr__ = _Vec2i__repr__
        
def _Complexd__repr__(self):
    return "Complexd(re=" + repr(self.re) + ", im=" + repr(self.im) + ")"
Complexd.__repr__ = _Complexd__repr__
        
def _Complexf__repr__(self):
    return "Complexf(re=" + repr(self.re) + ", im=" + repr(self.im) + ")"
Complexf.__repr__ = _Complexf__repr__
        
def _Point2d__repr__(self):
    return "Point2d(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
Point2d.__repr__ = _Point2d__repr__
        
        
_str = "\n    Creates a Point2d view on an ndarray instance."
if Point2d.from_ndarray.__doc__ is None:
    Point2d.from_ndarray.__doc__ = _str
else:
    Point2d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Point2d that shares the same data with an ndarray instance, use:\n        'Point2d.from_ndarray(a)' or 'asPoint2d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point2d.__doc__ is None:
    Point2d.__doc__ = _str
else:
    Point2d.__doc__ += _str
    
def _Point2d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point2d.__getitem__ = _Point2d__getitem__
            
def _Point2d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point2d.__setitem__ = _Point2d__setitem__
            
def _Point2d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point2d.__getslice__ = _Point2d__getslice__
            
def _Point2d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point2d.__setslice__ = _Point2d__setslice__
        
def _Point2f__repr__(self):
    return "Point2f(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
Point2f.__repr__ = _Point2f__repr__
        
        
_str = "\n    Creates a Point2f view on an ndarray instance."
if Point2f.from_ndarray.__doc__ is None:
    Point2f.from_ndarray.__doc__ = _str
else:
    Point2f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Point2f that shares the same data with an ndarray instance, use:\n        'Point2f.from_ndarray(a)' or 'asPoint2f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point2f.__doc__ is None:
    Point2f.__doc__ = _str
else:
    Point2f.__doc__ += _str
    
def _Point2f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point2f.__getitem__ = _Point2f__getitem__
            
def _Point2f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point2f.__setitem__ = _Point2f__setitem__
            
def _Point2f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point2f.__getslice__ = _Point2f__getslice__
            
def _Point2f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point2f.__setslice__ = _Point2f__setslice__
        
def _Point2i__repr__(self):
    return "Point2i(x=" + repr(self.x) + ", y=" + repr(self.y) + ")"
Point2i.__repr__ = _Point2i__repr__
        
        
_str = "\n    Creates a Point2i view on an ndarray instance."
if Point2i.from_ndarray.__doc__ is None:
    Point2i.from_ndarray.__doc__ = _str
else:
    Point2i.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Point2i that shares the same data with an ndarray instance, use:\n        'Point2i.from_ndarray(a)' or 'asPoint2i(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point2i.__doc__ is None:
    Point2i.__doc__ = _str
else:
    Point2i.__doc__ += _str
    
def _Point2i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point2i.__getitem__ = _Point2i__getitem__
            
def _Point2i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point2i.__setitem__ = _Point2i__setitem__
            
def _Point2i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point2i.__getslice__ = _Point2i__getslice__
            
def _Point2i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point2i.__setslice__ = _Point2i__setslice__
        
Point = Point2i
asPoint = asPoint2i
    
_str = "\n    Creates a Point3d view on an ndarray instance."
if Point3d.from_ndarray.__doc__ is None:
    Point3d.from_ndarray.__doc__ = _str
else:
    Point3d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Point3d that shares the same data with an ndarray instance, use:\n        'Point3d.from_ndarray(a)' or 'asPoint3d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point3d.__doc__ is None:
    Point3d.__doc__ = _str
else:
    Point3d.__doc__ += _str
    
def _Point3d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point3d.__getitem__ = _Point3d__getitem__
            
def _Point3d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point3d.__setitem__ = _Point3d__setitem__
            
def _Point3d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point3d.__getslice__ = _Point3d__getslice__
            
def _Point3d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point3d.__setslice__ = _Point3d__setslice__
        
def _Point3d__repr__(self):
    return "Point3d(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
Point3d.__repr__ = _Point3d__repr__
        
        
_str = "\n    Creates a Point3f view on an ndarray instance."
if Point3f.from_ndarray.__doc__ is None:
    Point3f.from_ndarray.__doc__ = _str
else:
    Point3f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Point3f that shares the same data with an ndarray instance, use:\n        'Point3f.from_ndarray(a)' or 'asPoint3f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point3f.__doc__ is None:
    Point3f.__doc__ = _str
else:
    Point3f.__doc__ += _str
    
def _Point3f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point3f.__getitem__ = _Point3f__getitem__
            
def _Point3f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point3f.__setitem__ = _Point3f__setitem__
            
def _Point3f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point3f.__getslice__ = _Point3f__getslice__
            
def _Point3f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point3f.__setslice__ = _Point3f__setslice__
        
def _Point3f__repr__(self):
    return "Point3f(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
Point3f.__repr__ = _Point3f__repr__
        
        
_str = "\n    Creates a Point3i view on an ndarray instance."
if Point3i.from_ndarray.__doc__ is None:
    Point3i.from_ndarray.__doc__ = _str
else:
    Point3i.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Point3i that shares the same data with an ndarray instance, use:\n        'Point3i.from_ndarray(a)' or 'asPoint3i(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Point3i.__doc__ is None:
    Point3i.__doc__ = _str
else:
    Point3i.__doc__ += _str
    
def _Point3i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Point3i.__getitem__ = _Point3i__getitem__
            
def _Point3i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Point3i.__setitem__ = _Point3i__setitem__
            
def _Point3i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Point3i.__getslice__ = _Point3i__getslice__
            
def _Point3i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Point3i.__setslice__ = _Point3i__setslice__
        
def _Point3i__repr__(self):
    return "Point3i(x=" + repr(self.x) + ", y=" + repr(self.y) + ", z=" + repr(self.z) + ")"
Point3i.__repr__ = _Point3i__repr__
        
        
_str = "\n    Creates a Size2i view on an ndarray instance."
if Size2i.from_ndarray.__doc__ is None:
    Size2i.from_ndarray.__doc__ = _str
else:
    Size2i.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Size2i that shares the same data with an ndarray instance, use:\n        'Size2i.from_ndarray(a)' or 'asSize2i(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Size2i.__doc__ is None:
    Size2i.__doc__ = _str
else:
    Size2i.__doc__ += _str
    
def _Size2i__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Size2i.__getitem__ = _Size2i__getitem__
            
def _Size2i__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Size2i.__setitem__ = _Size2i__setitem__
            
def _Size2i__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Size2i.__getslice__ = _Size2i__getslice__
            
def _Size2i__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Size2i.__setslice__ = _Size2i__setslice__
        
def _Size2i__repr__(self):
    return "Size2i(width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Size2i.__repr__ = _Size2i__repr__
        
        
_str = "\n    Creates a Size2d view on an ndarray instance."
if Size2d.from_ndarray.__doc__ is None:
    Size2d.from_ndarray.__doc__ = _str
else:
    Size2d.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Size2d that shares the same data with an ndarray instance, use:\n        'Size2d.from_ndarray(a)' or 'asSize2d(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Size2d.__doc__ is None:
    Size2d.__doc__ = _str
else:
    Size2d.__doc__ += _str
    
def _Size2d__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Size2d.__getitem__ = _Size2d__getitem__
            
def _Size2d__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Size2d.__setitem__ = _Size2d__setitem__
            
def _Size2d__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Size2d.__getslice__ = _Size2d__getslice__
            
def _Size2d__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Size2d.__setslice__ = _Size2d__setslice__
        
def _Size2d__repr__(self):
    return "Size2d(width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Size2d.__repr__ = _Size2d__repr__
        
        
_str = "\n    Creates a Size2f view on an ndarray instance."
if Size2f.from_ndarray.__doc__ is None:
    Size2f.from_ndarray.__doc__ = _str
else:
    Size2f.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Size2f that shares the same data with an ndarray instance, use:\n        'Size2f.from_ndarray(a)' or 'asSize2f(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Size2f.__doc__ is None:
    Size2f.__doc__ = _str
else:
    Size2f.__doc__ += _str
    
def _Size2f__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Size2f.__getitem__ = _Size2f__getitem__
            
def _Size2f__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Size2f.__setitem__ = _Size2f__setitem__
            
def _Size2f__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Size2f.__getslice__ = _Size2f__getslice__
            
def _Size2f__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Size2f.__setslice__ = _Size2f__setslice__
        
def _Size2f__repr__(self):
    return "Size2f(width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Size2f.__repr__ = _Size2f__repr__
        
        
Size = Size2i
    
_str = "\n    Creates a Rectd view on an ndarray instance."
if Rectd.from_ndarray.__doc__ is None:
    Rectd.from_ndarray.__doc__ = _str
else:
    Rectd.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Rectd that shares the same data with an ndarray instance, use:\n        'Rectd.from_ndarray(a)' or 'asRectd(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Rectd.__doc__ is None:
    Rectd.__doc__ = _str
else:
    Rectd.__doc__ += _str
    
def _Rectd__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Rectd.__getitem__ = _Rectd__getitem__
            
def _Rectd__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Rectd.__setitem__ = _Rectd__setitem__
            
def _Rectd__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Rectd.__getslice__ = _Rectd__getslice__
            
def _Rectd__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Rectd.__setslice__ = _Rectd__setslice__
        
def _Rectd__repr__(self):
    return "Rectd(x=" + repr(self.x) + ", y=" + repr(self.y) + \
        ", width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Rectd.__repr__ = _Rectd__repr__
        
        
_str = "\n    Creates a Rectf view on an ndarray instance."
if Rectf.from_ndarray.__doc__ is None:
    Rectf.from_ndarray.__doc__ = _str
else:
    Rectf.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Rectf that shares the same data with an ndarray instance, use:\n        'Rectf.from_ndarray(a)' or 'asRectf(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Rectf.__doc__ is None:
    Rectf.__doc__ = _str
else:
    Rectf.__doc__ += _str
    
def _Rectf__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Rectf.__getitem__ = _Rectf__getitem__
            
def _Rectf__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Rectf.__setitem__ = _Rectf__setitem__
            
def _Rectf__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Rectf.__getslice__ = _Rectf__getslice__
            
def _Rectf__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Rectf.__setslice__ = _Rectf__setslice__
        
def _Rectf__repr__(self):
    return "Rectf(x=" + repr(self.x) + ", y=" + repr(self.y) + \
        ", width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Rectf.__repr__ = _Rectf__repr__
        
        
_str = "\n    Creates a Rect view on an ndarray instance."
if Rect.from_ndarray.__doc__ is None:
    Rect.from_ndarray.__doc__ = _str
else:
    Rect.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Rect that shares the same data with an ndarray instance, use:\n        'Rect.from_ndarray(a)' or 'asRect(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Rect.__doc__ is None:
    Rect.__doc__ = _str
else:
    Rect.__doc__ += _str
    
def _Rect__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Rect.__getitem__ = _Rect__getitem__
            
def _Rect__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Rect.__setitem__ = _Rect__setitem__
            
def _Rect__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Rect.__getslice__ = _Rect__getslice__
            
def _Rect__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Rect.__setslice__ = _Rect__setslice__
        
def _Rect__repr__(self):
    return "Rect(x=" + repr(self.x) + ", y=" + repr(self.y) + \
        ", width=" + repr(self.width) + ", height=" + repr(self.height) + ")"
Rect.__repr__ = _Rect__repr__
        
        
_str = "\n    Creates a RotatedRect view on an ndarray instance."
if RotatedRect.from_ndarray.__doc__ is None:
    RotatedRect.from_ndarray.__doc__ = _str
else:
    RotatedRect.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of RotatedRect that shares the same data with an ndarray instance, use:\n        'RotatedRect.from_ndarray(a)' or 'asRotatedRect(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if RotatedRect.__doc__ is None:
    RotatedRect.__doc__ = _str
else:
    RotatedRect.__doc__ += _str
    
def _RotatedRect__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
RotatedRect.__getitem__ = _RotatedRect__getitem__
            
def _RotatedRect__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
RotatedRect.__setitem__ = _RotatedRect__setitem__
            
def _RotatedRect__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
RotatedRect.__getslice__ = _RotatedRect__getslice__
            
def _RotatedRect__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
RotatedRect.__setslice__ = _RotatedRect__setslice__
        
def _RotatedRect__repr__(self):
    return "RotatedRect(center=" + repr(self.center) + ", size=" + repr(self.size) + \
        ", angle=" + repr(self.angle) + ")"
RotatedRect.__repr__ = _RotatedRect__repr__
        
    
_str = "\n    Creates a Scalar view on an ndarray instance."
if Scalar.from_ndarray.__doc__ is None:
    Scalar.from_ndarray.__doc__ = _str
else:
    Scalar.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Scalar that shares the same data with an ndarray instance, use:\n        'Scalar.from_ndarray(a)' or 'asScalar(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Scalar.__doc__ is None:
    Scalar.__doc__ = _str
else:
    Scalar.__doc__ += _str
    
def _Scalar__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Scalar.__getitem__ = _Scalar__getitem__
            
def _Scalar__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Scalar.__setitem__ = _Scalar__setitem__
            
def _Scalar__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Scalar.__getslice__ = _Scalar__getslice__
            
def _Scalar__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Scalar.__setslice__ = _Scalar__setslice__
        
def _Scalar__repr__(self):
    return "Scalar(" + self.ndarray.__str__() + ")"
Scalar.__repr__ = _Scalar__repr__
    
_str = "\n    Creates a Range view on an ndarray instance."
if Range.from_ndarray.__doc__ is None:
    Range.from_ndarray.__doc__ = _str
else:
    Range.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Range that shares the same data with an ndarray instance, use:\n        'Range.from_ndarray(a)' or 'asRange(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Range.__doc__ is None:
    Range.__doc__ = _str
else:
    Range.__doc__ += _str
    
def _Range__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Range.__getitem__ = _Range__getitem__
            
def _Range__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Range.__setitem__ = _Range__setitem__
            
def _Range__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Range.__getslice__ = _Range__getslice__
            
def _Range__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Range.__setslice__ = _Range__setslice__
        
def _Range__repr__(self):
    return "Range(start=" + repr(self.start) + ", end=" + repr(self.end) + ")"
Range.__repr__ = _Range__repr__
        
    
_str = "\n    Creates a Mat view on an ndarray instance."
if Mat.from_ndarray.__doc__ is None:
    Mat.from_ndarray.__doc__ = _str
else:
    Mat.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of Mat that shares the same data with an ndarray instance, use:\n        'Mat.from_ndarray(a)' or 'asMat(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if Mat.__doc__ is None:
    Mat.__doc__ = _str
else:
    Mat.__doc__ += _str
    
def _Mat__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
Mat.__getitem__ = _Mat__getitem__
            
def _Mat__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
Mat.__setitem__ = _Mat__setitem__
            
def _Mat__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
Mat.__getslice__ = _Mat__getslice__
            
def _Mat__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
Mat.__setslice__ = _Mat__setslice__
        
def _Mat__repr__(self):
    return "Mat()" if self.empty() else "Mat(rows=" + repr(self.rows)         + ", cols=" + repr(self.cols) + ", nchannels=" + repr(self.channels())         + ", depth=" + repr(self.depth()) + "):\n" + repr(self.ndarray)
Mat.__repr__ = _Mat__repr__
    
def asMat(obj, force_single_channel=False):
    """Converts a Python object into a Mat object.
    
    If 'force_single_channel' is True, the returing Mat is single-channel. Otherwise, PyOpenCV tries to return a multi-channel Mat whenever possible.
    """
    
    if obj is None:
        return Mat()
    
    if isinstance(obj, _NP.ndarray):
        out_mat = Mat.from_ndarray(obj)
    else:
        z = obj[0]
        if isinstance(z, int):
            out_mat = Mat.from_list_of_int32(obj)
        elif isinstance(z, float):
            out_mat = Mat.from_list_of_float64(obj)
        else:
            out_mat = eval("Mat.from_list_of_%s(obj)" % z.__class__.__name__)
    
    if force_single_channel and out_mat.channels() != 1:
        return out_mat.reshape(1, out_mat.cols if out_mat.rows==1 else out_mat.rows)
        
    return out_mat
    
def _RNG__repr__(self):
    return "RNG(state=" + repr(self.state) + ")"
RNG.__repr__ = _RNG__repr__
        
    
def _TermCriteria__repr__(self):
    return "TermCriteria(type=" + repr(self.type) + ", maxCount=" + repr(self.maxCount) + \
        ", epsilon=" + repr(self.epsilon) + ")"
TermCriteria.__repr__ = _TermCriteria__repr__
        
    
_str = "\n    Creates a MatND view on an ndarray instance."
if MatND.from_ndarray.__doc__ is None:
    MatND.from_ndarray.__doc__ = _str
else:
    MatND.from_ndarray.__doc__ += _str

_str = "\n    Property 'ndarray' provides a numpy.ndarray view on the object.\n    If you create a reference to 'ndarray', you must keep the object unchanged until your reference is deleted, or Python may crash!\n    \n    To create an instance of MatND that shares the same data with an ndarray instance, use:\n        'MatND.from_ndarray(a)' or 'asMatND(a)\n    where 'a' is an ndarray instance. Similarly, to avoid a potential Python crash, you must keep the current instance unchanged until the reference is deleted."
if MatND.__doc__ is None:
    MatND.__doc__ = _str
else:
    MatND.__doc__ += _str
    
def _MatND__getitem__(self, *args, **kwds):
    return self.ndarray.__getitem__(*args, **kwds)
MatND.__getitem__ = _MatND__getitem__
            
def _MatND__setitem__(self, *args, **kwds):
    return self.ndarray.__setitem__(*args, **kwds)
MatND.__setitem__ = _MatND__setitem__
            
def _MatND__getslice__(self, *args, **kwds):
    return self.ndarray.__getslice__(*args, **kwds)
MatND.__getslice__ = _MatND__getslice__
            
def _MatND__setslice__(self, *args, **kwds):
    return self.ndarray.__setslice__(*args, **kwds)
MatND.__setslice__ = _MatND__setslice__
        
def _MatND__repr__(self):
    return "MatND(shape=" + repr(self.ndarray.shape) + ", nchannels=" + repr(self.channels())         + ", depth=" + repr(self.depth()) + "):\n" + repr(self.ndarray)
MatND.__repr__ = _MatND__repr__
    
#=============================================================================
# cxflann.h
#=============================================================================


    
#=============================================================================
# cvtypes.h
#=============================================================================


# Defines for Distance Transform
CV_DIST_USER    = -1
CV_DIST_L1      = 1
CV_DIST_L2      = 2
CV_DIST_C       = 3
CV_DIST_L12     = 4
CV_DIST_FAIR    = 5
CV_DIST_WELSCH  = 6
CV_DIST_HUBER   = 7

# Haar-like Object Detection structures

CV_HAAR_MAGIC_VAL    = 0x42500000
CV_TYPE_NAME_HAAR    = "opencv-haar-classifier"
CV_HAAR_FEATURE_MAX  = 3


    
CvContourScanner._ownershiplevel = 0

def _CvContourScanner__del__(self):
    if self._ownershiplevel==1:
        _PE._cvEndFindContours(self)
CvContourScanner.__del__ = _CvContourScanner__del__

CvConDensation._ownershiplevel = 0

def _CvConDensation__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseConDensation(self)
CvConDensation.__del__ = _CvConDensation__del__

#=============================================================================
# cv.h
#=============================================================================


    
#-----------------------------------------------------------------------------
# Image Processing
#-----------------------------------------------------------------------------

    
CV_BLUR_NO_SCALE = 0
CV_BLUR = 1
CV_GAUSSIAN = 2
CV_MEDIAN = 3
CV_BILATERAL = 4

CV_SCHARR = -1
CV_MAX_SOBEL_KSIZE = 7

CV_BGR2BGRA =   0
CV_RGB2RGBA =   CV_BGR2BGRA

CV_BGRA2BGR =   1
CV_RGBA2RGB =   CV_BGRA2BGR

CV_BGR2RGBA =   2
CV_RGB2BGRA =   CV_BGR2RGBA

CV_RGBA2BGR =   3
CV_BGRA2RGB =   CV_RGBA2BGR

CV_BGR2RGB  =   4
CV_RGB2BGR  =   CV_BGR2RGB

CV_BGRA2RGBA =  5
CV_RGBA2BGRA =  CV_BGRA2RGBA

CV_BGR2GRAY =   6
CV_RGB2GRAY =   7
CV_GRAY2BGR =   8
CV_GRAY2RGB =   CV_GRAY2BGR
CV_GRAY2BGRA =  9
CV_GRAY2RGBA =  CV_GRAY2BGRA
CV_BGRA2GRAY =  10
CV_RGBA2GRAY =  11

CV_BGR2BGR565 = 12
CV_RGB2BGR565 = 13
CV_BGR5652BGR = 14
CV_BGR5652RGB = 15
CV_BGRA2BGR565 = 16
CV_RGBA2BGR565 = 17
CV_BGR5652BGRA = 18
CV_BGR5652RGBA = 19

CV_GRAY2BGR565 = 20
CV_BGR5652GRAY = 21

CV_BGR2BGR555  = 22
CV_RGB2BGR555  = 23
CV_BGR5552BGR  = 24
CV_BGR5552RGB  = 25
CV_BGRA2BGR555 = 26
CV_RGBA2BGR555 = 27
CV_BGR5552BGRA = 28
CV_BGR5552RGBA = 29

CV_GRAY2BGR555 = 30
CV_BGR5552GRAY = 31

CV_BGR2XYZ =    32
CV_RGB2XYZ =    33
CV_XYZ2BGR =    34
CV_XYZ2RGB =    35

CV_BGR2YCrCb =  36
CV_RGB2YCrCb =  37
CV_YCrCb2BGR =  38
CV_YCrCb2RGB =  39

CV_BGR2HSV =    40
CV_RGB2HSV =    41

CV_BGR2Lab =    44
CV_RGB2Lab =    45

CV_BayerBG2BGR = 46
CV_BayerGB2BGR = 47
CV_BayerRG2BGR = 48
CV_BayerGR2BGR = 49

CV_BayerBG2RGB = CV_BayerRG2BGR
CV_BayerGB2RGB = CV_BayerGR2BGR
CV_BayerRG2RGB = CV_BayerBG2BGR
CV_BayerGR2RGB = CV_BayerGB2BGR

CV_BGR2Luv =    50
CV_RGB2Luv =    51
CV_BGR2HLS =    52
CV_RGB2HLS =    53

CV_HSV2BGR =    54
CV_HSV2RGB =    55

CV_Lab2BGR =    56
CV_Lab2RGB =    57
CV_Luv2BGR =    58
CV_Luv2RGB =    59
CV_HLS2BGR =    60
CV_HLS2RGB =    61

CV_COLORCVT_MAX = 100

CV_WARP_FILL_OUTLIERS = 8
CV_WARP_INVERSE_MAP = 16

CV_SHAPE_RECT = 0
CV_SHAPE_CROSS = 1
CV_SHAPE_ELLIPSE = 2
CV_SHAPE_CUSTOM = 100

CV_MOP_OPEN = 2
CV_MOP_CLOSE = 3
CV_MOP_GRADIENT = 4
CV_MOP_TOPHAT = 5
CV_MOP_BLACKHAT = 6

CV_TM_SQDIFF        = 0
CV_TM_SQDIFF_NORMED = 1
CV_TM_CCORR         = 2
CV_TM_CCORR_NORMED  = 3
CV_TM_CCOEFF        = 4
CV_TM_CCOEFF_NORMED = 5



    
_str = "\n    'distance_func' is a Python function declared as follows:\n        def distance_func((int)a, (int)b, (object)userdata) -> (float)x\n    where\n        'a' : the address of a C array of C floats representing the first vector\n        'b' : the address of a C array of C floats representing the second vector\n        'userdata' : the 'userdata' parameter of cvCalcEMD2()\n        'x' : the resultant distance"
if calcEMD2.__doc__ is None:
    calcEMD2.__doc__ = _str
else:
    calcEMD2.__doc__ += _str

#-----------------------------------------------------------------------------
# Contours Retrieving
#-----------------------------------------------------------------------------


    
def endFindContours(scanner):
    z = _PE._cvEndFindContours(scanner)
    scanner._ownershiplevel = 0 # not owning the structure anymore
    return z
endFindContours.__doc__ = _PE._cvEndFindContours.__doc__
    
#-----------------------------------------------------------------------------
# Motion Analysis
#-----------------------------------------------------------------------------


CV_LKFLOW_PYR_A_READY = 1
CV_LKFLOW_PYR_B_READY = 2
CV_LKFLOW_INITIAL_GUESSES = 4
CV_LKFLOW_GET_MIN_EIGENVALS = 8


    
#-----------------------------------------------------------------------------
# Object Tracking
#-----------------------------------------------------------------------------


    
#-----------------------------------------------------------------------------
# Planar Subdivisions
#-----------------------------------------------------------------------------


    
#-----------------------------------------------------------------------------
# Contour Processing and Shape Analysis
#-----------------------------------------------------------------------------


CV_POLY_APPROX_DP = 0

CV_DOMINANT_IPAN = 1

CV_CONTOURS_MATCH_I1 = 1
CV_CONTOURS_MATCH_I2 = 2
CV_CONTOURS_MATCH_I3 = 3

CV_CONTOUR_TREES_MATCH_I1 = 1

CV_CLOCKWISE = 1
CV_COUNTER_CLOCKWISE = 2

CV_COMP_CORREL       = 0
CV_COMP_CHISQR       = 1
CV_COMP_INTERSECT    = 2
CV_COMP_BHATTACHARYYA= 3

CV_VALUE = 1
CV_ARRAY = 2

CV_DIST_MASK_3 = 3
CV_DIST_MASK_5 = 5
CV_DIST_MASK_PRECISE = 0

    
#-----------------------------------------------------------------------------
# Feature detection
#-----------------------------------------------------------------------------


    
CvFeatureTree._ownershiplevel = 0

def _CvFeatureTree__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseFeatureTree(self)
CvFeatureTree.__del__ = _CvFeatureTree__del__

CvLSH._ownershiplevel = 0

def _CvLSH__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseLSH(self)
CvLSH.__del__ = _CvLSH__del__

#-----------------------------------------------------------------------------
# POSIT (POSe from ITeration)
#-----------------------------------------------------------------------------


    
CvPOSITObject._ownershiplevel = 0

def _CvPOSITObject__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleasePOSITObject(self)
CvPOSITObject.__del__ = _CvPOSITObject__del__

#-----------------------------------------------------------------------------
# Kolmogorov-Zabin stereo-correspondence algorithm (a.k.a. KZ1)
#-----------------------------------------------------------------------------


    
CvStereoGCState._ownershiplevel = 0

def _CvStereoGCState__del__(self):
    if self._ownershiplevel==1:
        _PE._cvReleaseStereoGCState(self)
CvStereoGCState.__del__ = _CvStereoGCState__del__

#=============================================================================
# cv.hpp
#=============================================================================


    
#=============================================================================
# cvaux.h
#=============================================================================


    
#-----------------------------------------------------------------------------
# Eigen Objects
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# 1D/2D HMM
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# A few functions from old stereo gesture recognition demosions
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Additional operations on Subdivisions
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# More operations on sequences
#-----------------------------------------------------------------------------

    
    
CV_UNDEF_SC_PARAM = 12345

CV_IDP_BIRCHFIELD_PARAM1  = 25    
CV_IDP_BIRCHFIELD_PARAM2  = 5
CV_IDP_BIRCHFIELD_PARAM3  = 12
CV_IDP_BIRCHFIELD_PARAM4  = 15
CV_IDP_BIRCHFIELD_PARAM5  = 25

CV_DISPARITY_BIRCHFIELD  = 0    


    
#-----------------------------------------------------------------------------
# Contour Morphing
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Texture Descriptors
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Face eyes&mouth tracking
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# 3D Tracker
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Skeletons and Linear-Contour Models
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Background/foreground segmentation
#-----------------------------------------------------------------------------

    
    
#-----------------------------------------------------------------------------
# Calibration engine
#-----------------------------------------------------------------------------

    
    
#=============================================================================
# cvaux.hpp
#=============================================================================


    
YAPE = LDetector
    
#=============================================================================
# cvvidsurf.hpp
#=============================================================================

CV_BLOB_MINW = 5
CV_BLOB_MINH = 5


    
#=============================================================================
# ml.h
#=============================================================================

CV_LOG2PI = (1.8378770664093454835606594728112)

CV_COL_SAMPLE = 0
CV_ROW_SAMPLE = 1

def CV_IS_ROW_SAMPLE(flags):
    return ((flags) & CV_ROW_SAMPLE)

# Variable type
CV_VAR_NUMERICAL    = 0
CV_VAR_ORDERED      = 0
CV_VAR_CATEGORICAL  = 1

CV_TYPE_NAME_ML_SVM         = "opencv-ml-svm"
CV_TYPE_NAME_ML_KNN         = "opencv-ml-knn"
CV_TYPE_NAME_ML_NBAYES      = "opencv-ml-bayesian"
CV_TYPE_NAME_ML_EM          = "opencv-ml-em"
CV_TYPE_NAME_ML_BOOSTING    = "opencv-ml-boost-tree"
CV_TYPE_NAME_ML_TREE        = "opencv-ml-tree"
CV_TYPE_NAME_ML_ANN_MLP     = "opencv-ml-ann-mlp"
CV_TYPE_NAME_ML_CNN         = "opencv-ml-cnn"
CV_TYPE_NAME_ML_RTREES      = "opencv-ml-random-trees"

CV_TRAIN_ERROR  = 0
CV_TEST_ERROR   = 1

# Variable type
CV_VAR_NUMERICAL    = 0
CV_VAR_ORDERED      = 0
CV_VAR_CATEGORICAL  = 1

CV_TYPE_NAME_ML_SVM         = "opencv-ml-svm"
CV_TYPE_NAME_ML_KNN         = "opencv-ml-knn"
CV_TYPE_NAME_ML_NBAYES      = "opencv-ml-bayesian"
CV_TYPE_NAME_ML_EM          = "opencv-ml-em"
CV_TYPE_NAME_ML_BOOSTING    = "opencv-ml-boost-tree"
CV_TYPE_NAME_ML_TREE        = "opencv-ml-tree"
CV_TYPE_NAME_ML_ANN_MLP     = "opencv-ml-ann-mlp"
CV_TYPE_NAME_ML_CNN         = "opencv-ml-cnn"
CV_TYPE_NAME_ML_RTREES      = "opencv-ml-random-trees"

CV_TRAIN_ERROR  = 0
CV_TEST_ERROR   = 1

CV_TS_CONCENTRIC_SPHERES = 0

CV_COUNT     = 0
CV_PORTION   = 1

# StatModel = CvStatModel
# ParamGrid = CvParamGrid
# NormalBayesClassifier = CvNormalBayesClassifier
# KNearest = CvKNearest
# SVMParams = CvSVMParams
# SVMKernel = CvSVMKernel
# SVMSolver = CvSVMSolver
# SVM = CvSVM
# EMParams = CvEMParams
# ExpectationMaximization = CvEM
# DTreeParams = CvDTreeParams
# TrainData = CvMLData
# DecisionTree = CvDTree
# ForestTree = CvForestTree
# RandomTreeParams = CvRTParams
# RandomTrees = CvRTrees
# ERTreeTrainData = CvERTreeTrainData
# ERTree = CvForestERTree
# ERTrees = CvERTrees
# BoostParams = CvBoostParams
# BoostTree = CvBoostTree
# Boost = CvBoost
# ANN_MLP_TrainParams = CvANN_MLP_TrainParams
# NeuralNet_MLP = CvANN_MLP

    
def _CvParamGrid__repr__(self):
    return "CvParamGrid(min_val=" + repr(self.min_val) + ", max_val=" + repr(self.max_val)         + ", step=" + repr(self.step) + ")"
CvParamGrid.__repr__ = _CvParamGrid__repr__
        
    
#=============================================================================
# highgui.h
#=============================================================================


    
#-----------------------------------------------------------------------------
# Basic GUI functions 
#-----------------------------------------------------------------------------

    
CV_WINDOW_AUTOSIZE = 1

# Holds references to ctypes function wrappers for callbacks to keep the
# Python side object alive.  Keyed by window name, with a window value being
# a dictionary of callbacks, keyed by "mouse" mouse callback, or "trackbar-name"
# for a trackbar named "name".  
#
# See module bottom for atexit registration to destroy windows at process exit.
_windows_callbacks = {}

# Assigns callback for mouse events
CV_EVENT_MOUSEMOVE = 0
CV_EVENT_LBUTTONDOWN = 1
CV_EVENT_RBUTTONDOWN = 2
CV_EVENT_MBUTTONDOWN = 3
CV_EVENT_LBUTTONUP = 4
CV_EVENT_RBUTTONUP = 5
CV_EVENT_MBUTTONUP = 6
CV_EVENT_LBUTTONDBLCLK = 7
CV_EVENT_RBUTTONDBLCLK = 8
CV_EVENT_MBUTTONDBLCLK = 9

CV_EVENT_FLAG_LBUTTON = 1
CV_EVENT_FLAG_RBUTTON = 2
CV_EVENT_FLAG_MBUTTON = 4
CV_EVENT_FLAG_CTRLKEY = 8
CV_EVENT_FLAG_SHIFTKEY = 16
CV_EVENT_FLAG_ALTKEY = 32

CV_LOAD_IMAGE_UNCHANGED = -1 # 8 bit, color or gray - deprecated, use CV_LOAD_IMAGE_ANYCOLOR
CV_LOAD_IMAGE_GRAYSCALE =  0 # 8 bit, gray
CV_LOAD_IMAGE_COLOR     =  1 # 8 bit unless combined with CV_LOAD_IMAGE_ANYDEPTH, color
CV_LOAD_IMAGE_ANYDEPTH  =  2 # any depth, if specified on its own gray by itself
                             # equivalent to CV_LOAD_IMAGE_UNCHANGED but can be modified
                             # with CV_LOAD_IMAGE_ANYDEPTH
CV_LOAD_IMAGE_ANYCOLOR  =  4

CV_IMWRITE_JPEG_QUALITY = 1
CV_IMWRITE_PNG_COMPRESSION = 16
CV_IMWRITE_PXM_BINARY = 32

CV_CVTIMG_FLIP = 1
CV_CVTIMG_SWAP_RB = 2

CV_CAP_ANY = 0     # autodetect
CV_CAP_MIL = 100     # MIL proprietary drivers
CV_CAP_VFW = 200     # platform native
CV_CAP_V4L = 200
CV_CAP_V4L2 = 200
CV_CAP_FIREWARE = 300     # IEEE 1394 drivers
CV_CAP_FIREWIRE = 300     # IEEE 1394 drivers
CV_CAP_IEEE1394 = 300
CV_CAP_DC1394 = 300
CV_CAP_CMU1394 = 300
CV_CAP_STEREO = 400     # TYZX proprietary drivers
CV_CAP_TYZX = 400
CV_TYZX_LEFT = 400
CV_TYZX_RIGHT = 401
CV_TYZX_COLOR = 402
CV_TYZX_Z = 403
CV_CAP_QT = 500     # Quicktime
CV_CAP_UNICAP = 600   # Unicap drivers
CV_CAP_DSHOW = 700   # DirectShow (via videoInput)

CV_CAP_PROP_POS_MSEC      = 0
CV_CAP_PROP_POS_FRAMES    = 1
CV_CAP_PROP_POS_AVI_RATIO = 2
CV_CAP_PROP_FRAME_WIDTH   = 3
CV_CAP_PROP_FRAME_HEIGHT  = 4
CV_CAP_PROP_FPS           = 5
CV_CAP_PROP_FOURCC        = 6
CV_CAP_PROP_FRAME_COUNT   = 7
CV_CAP_PROP_FORMAT        = 8
CV_CAP_PROP_MODE          = 9
CV_CAP_PROP_BRIGHTNESS    =10
CV_CAP_PROP_CONTRAST      =11
CV_CAP_PROP_SATURATION    =12
CV_CAP_PROP_HUE           =13
CV_CAP_PROP_GAIN          =14
CV_CAP_PROP_EXPOSURE      =15
CV_CAP_PROP_CONVERT_RGB   =16
CV_CAP_PROP_WHITE_BALANCE =17
CV_CAP_PROP_RECTIFICATION =18

def CV_FOURCC(c1,c2,c3,c4):
    return (((ord(c1))&255) + (((ord(c2))&255)<<8) + (((ord(c3))&255)<<16) + (((ord(c4))&255)<<24))
    
CV_FOURCC_PROMPT = -1 # Windows only
CV_FOURCC_DEFAULT = CV_FOURCC('I', 'Y', 'U', 'V') # Linux only

    
def createTrackbar(trackbar_name, window_name, value, count, on_change=None, userdata=None):
    if not isinstance(value, _CT.c_int):
        value = _CT.c_int(value)

    result, z = _PE._cvCreateTrackbar2(trackbar_name, window_name, _CT.addressof(value), count, on_change, userdata=userdata)
    if result:
        cb_key = 'tracker-' + trackbar_name
        _windows_callbacks.setdefault(window_name,{})[cb_key] = z
    return result
createTrackbar.__doc__ = _PE._cvCreateTrackbar2.__doc__
    
_str = "\n    'value' is the initial position of the trackbar. Also, if 'value' is an instance of ctypes.c_int, it keeps the current position of the trackbar at any time.\n    'on_change' can be passed with None."
if createTrackbar.__doc__ is None:
    createTrackbar.__doc__ = _str
else:
    createTrackbar.__doc__ += _str

def setMouseCallback(window_name, on_mouse, param=None):
    _windows_callbacks.setdefault(window_name,{})["mouse"] = _PE._cvSetMouseCallback(window_name, on_mouse, param=param)
setMouseCallback.__doc__ = _PE._cvSetMouseCallback.__doc__
    
def destroyWindow(name):
    _PE._cvDestroyWindow(name)
    if name in _windows_callbacks:
        _windows_callbacks.pop(name)
destroyWindow.__doc__ = _PE._cvDestroyWindow.__doc__        
    
def destroyAllWindows():
    _PE._cvDestroyAllWindows()
    _windows_callbacks.clear()
destroyAllWindows.__doc__ = _PE._cvDestroyAllWindows.__doc__        

    
# Automatically destroy any remaining tracked windows at process exit,
# otherwise our references to ctypes objects may be destroyed by the normal
# interpreter cleanup before the highgui library cleans up fully, leaving us
# exposed to exceptions.

import atexit
atexit.register(destroyAllWindows)
    
#=============================================================================
# highgui.hpp
#=============================================================================


    
#-----------------------------------------------------------------------------
# C++ Interface
#-----------------------------------------------------------------------------

    
#=============================================================================
# sdopencv
#=============================================================================


    