import React from 'react';

import Image from 'react-image-resizer';


class Bs extends React.Component {
    // constructor(props) {
    //     super(props);
    // }

    render() {


        return (

            <ul className='budgetCar'> 
                         
                <li className='make'>{this.props.make} </li>
                <li className='model' >{this.props.model} </li>
                <li className='price' >${this.props.price}</li>
                <li className='year'>Year: {this.props.year}</li>
                <li className='miles'>{this.props.miles} mi</li>
                <li className='dist'>Distance: {this.props.dist} miles</li>
                <a  onClick={(event) => {
                        event.preventDefault(); window.open(this.props.href);}} >
                    <Image
                        className='img'
                        src={this.props.picture}
                        height={480}
                        width={480} />
                </a>
            </ul>

        )
    }
}

export default Bs