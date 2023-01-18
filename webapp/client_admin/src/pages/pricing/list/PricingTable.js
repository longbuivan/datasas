import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import swal from "sweetalert";

class PricingTable extends Component {
    state = {}

    // Delete handler
    handleDelete() {
        swal({
            title: "Are you sure?",
            text: "Will you delete the experience",
            icon: "warning",
            buttons: ["No", "Yes"],
            dangerMode: true
        }).then(willDelete => {
            if (willDelete) {
                swal("Deleted!", "Your imaginary file has been deleted!", "success");
            }
        })
    }

    render() {
        return (
            <>
                <table id="dtBasicExample" className="table table-striped table-bordered table-sm">
                    <thead>
                        <tr>
                            <th className="th-sm">SL</th>
                            <th className="th-sm">Name</th>
                            <th className="th-sm">Status </th>
                            <th className="th-sm">Target</th>
                            <th className="th-sm">Start Date</th>
                            <th className="th-sm">End Date</th>
                            <th className="th-sm">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                        <tr>
                            <td>#01</td>
                            <td>Tiger Nixon</td>
                            <td>System Architect</td>
                            <td>Edinburgh</td>
                            <td>011/04/25</td>
                            <td>2011/04/25</td>
                            <td>
                                <Link to="/" className="btn btn-info btn-sm mr-1"><i className="fa fa-eye"></i></Link>
                                <button className="btn btn-info btn-sm mr-1"><i className="fa fa-pencil"></i></button>
                                <button
                                    onClick={e => this.handleDelete()}
                                    className="btn btn-danger btn-sm mr-1">
                                    <i className="fa fa-trash"></i>
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </>
        );
    }
}

export default PricingTable;
