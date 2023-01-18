import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class PageTitle extends Component {

    render() { 
        return (
            <>
                <div className="row page_title mb-4">
                    <div className="col-lg-4">
                        <p>{this.props.page_headline}</p>
                    </div>
                    <div className="col-lg-8 text-right">
                        <div className="pageRight">
                            <Link to='/dashboard'>Dashboard</Link>
                        </div>
                    </div>
                </div>
            </>
        );
    }
}
 
export default PageTitle;
