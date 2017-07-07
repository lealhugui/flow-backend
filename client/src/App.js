import React, { Component } from 'react';
//import logo from './logo.svg';
import './App.css';
import LoginForm from './components/LoginForm';

class App extends Component {
  
  constructor(){
    super();
    this.state={u: null}
  }
  
  checkUser = () => {
    if(this.state.u===null){
      this.setState({u: localStorage.getItem("uTk")}, () => {
        return this.state.u===null
      });
    }
  }
  
  render() {
    
    let stl = {
      fontSize: "small",
      textAlign: "right"
    }
    
    let main = null;
    if(this.state.u===null){
      
      main = <LoginForm />;
    } else {
      main = (
        <button onClick={
            () => { 
              localStorage.setItem("uTk", null);
              this.setState({u: null});
            }
           }></button>
      )
    }
    
    return (
      <div>        
        <div id="message">
          <h1>Flow</h1>          
          <div>welcome</div>
          
          <div style={stl}><a href="https://www.databeyond.info">by DataBeyond</a></div>
        </div>        
      </div>
    );
  }
}

export default App;
