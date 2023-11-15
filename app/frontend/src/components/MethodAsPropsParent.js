import React, {Component} from 'react';
import MethodAsPropsChild from "./MethodAsPropsChild";

class MethodAsPropsParent extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false
    }
  }

  handleSignIn = () => {
    // this.setState({
    //   isLoggedIn: true
    // })
    // console.log(this);
    this.setState(prevState => ({
      isLoggedIn: !prevState.isLoggedIn
    }))
  }


  render() {
    return (
      <div>
        <MethodAsPropsChild
          isLoggedIn={this.state.isLoggedIn}
          // Pass the function down to the child
          handleSignIn={this.handleSignIn}
        />
      </div>
    );
  }
}

export default MethodAsPropsParent;