import React from 'react';
import Service from '../service';

let service = new Service();

class NewCarForm extends React.Component {
    constructor(props) {
        super();
        this.props = props;
        this.state = { models1: [], models2: [] };
        this.handleChangeMake= this.handleChangeMake.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleChangeModel= this.handleChangeModel.bind(this);
        this.handleChangeZip= this.handleChangeZip.bind(this);
        this.handleSubmit= this.handleSubmit.bind(this);
    }

    handleChange(event) {
        let selectedMake = event.currentTarget.value;
        let dataMake = service.selectMake(selectedMake);

        dataMake.then((data) => {
            console.log(`Data received ${data}`);
            let modelsFromApi = data.map(m => { return { value: m, display: m } })
            this.setState({ models1: [].concat(modelsFromApi) });
        }).catch(error => {
            console.log(error);
        });
    }

    handleChangeMake(event){
        this.setState({make: event.currentTarget.value})
    }

    handleChangeModel(event){
        this.setState({model: event.currentTarget.value})
    }

    handleChangeZip(event){
        this.setState({zipcode: event.currentTarget.value})
    }


    handleSubmit(event){
        service.newCarSearch(this.state.make, this.state.model, this.state.zipcode)
            .then(data3 => {
                // console.log(data3)
                this.props.newCarSubmit(data3)
            }
            )
        event.preventDefault();
    }




    render() {
        return (

            <form className= 'newcarform'>
                <label>Choose a new car
                <select id="make1"
                        className='select'
                        onChange={(event) => this.handleChange(event)}
                        onInput={(event) => this.handleChangeMake(event)}
                    >
                        <option value="">--Make--</option>
                        <option value="Honda">Honda</option>
                        <option value="BMW">BMW</option>
                        <option value="Audi">Audi</option>
                        <option value="Toyota">Toyota</option>
                        <option value="Nissan">Nissan</option>
                    </select>
                </label>

                <label htmlFor="Model-select">Choose a model</label>
                <select id="model1"
                    className='select'
                onChange={(event) => this.handleChangeModel(event)}
                >
                    <option value="">--Model--</option>
                    {this.state.models1.map((m, i) =>
                        <option key={i} value={m.value}>{m.display}</option>)}
                </select>
                <label htmlFor="zip">Metro Area</label>
                <select id="zip2"
                    className='select'
                    onChange={(event) => this.handleChangeZip(event)}>
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
                <p><input type="submit"
                    value="Submit"
                    onClick={(event) => this.handleSubmit(event)}
                    className='myButton' /></p>

            </form>
        )
    }
}

export default NewCarForm