import React, { Component } from 'react';
import Nav from '../../components/Nav';
import Header from '../../components/Header';
import Widget from './Widget';

class Dashboard extends Component {
    state = {}
    render() {
        return (
            <>
                <div className="nav_bg_color" id="wrapper">
                    <Nav />
                    <div id="page-wrapper" className="gray-bg">
                        <div className="row border-bottom">
                            <Header />
                        </div>
                        <div className="wrapper wrapper-content animated fadeInRight">
                            <div className="row">
                                <div className="col-lg-3">
                                    <div className="widget style1 navy-bg">
                                        <Widget name="Today Cases" count="107" icon_name="fa fa-briefcase fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 lazur-bg">
                                        <Widget name="Advocates" count="27" icon_name="fa fa-user-circle-o fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 yellow-bg">
                                        <Widget name="Documents" count="12" icon_name="fa fa-leanpub fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 red-bg">
                                        <Widget name="Team member" count="27" icon_name="fa fa-users fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 blue-bg">
                                        <Widget name="To-Dos" count="27" icon_name="fa fa-address-card-o fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 purple-bg">
                                        <Widget name="My Case Diary" count="27" icon_name="fa fa-book fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 green-bg">
                                        <Widget name="Team 1" count="27" icon_name="fa fa-heart fa-5x" />
                                    </div>
                                </div>
                                <div className="col-lg-3">
                                    <div className="widget style1 ash-bg">
                                        <Widget name="Team 2" count="27" icon_name="fa fa-envelope-o fa-5x" />
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </>
        );
    }
}

export default Dashboard;
