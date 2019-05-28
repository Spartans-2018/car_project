import React from 'react'

class Budget extends React.Component {

    constructor(props) {
        super(props);
        this.state = { amount: 'zero' };
       

        this.handleChange = this.handleChange.bind(this);
        this.handleSelect = this.handleSelect.bind(this);
    }

    handleChange(event) {
        
      this.setState({ amount: event.target.value });  
      
      
    }

    handleSelect(event) {
        
        alert('Is your budget: ' + this.state.amount);
        console.log('test', this.state.amount);
        event.preventDefault();
        
    }


    render() {
        
        return (
            
                <label    >Select budget
                    <select id="budget" 
                            value= {this.state.amount} 
                            className='select' 
                            onChange={this.handleChange}>

                        <option value="no money">--Amount--</option>
                        <option  value="3000">$3,000</option>
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
             
        )
    }
}
export default Budget