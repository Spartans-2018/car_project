import React from 'react'
import Service from '../service.js'

let service = new Service();

class Budgetform extends React.Component {

    constructor(props) {
        super();

        this.props = props;
        this.state = {
            // cars: [{
                amount: '10000',
                carType: 'Sedan',
                mileage: '80000',
                area: '07030',
                model: 'no model',
                color: 'black'
            // }
            // ]
        };


        this.handleChange = this.handleChange.bind(this);
        this.handleSelect = this.handleSelect.bind(this);
        this.handleChange1 = this.handleChange1.bind(this);
        this.handleChange2 = this.handleChange2.bind(this);
        this.handleChange3 = this.handleChange3.bind(this);
        this.handleChange4 = this.handleChange4.bind(this);


    }



    handleChange(event) {
        this.setState({ amount: event.target.value });
        event.preventDefault();
    }

    handleChange1(event) {
        this.setState({ carType: event.target.value });
    }

    handleChange2(event) {
        this.setState({ mileage: event.target.value });
    }

    handleChange3(event) {
        this.setState({ area: event.target.value });
    }
    handleChange4(event) {
        this.setState({ color: event.target.value });
    }


    handleSelect(event) {
        service.budget(this.state.amount,
            this.state.carType,
            this.state.mileage,
            this.state.area,
            this.state.color)
            .then((data) => {

                // Passing the retrieved data to the props submit handler
                this.props.submitHandler(data);
            })

        event.preventDefault();

    }


    render() {

        return (

            <form onSubmit={this.handleSelect}>
                <header>Find car with your budget</header>
                <br />

                <div className= 'budget-css'> 
                    <label className= 'budget-css'>Select your budget
                    <select id="budget"
                            value={this.state.amount}
                            className='select'
                            onChange={(event) => this.handleChange(event)}
                        >
                            <option value="no money">--Amount--</option>
                            <option value="3000">$3,000</option>
                            <option value="4000">$4,000</option>
                            <option value="5000">$5,000</option>
                            <option value="6000">$6,000</option>
                            <option value="7000">$7,000</option>
                            <option value="8000">$8,000</option>
                            <option value="9000">$9,000</option>
                            <option value="10000">$10,000</option>
                            <option value="12000">$12,000</option>
                            <option value="14000">$14,000</option>
                            <option value="16000">$16,000</option>
                            <option value="18000">$18,000</option>
                        </select>
                    </label>

                    <label>Select Color
                    <select id='color'
                            value={this.state.color}
                            className='select'
                            onChange={this.handleChange4}>
                            <option value="">--Color--</option>
                            <option value="silver">Silver</option>
                            <option value="grey">Grey</option>
                            <option value="black">Black</option>
                            <option value="red">Red</option>
                            <option value='white'>White</option>
                        </select>
                    </label>

                    <label >Select Car Type
                <select id="type"
                            value={this.state.carType}
                            className='select'
                            onChange={this.handleChange1}
                        >
                            <option value="">--Type--</option>
                            <option value="Sedan">Sedan</option>
                            <option value="SUV">SUV</option>
                            <option value="Coupe">Coupe</option>
                        </select>
                    </label>



                    <label >Max Mileage
                <select id="miles"
                            value={this.state.mileage}
                            className='select'
                            onChange={this.handleChange2}
                        >
                            <option value="any">Any mileage</option>
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

                    <label>Metro Area
                <select id="zipb"
                            className='select'
                            value={this.state.area}
                            onChange={this.handleChange3}
                        >
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
                </div>

                <br/>


                <input type="submit"
                    value="Submit"
                    className='myButton'
                        /*onClick= {()=>
                        service.budget(this.state.amount, 
                                        this.state.carType, 
                                        this.state.mileage, 
                                        this.state.area)}*/ />
            </form>
        )
    }
}





export default Budgetform
