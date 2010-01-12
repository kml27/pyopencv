// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "ndarray.hpp"
#include "point3f.pypp.hpp"

namespace bp = boost::python;

void register_Point3f_class(){

    { //::cv::Point3_< float >
        typedef bp::class_< cv::Point3_< float > > Point3f_exposer_t;
        Point3f_exposer_t Point3f_exposer = Point3f_exposer_t( "Point3f", bp::init< >() );
        bp::scope Point3f_scope( Point3f_exposer );
        Point3f_exposer.add_property( "this", pyplus_conv::make_addressof_inst_getter< cv::Point3_< float > >() );
        Point3f_exposer.def( bp::init< float, float, float >(( bp::arg("_x"), bp::arg("_y"), bp::arg("_z") )) );
        Point3f_exposer.def( bp::init< cv::Point3_< float > const & >(( bp::arg("pt") )) );
        Point3f_exposer.def( bp::init< cv::Point_< float > const & >(( bp::arg("pt") )) );
        bp::implicitly_convertible< cv::Point_< float > const &, cv::Point3_< float > >();
        Point3f_exposer.def( bp::init< cv::Vec< float, 3 > const & >(( bp::arg("v") )) );
        bp::implicitly_convertible< cv::Vec< float, 3 > const &, cv::Point3_< float > >();
        { //::cv::Point3_< float >::ddot
        
            typedef cv::Point3_< float > exported_class_t;
            typedef double ( exported_class_t::*ddot_function_type )( ::cv::Point3_< float > const & ) const;
            
            Point3f_exposer.def( 
                "ddot"
                , ddot_function_type( &::cv::Point3_< float >::ddot )
                , ( bp::arg("pt") ) );
        
        }
        { //::cv::Point3_< float >::dot
        
            typedef cv::Point3_< float > exported_class_t;
            typedef float ( exported_class_t::*dot_function_type )( ::cv::Point3_< float > const & ) const;
            
            Point3f_exposer.def( 
                "dot"
                , dot_function_type( &::cv::Point3_< float >::dot )
                , ( bp::arg("pt") ) );
        
        }
        Point3f_exposer.def( "as_Vec3f", &cv::Point3_< float >::operator ::cv::Vec< float, 3 >  );
        { //::cv::Point3_< float >::operator=
        
            typedef cv::Point3_< float > exported_class_t;
            typedef ::cv::Point3_< float > & ( exported_class_t::*assign_function_type )( ::cv::Point3_< float > const & ) ;
            
            Point3f_exposer.def( 
                "assign"
                , assign_function_type( &::cv::Point3_< float >::operator= )
                , ( bp::arg("pt") )
                , bp::return_self< >() );
        
        }
        Point3f_exposer.def_readwrite( "x", &cv::Point3_< float >::x );
        Point3f_exposer.def_readwrite( "y", &cv::Point3_< float >::y );
        Point3f_exposer.def_readwrite( "z", &cv::Point3_< float >::z );
        Point3f_exposer.def("from_ndarray", &bp::as_Point3f);
        Point3f_exposer.staticmethod("from_ndarray");
        Point3f_exposer.add_property("ndarray", &bp::as_ndarray);
    }

}
