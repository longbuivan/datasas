import { useEffect } from "react";
import { useLocation } from "react-router-dom";

export default function ScrollToTop() {
  const { pathname } = useLocation();

  //go to top when change page
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  return null;
}
