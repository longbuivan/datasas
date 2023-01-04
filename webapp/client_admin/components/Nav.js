import React, { Component } from 'react';
// import { Link } from 'react-router-dom';

class Nav extends Component {

    render() {
        return (
            <>
                <nav className="navbar-default navbar-static-side" role="navigation">
                    <div className="sidebar-collapse">
                        <ul className="nav metismenu" id="side-menu">
                            <li className="nav-header">
                                <div className="dropdown profile-element left-profile">
                                    <img className="rounded-circle" src="asset/img/profile_small.jpg" alt="" />
                                    <a href="/dashboard">
                                        <span className="block m-t-xs font-bold profile-title">My Dashboard</span>
                                    </a>
                                </div>
                                <div className="logo-element">
                                    MLC
                        </div>
                            </li>
                            <li className="active">
                                <a href="/dashboard"><i className="fa fa-th-large"></i> <span className="nav-label">Dashboard</span></a>
                            </li>
                            <li>
                                <a href="#0">
                                    <i className="fa fa-tag"></i>
                                    <span className="nav-label">Topic</span>
                                    <span className="fa arrow"></span>
                                </a>
                                <ul className="nav nav-second-level collapse">
                                    <li><a href="/add-topic" >Add Topic</a></li>
                                    <li><a href="/topic-list" >Topic List</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="#0">
                                    <i className="fa fa-newspaper-o"></i>
                                    <span className="nav-label">Ads</span>
                                    <span className="fa arrow"></span>
                                </a>
                                <ul className="nav nav-second-level collapse">
                                    <li><a href="/add-ads" >Add Ads</a></li>
                                    <li><a href="/ads-list" >Ads List</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="#0">
                                    <i className="fa fa-money"></i>
                                    <span className="nav-label">Pricing</span>
                                    <span className="fa arrow"></span>
                                </a>
                                <ul className="nav nav-second-level collapse">
                                    <li><a href="/add-pricing" >Add New Pricing</a></li>
                                    <li><a href="/pricing-list" >Pricing List</a></li>
                                </ul>
                            </li>
                            <li>
                                <a href="#0"><i className="fa fa-users"></i> <span className="nav-label">Team</span></a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </>
        );
    }
}

export default Nav;
