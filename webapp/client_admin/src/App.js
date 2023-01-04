import React, { Component } from 'react';
// import logo from './logo.svg';
import './styles/Style.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Login from './pages/auth/Login';
import Singup from './pages/auth/Singup';
import Dashboard from './pages/dashboard/Dashboard';
import AddTopic from './pages/topic/add/AddTopic';
import TopicList from './pages/topic/list/TopicList';
import AdddAds from './pages/ads/add/AddAds';
import AdsList from './pages/ads/list/AdsList';
import AddPrice from './pages/pricing/add/AddPrice';
import PricingList from './pages/pricing/list/PricingList';
import ErrorPage from './pages/ErrorPage';

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Login} />
          <Route path="/singup" component={Singup} />
          <Route path="/dashboard" component={Dashboard} />
          <Route path="/add-topic" component={AddTopic} />
          <Route path="/topic-list" component={TopicList} />
          <Route path="/add-ads" component={AdddAds} />
          <Route path="/ads-list" component={AdsList} />
          <Route path="/add-pricing" component={AddPrice} />
          <Route path="/pricing-list" component={PricingList} />
          <Route component={ErrorPage} />
        </Switch>
      </BrowserRouter>
    )
  }
}
 
export default App;
