import React, { Component } from 'react';

class Pagination extends Component {
    state = {  }
    render() { 
        return (
            <>
                <ul className="pagination">
                    <li className="page-item"><a className="page-link" href="#0">Previous</a></li>
                    <li className="page-item"><a className="page-link" href="#0">1</a></li>
                    <li className="page-item"><a className="page-link" href="#0">2</a></li>
                    <li className="page-item"><a className="className-link" href="#0">3</a></li>
                    <li className="page-item"><a className="page-link" href="#0">Next</a></li>
                </ul>
            </>
        );
    }
}
 
export default Pagination;
