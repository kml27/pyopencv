// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "range.pypp.hpp"

namespace bp = boost::python;

void register_Range_class(){

    { //::cv::Range
        typedef bp::class_< cv::Range > Range_exposer_t;
        Range_exposer_t Range_exposer = Range_exposer_t( "Range", bp::init< >() );
        bp::scope Range_scope( Range_exposer );
        Range_exposer.add_property( "this", pyplus_conv::make_addressof_inst_getter< cv::Range >() );
        Range_exposer.def( bp::init< int, int >(( bp::arg("_start"), bp::arg("_end") )) );
        Range_exposer.def( bp::init< CvSlice const & >(( bp::arg("slice") )) );
        bp::implicitly_convertible< CvSlice const &, cv::Range >();
        { //::cv::Range::all
        
            typedef ::cv::Range ( *all_function_type )(  );
            
            Range_exposer.def( 
                "all"
                , all_function_type( &::cv::Range::all ) );
        
        }
        { //::cv::Range::empty
        
            typedef bool ( ::cv::Range::*empty_function_type )(  ) const;
            
            Range_exposer.def( 
                "empty"
                , empty_function_type( &::cv::Range::empty ) );
        
        }
        Range_exposer.def( "as_CvSlice", &cv::Range::operator ::CvSlice  );
        { //::cv::Range::size
        
            typedef int ( ::cv::Range::*size_function_type )(  ) const;
            
            Range_exposer.def( 
                "size"
                , size_function_type( &::cv::Range::size ) );
        
        }
        Range_exposer.def_readwrite( "end", &cv::Range::end );
        Range_exposer.def_readwrite( "start", &cv::Range::start );
        Range_exposer.staticmethod( "all" );
    }

}
