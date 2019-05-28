import React from 'react'


class CarType extends React.Component{
    constructor(props) {
        super(props);
        this.state = { carType: 'no type' };

        this.handleChange = this.handleChange.bind(this);
    }

    handleChange(event) {
        event.preventDefault();
       this.setState({ carType: event.target.value });
       let p= this.state.carType;
       
        return p
    }



    render() {
        return (
            <label htmlFor="carType">Select Car Type
                <select id="type" 
                        value={this.state.carType}
                        className='select'
                        onChange= {this.handleChange}
                >

                    <option value="">--Type--</option>
                    <option value="Sedan">Sedan</option>
                    <option value="SUV">SUV</option>
                    <option value="Coupe">Coupe</option>
                </select>

            </label>
        )
    }
}


export default CarType