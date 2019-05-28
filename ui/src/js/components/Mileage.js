import React from 'react'

class Mileage extends React.Component{
    constructor(props) {
        super(props);
        this.state = { mileage: 'no mileage' };

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event){
        event.preventDefault();
        this.setState({mileage: event.target.value})
        let p = this.state.mileage;

        return p
    }



    render(){   
    return (
        <label htmlFor="mileage">Max Mileage
        <select  
        id="miles"
        value={this.state.mileage} 
        className= 'select'
        onChange= {this.handleChange}
        >

            <option value="">Any mileage</option>
            <option value="10000">10,000</option>
            <option value="20000">20,000</option>
            <option value="30000">30,000</option>
            <option value="50000">50,000</option>
            <option value="80000">80,000</option>
            <option value="100000">100,000</option>
            <option value="120000">120,000</option>
            <option value="150000">150,000</option>
        </select>
        </label>

    )
    }
}


export default Mileage