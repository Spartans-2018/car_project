import React from 'react'
import Service from '../service'

import $ from 'jquery';
import jQuery from 'jquery';
// window.$ = jQuery;

let service = new Service();

class Compareform extends React.Component {
    constructor(props) {
        super();
        this.props = props;
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange1 = this.handleChange1.bind(this);
        this.handleChange2 = this.handleChange2.bind(this);
        this.handleChangeModel = this.handleChangeModel.bind(this)
        this.handleChangeFromYear = this.handleChangeFromYear.bind(this)
        this.handleChangeToYear = this.handleChangeToYear.bind(this)
        this.handleChangeZip = this.handleChangeZip.bind(this)
        this.handleChangeMake = this.handleChangeMake.bind(this)
        this.state = { models1: [], models2: [] }
    }


    handleSubmit(event) {
        service.completeMake(this.state.zipcode,
            this.state.fromyear,
            this.state.toyear,
            this.state.make,
            this.state.model
        )
            .then((data1) => {
                // console.log(data1)
                this.props.submitHandlerGraph(data1)
            });
        event.preventDefault();
    }


    handleChange1(event) {
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

    handleChange2(event) {
        let selectedMake = event.currentTarget.value;
        let dataMake = service.selectMake(selectedMake);

        dataMake.then((data) => {
            console.log(`Data received ${data}`);
            let modelsFromApi = data.map(m => { return { value: m, display: m } })
            this.setState({ models2: [].concat(modelsFromApi) });
        }).catch(error => {
            console.log(error);
        });
    }

    handleChangeMake(event) {
        event.preventDefault()

        let makeValue1 = $("#make1").val()
        let makeValue2 = $("#make2").val()
        this.setState({ make: [makeValue1, makeValue2] })
    }

    handleChangeModel(event) {
        event.preventDefault()

        let modelValue1 = $("#model1").val()
        let modelValue2 = $("#model2").val()
        this.setState({ model: [modelValue1, modelValue2] })
    }

    handleChangeFromYear(event) {
        event.preventDefault()

        let fromYearValue1 = $("#fromyear1").val()
        let fromYearValue2 = $("#fromyear2").val()
        this.setState({ fromyear: [fromYearValue1, fromYearValue2] })
    }

    handleChangeToYear(event) {
        event.preventDefault()

        let toYearValue1 = $("#toyear1").val()
        let toYearValue2 = $("#toyear2").val()
        this.setState({ toyear: [toYearValue1, toYearValue2] })
    }

    handleChangeZip(event) {
        event.preventDefault()

        let zipValue1 = $("#zip1").val()
        let zipValue2 = $("#zip2").val()
        this.setState({ zipcode: [zipValue1, zipValue2] })
    }




    render() {


        return (

            <form 
            // class= 'myButton'
            // onSubmit={this.handleSelect(event)}
            >
                <header>Compare cars by Make and Model</header>
                <br />
                <div className='compare'>
                    <div>1st choice </div>
                    <label htmlFor="Car-select">Choose a car</label>
                    <select id="make1"
                        className='select'
                        onChange={(event) => this.handleChange1(event)}
                        onInput={(event) => this.handleChangeMake(event)}
                    >
                        <option value="">--Make--</option>
                        <option value="Honda">Honda</option>
                        <option value="BMW">BMW</option>
                        <option value="Audi">Audi</option>
                        <option value="Toyota">Toyota</option>
                        <option value="Nissan">Nissan</option>
                    </select>


                    <label htmlFor="Model-select">Choose a model</label>
                    <select id="model1"
                        className='select'
                        onChange={(event) => this.handleChangeModel(event)}
                    >
                        <option value="">--Model--</option>
                        {this.state.models1.map((m, i) =>
                            <option key={i} value={m.value}>{m.display}</option>)}
                    </select>


                    <label htmlFor="From Year-select">From Year</label>
                    <select id="fromyear1"
                        className='select'
                        onChange={(event) => this.handleChangeFromYear(event)}>
                        <option value="">--From Year--</option>
                        <option value="2009">2009</option>
                        <option value="2010">2010</option>
                        <option value="2011">2011</option>
                        <option value="2012">2012</option>
                        <option value="2013">2013</option>
                        <option value="2014">2014</option>
                        <option value="2015">2015</option>
                        <option value="2016">2016</option>
                        <option value="2017">2017</option>
                        <option value="2018">2018</option>
                        <option value="2019">2019</option>
                    </select>


                    <label htmlFor="To Year-select">To Year</label>
                    <select id="toyear1"
                        className='select'
                        onChange={(event) => this.handleChangeToYear(event)}>
                        <option value="">--To Year--</option>
                        <option value="2009">2009</option>
                        <option value="2010">2010</option>
                        <option value="2011">2011</option>
                        <option value="2012">2012</option>
                        <option value="2013">2013</option>
                        <option value="2014">2014</option>
                        <option value="2015">2015</option>
                        <option value="2016">2016</option>
                        <option value="2017">2017</option>
                        <option value="2018">2018</option>
                        <option value="2019">2019</option>
                    </select>


                    <label htmlFor="zip">Metro Area</label>
                    <select id="zip1"
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
                </div>
                {/* <br /> */}



                <div className='compare'>

                    <div> 2nd choice</div>
                    <label htmlFor="Car-select">Choose a car</label>

                    <select id="make2"
                        className='select'
                        onChange={(event) => this.handleChange2(event)}
                        onInput={(event) => this.handleChangeMake(event)} >
                        <option value="">--Make--</option>
                        <option value="Honda">Honda</option>
                        <option value="BMW">BMW</option>
                        <option value="Audi">Audi</option>
                        <option value="Toyota">Toyota</option>
                        <option value="Nissan">Nissan</option>
                    </select>

                    <label htmlFor="Model-select">Choose a model</label>
                    <select id="model2"
                        className='select'
                        onChange={(event) => this.handleChangeModel(event)}>
                        <option value="">--Model--</option>
                        {this.state.models2.map((m, i) =>
                            <option key={i} value={m.value}>{m.display}</option>)}
                    </select>



                    <label htmlFor="From Year-select">From Year</label>
                    <select id="fromyear2"
                        className='select'
                        onChange={(event) => this.handleChangeFromYear(event)}>
                        <option value="">--From Year--</option>
                        <option value="2009">2009</option>
                        <option value="2010">2010</option>
                        <option value="2011">2011</option>
                        <option value="2012">2012</option>
                        <option value="2013">2013</option>
                        <option value="2014">2014</option>
                        <option value="2015">2015</option>
                        <option value="2016">2016</option>
                        <option value="2017">2017</option>
                        <option value="2018">2018</option>
                        <option value="2019">2019</option>
                    </select>


                    <label htmlFor="To Year-select">To Year</label>
                    <select id="toyear2"
                        className='select'
                        onChange={(event) => this.handleChangeToYear(event)}>
                        <option value="">--To Year--</option>
                        <option value="2009">2009</option>
                        <option value="2010">2010</option>
                        <option value="2011">2011</option>
                        <option value="2012">2012</option>
                        <option value="2013">2013</option>
                        <option value="2014">2014</option>
                        <option value="2015">2015</option>
                        <option value="2016">2016</option>
                        <option value="2017">2017</option>
                        <option value="2018">2018</option>
                        <option value="2019">2019</option>
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
                </div>
                
                <p><input type="submit" 
                            value="Submit" 
                            onClick={(event) => this.handleSubmit(event)} 
                            className='myButton'/></p>
            </form>
        )
    }

}



export default Compareform