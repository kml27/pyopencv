// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "CvPoint3D64f.pypp.hpp"

namespace bp = boost::python;

void register_CvPoint3D64f_class(){

    bp::class_< CvPoint3D64f >( "CvPoint3D64f", "\n3D point with double precision floating-point coordinates."
    "\n"
    "\nWarning: This structure is obsolete. It exists only to support "
    "\nbackward compatibility. Please use class Point3d instead."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/basic_structures.html#cvpoint3d64f" )    
        .add_property( "this", pyplus_conv::make_addressof_inst_getter< CvPoint3D64f >(), "\n3D point with double precision floating-point coordinates."
    "\n"
    "\nWarning: This structure is obsolete. It exists only to support "
    "\nbackward compatibility. Please use class Point3d instead."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/basic_structures.html#cvpoint3d64f" )    
        .def_readwrite( "x", &CvPoint3D64f::x )    
        .def_readwrite( "y", &CvPoint3D64f::y )    
        .def_readwrite( "z", &CvPoint3D64f::z );

}
