import React, { useState } from "react";

/// React router dom
import { Link } from "react-router-dom";

/// images
import logo from "../../../images/logo.png";
import logoText from "../../../images/logo-text.png";

const NavHader = () => {
  //show full navbar if toggle is false
  const [toggle, setToggle] = useState(false);

  return (
    <div className="nav-header">
      <Link to="/" className="brand-logo">
        <img className="logo-abbr" src={logo} alt="logo" />
        <img className="logo-compact" src={logoText} alt="logo-compact" />
        <img className="brand-title" src={logoText} alt="logo-title" />
      </Link>

      <div className="nav-control" onClick={() => setToggle(!toggle)}>
        <div className={`hamburger ${toggle ? "is-active" : ""}`}>
          <span className="line"></span>
          <span className="line"></span>
          <span className="line"></span>
        </div>
      </div>
    </div>
  );
};

export default NavHader;
