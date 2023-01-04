import React, { Component } from 'react';

class TopicForm extends Component {
    state = {  }
    render() { 
        return (
            <>
                <div className="topic_form">
                    <form>
                        <div className="row">
                            <div className="col-lg-4">
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
                            </div>
                            <div className="col-lg-4">
                                <div className="form-group">
                                    <label htmlFor="subject">Subject</label>
                                    <input type="text"
                                        className="form-control"
                                        id="subject"
                                        ref="subject"
                                        name="subject"
                                        placeholder="Enter subject"
                                    />
                                    {/* <small className="text-danger">{this.state.subject}</small> */}
                                </div>
                            </div>
                            <div className="col-lg-4">
                                <div className="form-group">
                                    <label htmlFor="sub_topic">Sub Topic</label>
                                    <input type="text"
                                        className="form-control"
                                        id="sub_topic"
                                        ref="sub_topic"
                                        name="sub_topic"
                                        placeholder="Enter sub topic"
                                    />
                                    {/* <small className="text-danger">{this.state.name}</small> */}
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
 
export default TopicForm;
