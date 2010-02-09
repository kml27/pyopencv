// This file has been generated by Py++.

#include "boost/python.hpp"
#include "__ctypes_integration.pypp.hpp"
#include "opencv_headers.hpp"
#include "boost/python/object.hpp"
#include "boost/python/str.hpp"
#include "CvSeq.pypp.hpp"

namespace bp = boost::python;

struct CvSeq_wrapper : CvSeq, bp::wrapper< CvSeq > {

    CvSeq_wrapper(CvSeq const & arg )
    : CvSeq( arg )
      , bp::wrapper< CvSeq >(){
        // copy constructor
        
    }

    CvSeq_wrapper()
    : CvSeq()
      , bp::wrapper< CvSeq >(){
        // null constructor
        
    }

    static bp::object get_block_max( ::CvSeq const & inst ){        
        return inst.block_max? bp::str(inst.block_max): bp::object();
    }

    static bp::object get_ptr( ::CvSeq const & inst ){        
        return inst.ptr? bp::str(inst.ptr): bp::object();
    }

};

static ::CvSeq * get_h_prev( ::CvSeq const & inst ) { return inst.h_prev; }

static ::CvSeq * get_h_next( ::CvSeq const & inst ) { return inst.h_next; }

static ::CvSeq * get_v_prev( ::CvSeq const & inst ) { return inst.v_prev; }

static ::CvSeq * get_v_next( ::CvSeq const & inst ) { return inst.v_next; }

static ::CvMemStorage * get_storage( ::CvSeq const & inst ) { return inst.storage; }

static ::CvSeqBlock * get_free_blocks( ::CvSeq const & inst ) { return inst.free_blocks; }

static ::CvSeqBlock * get_first( ::CvSeq const & inst ) { return inst.first; }

void register_CvSeq_class(){

    bp::class_< CvSeq_wrapper >( "CvSeq" )    
        .add_property( "this", pyplus_conv::make_addressof_inst_getter< CvSeq >() )    
        .def_readwrite( "delta_elems", &CvSeq::delta_elems )    
        .def_readwrite( "elem_size", &CvSeq::elem_size )    
        .def_readwrite( "flags", &CvSeq::flags )    
        .def_readwrite( "header_size", &CvSeq::header_size )    
        .def_readwrite( "total", &CvSeq::total )    
        .add_property( "h_prev", bp::make_function(&::get_h_prev, bp::return_internal_reference<>()) )    
        .add_property( "h_next", bp::make_function(&::get_h_next, bp::return_internal_reference<>()) )    
        .add_property( "v_prev", bp::make_function(&::get_v_prev, bp::return_internal_reference<>()) )    
        .add_property( "v_next", bp::make_function(&::get_v_next, bp::return_internal_reference<>()) )    
        .add_property( "storage", bp::make_function(&::get_storage, bp::return_internal_reference<>()) )    
        .add_property( "free_blocks", bp::make_function(&::get_free_blocks, bp::return_internal_reference<>()) )    
        .add_property( "first", bp::make_function(&::get_first, bp::return_internal_reference<>()) )    
        .add_property( "block_max", bp::make_function(&::CvSeq_wrapper::get_block_max) )    
        .add_property( "ptr", bp::make_function(&::CvSeq_wrapper::get_ptr) );

}
