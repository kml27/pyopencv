// This file has been generated by Py++.

#include "boost/python.hpp"
#include "opencv_headers.hpp"
#include "pyopencvext_free_functions_e.pypp.hpp"

namespace bp = boost::python;

void register_free_functions_e(){

    { //::cvError
    
        typedef void ( *error_function_type )( int,char const *,char const *,char const *,int );
        
        bp::def( 
            "error"
            , error_function_type( &::cvError )
            , ( bp::arg("status"), bp::arg("func_name"), bp::arg("err_msg"), bp::arg("file_name"), bp::arg("line") )
            , "\nWrapped function:"
    "\n    cvError" );
    
    }

    { //::cvErrorFromIppStatus
    
        typedef int ( *errorFromIppStatus_function_type )( int );
        
        bp::def( 
            "errorFromIppStatus"
            , errorFromIppStatus_function_type( &::cvErrorFromIppStatus )
            , ( bp::arg("ipp_status") )
            , "\nWrapped function:"
    "\n    cvErrorFromIppStatus" );
    
    }

    { //::cvErrorStr
    
        typedef char const * ( *errorStr_function_type )( int );
        
        bp::def( 
            "errorStr"
            , errorStr_function_type( &::cvErrorStr )
            , ( bp::arg("status") )
            , "\nWrapped function:"
    "\n    cvErrorStr" );
    
    }

    { //::cv::eigen
    
        typedef bool ( *eigen_function_type )( ::cv::Mat const &,::cv::Mat &,::cv::Mat &,int,int );
        
        bp::def( 
            "eigen"
            , eigen_function_type( &::cv::eigen )
            , ( bp::arg("a"), bp::arg("eigenvalues"), bp::arg("eigenvectors"), bp::arg("lowindex")=(int)(-0x000000001), bp::arg("highindex")=(int)(-0x000000001) )
            , "\nComputes eigenvalues and eigenvectors of a symmetric matrix."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/cpp/operations_on_arrays.html#cv-eigen" );
    
    }

    { //::cv::eigen
    
        typedef bool ( *eigen_function_type )( ::cv::Mat const &,::cv::Mat &,int,int );
        
        bp::def( 
            "eigen"
            , eigen_function_type( &::cv::eigen )
            , ( bp::arg("a"), bp::arg("eigenvalues"), bp::arg("lowindex")=(int)(-0x000000001), bp::arg("highindex")=(int)(-0x000000001) )
            , "\nComputes eigenvalues and eigenvectors of a symmetric matrix."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/cpp/operations_on_arrays.html#cv-eigen" );
    
    }

    { //::cv::ellipse
    
        typedef void ( *ellipse_function_type )( ::cv::Mat &,::cv::RotatedRect const &,::cv::Scalar const &,int,int );
        
        bp::def( 
            "ellipse"
            , ellipse_function_type( &::cv::ellipse )
            , ( bp::arg("img"), bp::arg("box"), bp::arg("color"), bp::arg("thickness")=(int)(1), bp::arg("lineType")=(int)(8) ) );
    
    }

    { //::cv::ellipse
    
        typedef void ( *ellipse_function_type )( ::cv::Mat &,::cv::Point,::cv::Size,double,double,double,::cv::Scalar const &,int,int,int );
        
        bp::def( 
            "ellipse"
            , ellipse_function_type( &::cv::ellipse )
            , ( bp::arg("img"), bp::arg("center"), bp::arg("axes"), bp::arg("angle"), bp::arg("startAngle"), bp::arg("endAngle"), bp::arg("color"), bp::arg("thickness")=(int)(1), bp::arg("lineType")=(int)(8), bp::arg("shift")=(int)(0) ) );
    
    }

    { //::cv::ellipse2Poly
    
        typedef void ( *ellipse2Poly_function_type )( ::cv::Point,::cv::Size,int,int,int,int,::std::vector< cv::Point_<int> > & );
        
        bp::def( 
            "ellipse2Poly"
            , ellipse2Poly_function_type( &::cv::ellipse2Poly )
            , ( bp::arg("center"), bp::arg("axes"), bp::arg("angle"), bp::arg("arcStart"), bp::arg("arcEnd"), bp::arg("delta"), bp::arg("pts") )
            , "\nApproximates an elliptic arc with a polyline."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/cpp/drawing_functions.html#cv-ellipse2poly" );
    
    }

    { //::cv::equalizeHist
    
        typedef void ( *equalizeHist_function_type )( ::cv::Mat const &,::cv::Mat & );
        
        bp::def( 
            "equalizeHist"
            , equalizeHist_function_type( &::cv::equalizeHist )
            , ( bp::arg("src"), bp::arg("dst") ) );
    
    }

    { //::cv::erode
    
        typedef void ( *erode_function_type )( ::cv::Mat const &,::cv::Mat &,::cv::Mat const &,::cv::Point,int,int,::cv::Scalar const & );
        
        bp::def( 
            "erode"
            , erode_function_type( &::cv::erode )
            , ( bp::arg("src"), bp::arg("dst"), bp::arg("kernel"), bp::arg("anchor")=cv::Point_<int>(-0x000000001, -0x000000001), bp::arg("iterations")=(int)(1), bp::arg("borderType")=int(::cv::BORDER_CONSTANT), bp::arg("borderValue")=cv::morphologyDefaultBorderValue( ) ) );
    
    }

    { //::cv::estimateAffine3D
    
        typedef int ( *estimateAffine3D_function_type )( ::cv::Mat const &,::cv::Mat const &,::cv::Mat &,::std::vector< unsigned char > &,double,double );
        
        bp::def( 
            "estimateAffine3D"
            , estimateAffine3D_function_type( &::cv::estimateAffine3D )
            , ( bp::arg("from"), bp::arg("to"), bp::arg("out"), bp::arg("outliers"), bp::arg("param1")=3.0e+0, bp::arg("param2")=9.89999999999999991118215802998747676610946655273e-1 ) );
    
    }

    { //::cv::exp
    
        typedef void ( *exp_function_type )( ::cv::MatND const &,::cv::MatND & );
        
        bp::def( 
            "exp"
            , exp_function_type( &::cv::exp )
            , ( bp::arg("a"), bp::arg("b") )
            , "\nCalculates the exponent of every array element."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/cpp/operations_on_arrays.html#cv-exp" );
    
    }

    { //::cv::exp
    
        typedef void ( *exp_function_type )( ::cv::Mat const &,::cv::Mat & );
        
        bp::def( 
            "exp"
            , exp_function_type( &::cv::exp )
            , ( bp::arg("a"), bp::arg("b") )
            , "\nCalculates the exponent of every array element."
    "\nReference:"
    "\n    http://opencv.willowgarage.com/documentation/cpp/operations_on_arrays.html#cv-exp" );
    
    }

}
