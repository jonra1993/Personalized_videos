import React, { Component } from 'react';
import './App.css';

import { BrowserRouter as Router, Route } from "react-router-dom";

import Heroe from "./components/Heroe/index";

class App extends Component {
  render() {
    return (
      <Router>
        <Route path="/" exact component={Heroe} />
    </Router>
    );
  }
}

export default App;