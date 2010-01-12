// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "cvmserparams.pypp.hpp"

namespace bp = boost::python;

void register_CvMSERParams_class(){

    bp::class_< CvMSERParams >( "CvMSERParams" )    
        .add_property( "this", pyplus_conv::make_addressof_inst_getter< CvMSERParams >() )    
        .def_readwrite( "areaThreshold", &CvMSERParams::areaThreshold )    
        .def_readwrite( "delta", &CvMSERParams::delta )    
        .def_readwrite( "edgeBlurSize", &CvMSERParams::edgeBlurSize )    
        .def_readwrite( "maxArea", &CvMSERParams::maxArea )    
        .def_readwrite( "maxEvolution", &CvMSERParams::maxEvolution )    
        .def_readwrite( "maxVariation", &CvMSERParams::maxVariation )    
        .def_readwrite( "minArea", &CvMSERParams::minArea )    
        .def_readwrite( "minDiversity", &CvMSERParams::minDiversity )    
        .def_readwrite( "minMargin", &CvMSERParams::minMargin );

}