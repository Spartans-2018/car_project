import React from 'react'


class Child extends React.Component{
    constructor (props){
        super();
        this.props= props;
        this.state ={value: ''};
        this.handleChange=this.handleChange.bind(this);
        this.handleSubmit=this.handleSubmit.bind(this);

    }




handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    var data= {value: event.target[0].value};
    this.props.submitChild(data);

    
    
    event.preventDefault();
  }

  render() {
    return (
      <form onSubmit={this.handleSubmit}
            value='super'>
        <label>
          Name:
          <input type="text" 
          value={this.state.value} 
          onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    );
  }


    
}

export default Child