// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "boost/python/object.hpp"
#include "boost/python/str.hpp"
#include "CvChainPtReader.pypp.hpp"

namespace bp = boost::python;

struct CvChainPtReader_wrapper : CvChainPtReader, bp::wrapper< CvChainPtReader > {

    CvChainPtReader_wrapper(CvChainPtReader const & arg )
    : CvChainPtReader( arg )
      , bp::wrapper< CvChainPtReader >(){
        // copy constructor
        
    }

    CvChainPtReader_wrapper()
    : CvChainPtReader()
      , bp::wrapper< CvChainPtReader >(){
        // null constructor
        
    }

    static bp::object get_ptr( ::CvChainPtReader const & inst ){        
        return inst.ptr? bp::str(inst.ptr): bp::object();
    }

    static bp::object get_block_min( ::CvChainPtReader const & inst ){        
        return inst.block_min? bp::str(inst.block_min): bp::object();
    }

    static bp::object get_block_max( ::CvChainPtReader const & inst ){        
        return inst.block_max? bp::str(inst.block_max): bp::object();
    }

    static bp::object get_prev_elem( ::CvChainPtReader const & inst ){        
        return inst.prev_elem? bp::str(inst.prev_elem): bp::object();
    }

};

static ::CvSeq * get_seq( ::CvChainPtReader const & inst ) { return inst.seq; }

static ::CvSeqBlock * get_block( ::CvChainPtReader const & inst ) { return inst.block; }

void register_CvChainPtReader_class(){

    bp::class_< CvChainPtReader_wrapper >( "CvChainPtReader" )    
        .add_property( "this", pyplus_conv::make_addressof_inst_getter< CvChainPtReader >() )    
        .def_readwrite( "code", &CvChainPtReader::code )    
        .def_readwrite( "delta_index", &CvChainPtReader::delta_index )    
        .def_readwrite( "header_size", &CvChainPtReader::header_size )    
        .def_readwrite( "pt", &CvChainPtReader::pt )    
        .add_property( "seq", bp::make_function(&::get_seq, bp::return_internal_reference<>()) )    
        .add_property( "block", bp::make_function(&::get_block, bp::return_internal_reference<>()) )    
        .add_property( "ptr", bp::make_function(&::CvChainPtReader_wrapper::get_ptr) )    
        .add_property( "block_min", bp::make_function(&::CvChainPtReader_wrapper::get_block_min) )    
        .add_property( "block_max", bp::make_function(&::CvChainPtReader_wrapper::get_block_max) )    
        .add_property( "prev_elem", bp::make_function(&::CvChainPtReader_wrapper::get_prev_elem) );

}
