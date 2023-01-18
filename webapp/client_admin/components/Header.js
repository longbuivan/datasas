import React, { Component } from 'react';

class Header extends Component {
    state = {}
    render() {
        return (
            <>
                <nav className="navbar navbar-static-top white-bg" role="navigation">
                    <div className="navbar-header">
                        <a className="navbar-minimalize minimalize-styl-2 btn btn-succcess btn-sm" href="#0"><i className="fa fa-bars"></i> </a>
                        <form role="search" className="navbar-form-custom" method="post" action="#0">
                            <div className="form-group">
                                <input type="text" placeholder="Search for something..." className="form-control" name="top-search" id="top-search" />
                            </div>
                        </form>
                    </div>
                    <ul className="nav navbar-top-links navbar-right">
                        <li>
                            <a href="/">
                                <i className="fa fa-sign-out"></i> Log out
                            </a>
                        </li>
                    </ul>
                </nav>
            </>
        );
    }
}

export default Header;
