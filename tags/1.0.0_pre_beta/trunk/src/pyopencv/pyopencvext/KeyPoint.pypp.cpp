// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "KeyPoint.pypp.hpp"

namespace bp = boost::python;

void register_KeyPoint_class(){

    bp::class_< cv::KeyPoint >( "KeyPoint", bp::init< >() )    
        .add_property( "this", pyplus_conv::make_addressof_inst_getter< cv::KeyPoint >() )    
        .def( bp::init< cv::Point2f, float, bp::optional< float, float, int, int > >(( bp::arg("_pt"), bp::arg("_size"), bp::arg("_angle")=-0x000000001, bp::arg("_response")=0, bp::arg("_octave")=(int)(0), bp::arg("_class_id")=(int)(-0x000000001) )) )    
        .def( bp::init< float, float, float, bp::optional< float, float, int, int > >(( bp::arg("x"), bp::arg("y"), bp::arg("_size"), bp::arg("_angle")=-0x000000001, bp::arg("_response")=0, bp::arg("_octave")=(int)(0), bp::arg("_class_id")=(int)(-0x000000001) )) )    
        .def_readwrite( "angle", &cv::KeyPoint::angle )    
        .def_readwrite( "class_id", &cv::KeyPoint::class_id )    
        .def_readwrite( "octave", &cv::KeyPoint::octave )    
        .def_readwrite( "pt", &cv::KeyPoint::pt )    
        .def_readwrite( "response", &cv::KeyPoint::response )    
        .def_readwrite( "size", &cv::KeyPoint::size );

}