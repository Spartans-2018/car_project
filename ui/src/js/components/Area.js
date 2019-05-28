import React from 'react'

class Area extends React.Component{

    constructor(props) {
        super(props);
        this.state = { area: 'no data' };

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event){
        event.preventDefault()
        this.setState({area: event.target.value});
        let p = this.state.area
        return p

    }


    render(){
    return(
        <label htmlFor="zip-budget">Metro Area
        <select id="zipb" 
                className= 'select'
                value= {this.state.area}
                onChange= {this.handleChange}>

            
            <option value="">--Metro Area--</option>
            <option value="07030">New Yor City</option>
            <option value="90010">Los Angeles</option>
            <option value="60020">Chicago</option>
            <option value="75202">Dallas</option>
            <option value="77024">Houston</option>
            <option value="20022">Washington, DC</option>
            <option value="33101">Miami</option>
            <option value="30301">Atlanta</option>
            <option value="02101">Boston</option>
            <option value="85020">Phoenix</option>
            <option value="48216">Detroit</option>
            <option value="98111">Seattle</option>
            <option value="55412">Minneapolis</option>
            <option value="80212">Denver</option>
            <option value="63109">St. Louis</option>
        </select>
        </label>
    )
    }
}

export default Area