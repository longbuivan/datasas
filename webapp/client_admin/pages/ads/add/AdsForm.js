import React, { Component } from 'react';

class AdsForm extends Component {
    state = {}
    render() {
        return (
            <>
                <div className="topic_form">
                    <form>
                        <div className="row">
                            <div className="col-lg-6">
                                <div className="form-group">
                                    <label htmlFor="name">Your Name</label>
                                    <input type="text"
                                        className="form-control"
                                        id="name"
                                        ref="name"
                                        name="name"
                                        placeholder="Enter your name"
                                    />
                                    {/* <small className="text-danger">{this.state.name}</small> */}
                                </div>
                                <div className="form-group">
                                    <label htmlFor="start_date">Start Date</label>
                                    <input type="date"
                                        className="form-control"
                                        id="start_date"
                                        ref="start_date"
                                        name="start_date"
                                    />
                                    {/* <small className="text-danger">{this.state.start_date}</small> */}
                                </div>
                                <div className="form-group">
                                    <label htmlFor="end_date">End Date</label>
                                    <input type="date"
                                        className="form-control"
                                        id="end_date"
                                        ref="end_date"
                                        name="end_date"
                                    />
                                    {/* <small className="text-danger">{this.state.end_date}</small> */}
                                </div>
                            </div>
                            <div className="col-lg-6">
                                <div className="form-group">
                                    <p>Target</p>
                                    <div className="custom-control custom-radio custom-control-inline">
                                        <input type="radio" className="custom-control-input" id="User" name="user" />
                                        <label className="custom-control-label" htmlFor="User">User</label>
                                    </div>
                                    <div className="custom-control custom-radio custom-control-inline">
                                        <input type="radio" className="custom-control-input" id="Banned" name="user" />
                                        <label className="custom-control-label" htmlFor="Banned">Banned</label>
                                    </div>
                                </div>
                                <div className="form-group">
                                    <label htmlFor="change_status">Change Status</label> <br />
                                    <input id="change_status" type="checkbox" data-toggle="toggle" data-onstyle="warning"/>
                                </div>
                            </div>
                        </div>
                        <button className="btn btn-success btn-sm form-control mb-3 btn_custom">Save</button>
                    </form>
                </div>
            </>
        );
    }
}

export default AdsForm;