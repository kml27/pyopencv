// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "boost/python/object.hpp"
#include "CvConnectedComp.pypp.hpp"

namespace bp = boost::python;

static cv::Scalar_<double> *get_value(CvConnectedComp const &inst) { return (cv::Scalar_<double> *)(&inst.value); }

static cv::Rect_<int> *get_rect(CvConnectedComp const &inst) { return (cv::Rect_<int> *)(&inst.rect); }

static ::CvSeq * get_contour( ::CvConnectedComp const & inst ) { return inst.contour; }

void register_CvConnectedComp_class(){

    bp::class_< CvConnectedComp >( "CvConnectedComp" )    
        .add_property( "this", pyplus_conv::make_addressof_inst_getter< CvConnectedComp >() )    
        .def_readwrite( "area", &CvConnectedComp::area )    
        .add_property( "value", bp::make_function(&::get_value, bp::return_internal_reference<>()) )    
        .add_property( "rect", bp::make_function(&::get_rect, bp::return_internal_reference<>()) )    
        .add_property( "contour", bp::make_function(&::get_contour, bp::return_internal_reference<>()) );

}
