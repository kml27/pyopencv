// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "boost/python/object.hpp"
#include "Seq_CvConnectedComp.pypp.hpp"

namespace bp = boost::python;

static size_t Seq_CvConnectedComp_len(cv::Seq<CvConnectedComp> const &inst) { return inst.size(); }

static ::CvSeq * get_seq( ::cv::Seq<CvConnectedComp> const & inst ) { return inst.seq; }

void register_Seq_CvConnectedComp_class(){

    { //::cv::Seq< CvConnectedComp >
        typedef bp::class_< cv::Seq< CvConnectedComp > > Seq_CvConnectedComp_exposer_t;
        Seq_CvConnectedComp_exposer_t Seq_CvConnectedComp_exposer = Seq_CvConnectedComp_exposer_t( "Seq_CvConnectedComp", bp::init< >() );
        bp::scope Seq_CvConnectedComp_scope( Seq_CvConnectedComp_exposer );
        Seq_CvConnectedComp_exposer.add_property( "this", pyplus_conv::make_addressof_inst_getter< cv::Seq< CvConnectedComp > >() );
        Seq_CvConnectedComp_exposer.def( bp::init< CvSeq const * >(( bp::arg("_seq") )) );
        bp::implicitly_convertible< CvSeq const *, cv::Seq< CvConnectedComp > >();
        Seq_CvConnectedComp_exposer.def( bp::init< cv::Ptr< CvMemStorage > &, bp::optional< int > >(( bp::arg("storage"), bp::arg("headerSize")=(int)(56u) )) );
        bp::implicitly_convertible< cv::Ptr< CvMemStorage > &, cv::Seq< CvConnectedComp > >();
        { //::cv::Seq< CvConnectedComp >::channels
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef int ( exported_class_t::*channels_function_type )(  ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "channels"
                , channels_function_type( &::cv::Seq< CvConnectedComp >::channels ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::clear
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*clear_function_type )(  ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "clear"
                , clear_function_type( &::cv::Seq< CvConnectedComp >::clear ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::copyTo
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*copyTo_function_type )( ::std::vector< CvConnectedComp > &,::cv::Range const & ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "copyTo"
                , copyTo_function_type( &::cv::Seq< CvConnectedComp >::copyTo )
                , ( bp::arg("vec"), bp::arg("range")=cv::Range::all() ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::depth
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef int ( exported_class_t::*depth_function_type )(  ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "depth"
                , depth_function_type( &::cv::Seq< CvConnectedComp >::depth ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::elemSize
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef ::size_t ( exported_class_t::*elemSize_function_type )(  ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "elemSize"
                , elemSize_function_type( &::cv::Seq< CvConnectedComp >::elemSize ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::empty
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef bool ( exported_class_t::*empty_function_type )(  ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "empty"
                , empty_function_type( &::cv::Seq< CvConnectedComp >::empty ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::index
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef ::size_t ( exported_class_t::*index_function_type )( ::CvConnectedComp const & ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "index"
                , index_function_type( &::cv::Seq< CvConnectedComp >::index )
                , ( bp::arg("elem") ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::insert
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*insert_function_type )( int,::CvConnectedComp const & ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "insert"
                , insert_function_type( &::cv::Seq< CvConnectedComp >::insert )
                , ( bp::arg("idx"), bp::arg("elem") ) );
        
        }
        Seq_CvConnectedComp_exposer.def( "__temp_func", &cv::Seq< CvConnectedComp >::operator ::std::vector< CvConnectedComp > , "\nWrapped function:"
    "\n    operator ::std::vector<CvConnectedComp, "
    "\n    std::allocator<CvConnectedComp> >" );
        { //::cv::Seq< CvConnectedComp >::operator[]
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef ::CvConnectedComp & ( exported_class_t::*__getitem___function_type )( int ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::cv::Seq< CvConnectedComp >::operator[] )
                , ( bp::arg("idx") )
                , bp::return_internal_reference< >()
                , "\nWrapped function:"
    "\n    operator[]" );
        
        }
        { //::cv::Seq< CvConnectedComp >::operator[]
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef ::CvConnectedComp const & ( exported_class_t::*__getitem___function_type )( int ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "__getitem__"
                , __getitem___function_type( &::cv::Seq< CvConnectedComp >::operator[] )
                , ( bp::arg("idx") )
                , bp::return_value_policy< bp::copy_const_reference >()
                , "\nWrapped function:"
    "\n    operator[]" );
        
        }
        { //::cv::Seq< CvConnectedComp >::pop_back
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*pop_back_function_type )(  ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "pop_back"
                , pop_back_function_type( &::cv::Seq< CvConnectedComp >::pop_back ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::pop_front
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*pop_front_function_type )(  ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "pop_front"
                , pop_front_function_type( &::cv::Seq< CvConnectedComp >::pop_front ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::push_back
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*push_back_function_type )( ::CvConnectedComp const & ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "push_back"
                , push_back_function_type( &::cv::Seq< CvConnectedComp >::push_back )
                , ( bp::arg("elem") ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::push_front
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*push_front_function_type )( ::CvConnectedComp const & ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "push_front"
                , push_front_function_type( &::cv::Seq< CvConnectedComp >::push_front )
                , ( bp::arg("elem") ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::remove
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*remove_function_type )( int ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "remove"
                , remove_function_type( &::cv::Seq< CvConnectedComp >::remove )
                , ( bp::arg("idx") ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::remove
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef void ( exported_class_t::*remove_function_type )( ::cv::Range const & ) ;
            
            Seq_CvConnectedComp_exposer.def( 
                "remove"
                , remove_function_type( &::cv::Seq< CvConnectedComp >::remove )
                , ( bp::arg("r") ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::size
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef ::size_t ( exported_class_t::*size_function_type )(  ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "size"
                , size_function_type( &::cv::Seq< CvConnectedComp >::size ) );
        
        }
        { //::cv::Seq< CvConnectedComp >::type
        
            typedef cv::Seq< CvConnectedComp > exported_class_t;
            typedef int ( exported_class_t::*type_function_type )(  ) const;
            
            Seq_CvConnectedComp_exposer.def( 
                "type"
                , type_function_type( &::cv::Seq< CvConnectedComp >::type ) );
        
        }
        Seq_CvConnectedComp_exposer.def("__len__", &::Seq_CvConnectedComp_len);
        Seq_CvConnectedComp_exposer.add_property( "seq", bp::make_function(&::get_seq, bp::return_internal_reference<>()) );
    }

}
