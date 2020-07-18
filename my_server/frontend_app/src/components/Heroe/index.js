import React, { Component } from "react";

import axios from "axios";

class Heroe extends Component {
  constructor(props) {
    super(props);
    this.state = {
      heroes:[],
    };
  }

  componentWillMount() {
    this.loadHeroes();
  }

  loadHeroes = async () =>
  {
    const promise = await axios.get("http://localhost:8000/heroes/");
    const status = promise.status;
    if(status===200)
    {
      //console.log("hello", promise.data);
      const data = promise.data;
      this.setState({heroes:data});
      console.log(data);
    }
  }

  render() {
    return(
      <div>
        <h1>Heroes</h1>
    {this.state.heroes.map((value, index )=> <p>Index: {index} Name: {value.name} Alias: {value.alias}</p>)}
      </div>
    )
  }
}

export default Heroe;