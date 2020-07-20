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

  componentDidMount(){
    // console.log("entre")
    this.timer();
  }


  loadHeroes = async () =>
  {
    // buscar un librerias para apis 

    // Usar una plantilla para el Front End
    const promise = await axios.get("http://localhost:8000/heroes/");
    const status = promise.status;
    if(status===200)
    {
      //console.log("hello", promise.data);
      const data = promise.data;
      this.setState({heroes:data});
      // console.log(data);
    }
  }


  timer =()=>{
    setInterval(() => {
      // console.log("hola") 
      this.loadHeroes();     
    },3000);
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