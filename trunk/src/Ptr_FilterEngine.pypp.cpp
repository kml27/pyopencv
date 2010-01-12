// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "ptr_filterengine.pypp.hpp"

namespace bp = boost::python;

cv::FilterEngine const &pointee_FilterEngine(cv::Ptr<cv::FilterEngine> const &inst) { return *((cv::FilterEngine const *)inst); }

void register_Ptr_FilterEngine_class(){

    { //::cv::Ptr< cv::FilterEngine >
        typedef bp::class_< cv::Ptr< cv::FilterEngine > > Ptr_FilterEngine_exposer_t;
        Ptr_FilterEngine_exposer_t Ptr_FilterEngine_exposer = Ptr_FilterEngine_exposer_t( "Ptr_FilterEngine" );
        bp::scope Ptr_FilterEngine_scope( Ptr_FilterEngine_exposer );
        Ptr_FilterEngine_exposer.add_property( "this", pyplus_conv::make_addressof_inst_getter< cv::Ptr< cv::FilterEngine > >() );
        { //::cv::Ptr< cv::FilterEngine >::addref
        
            typedef cv::Ptr< cv::FilterEngine > exported_class_t;
            typedef void ( exported_class_t::*addref_function_type )(  ) ;
            
            Ptr_FilterEngine_exposer.def( 
                "addref"
                , addref_function_type( &::cv::Ptr< cv::FilterEngine >::addref ) );
        
        }
        { //::cv::Ptr< cv::FilterEngine >::delete_obj
        
            typedef cv::Ptr< cv::FilterEngine > exported_class_t;
            typedef void ( exported_class_t::*delete_obj_function_type )(  ) ;
            
            Ptr_FilterEngine_exposer.def( 
                "delete_obj"
                , delete_obj_function_type( &::cv::Ptr< cv::FilterEngine >::delete_obj ) );
        
        }
        { //::cv::Ptr< cv::FilterEngine >::empty
        
            typedef cv::Ptr< cv::FilterEngine > exported_class_t;
            typedef bool ( exported_class_t::*empty_function_type )(  ) const;
            
            Ptr_FilterEngine_exposer.def( 
                "empty"
                , empty_function_type( &::cv::Ptr< cv::FilterEngine >::empty ) );
        
        }
        { //::cv::Ptr< cv::FilterEngine >::release
        
            typedef cv::Ptr< cv::FilterEngine > exported_class_t;
            typedef void ( exported_class_t::*release_function_type )(  ) ;
            
            Ptr_FilterEngine_exposer.def( 
                "release"
                , release_function_type( &::cv::Ptr< cv::FilterEngine >::release ) );
        
        }
        Ptr_FilterEngine_exposer.add_property("pointee", bp::make_function(&pointee_FilterEngine, bp::return_internal_reference<>()));
    }

}
