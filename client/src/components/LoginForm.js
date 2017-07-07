import React, { Component } from 'react';

class LoginForm extends Component{
    
    constructor(){
        super();
        this.state = {username: "", pass: ""};
    }

    handleSubmit = (e) => {
        e.preventDefault();
        
        this.doLogin(this.state)
    }
    
    doLogin = ({username, password}) => {
        /* mock login */
        localStorage.setItem("uTk", "mocked");
    }
    
    render(){
        return (
            <div>
                <form onSubmit={this.handleSubmit}>
                    <div>
                        <label>Usuário</label>
                        <input type="text" value={this.state.username}
                            onChange={(e) => {this.setState({username: e.target.value})}}></input>
                    </div>
                    <div>
                        <label>Senha</label>
                        <input type="password" value={this.state.pass}
                            onChange={(e) => {this.setState({pass: e.target.value})}}></input>
                       
                    </div>
                    <input type="submit" value="Entrar"></input>
                </form>
            </div>
        );
    }
}

export default LoginForm;