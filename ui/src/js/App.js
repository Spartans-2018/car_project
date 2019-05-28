import React from 'react';
import Header from './components/Header'
import Footer from './components/Footer'
import Budget from './components/Budget'
import CarType from './components/CarType'
import Mileage from './components/Mileage'
import Area from './components/Area'
import Bs from './components/Bs'
import Budgetform from './components/Budgetform'
import Service from './service';
// import Child from './components/Child'
import Compareform from './components/Compareform'
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import "react-tabs/style/react-tabs.css";
let service = new Service();
let budget = new Budget();
let carType = new CarType();
let mileage = new Mileage();
let area = new Area();


import Graph from './components/Graph';
import NewCarForm from './components/Newcarform';
import NewCarGraph from './components/Newcargraph'
import graphStateConst from './components/graphstate'




class App extends React.Component {

    constructor() {
        super();
        this.state = {
            cars: [],
            // graphState: {},
            displayState: {
            },
            otherState: {
            }
        };

        // Bind handle submit to this component.
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleGraphSubmit = this.handleGraphSubmit.bind(this);
        this.handleNewCarSubmit = this.handleNewCarSubmit.bind(this);
        

    }

    handleSubmit(data) {
        console.log(`In App.js component, data retrived ${data}`);

        // this.setState({ cars: data.listings });
        this.setState({ cars: data});
    }

    handleGraphSubmit(data1) {
        console.log(`graph data ${data1}`)

        this.setState({
            graphState: {
                data: [
                    {
                        y: data1.x1, x: data1.y1,
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: { color: 'blue' },
                        name: data1.makeModel1
                    },
                    {
                        y: data1.x2, x: data1.y2,
                        type: 'scatter',
                        mode: 'lines+markers',
                        marker: { color: 'orange' },
                        name: data1.makeModel2
                    }],
                frames: [],
                config: {},

            },
        })
    }




    handleNewCarSubmit(data3) {
        console.log(`passing data new car ${data3}`)

        this.setState({
           
            NewCarGraphState: {
                data: [
                    {
                        y: data3.y1, 
                        x: data3.x1,
                        type: 'scatter',
                        mode: 'lines',
                        marker: { color: 'red' },
                        name: data3.make_model,
                        showlegend: true,
                        hoverinfo: 'y'
                    },

                    {
                        type: 'table',
                        columnwidth: [120,120],
                        columnorder: [0,1],
                        header: {
                          values: ['YEARS OLD', 'PRICE $'],
                          align: "center",
                          line: {width: 1, color: 'rgb(50, 50, 50)'},
                          fill: {color: 'grey'},
                          font: {family: "Arial", size: 11, color: "white"}
                        },
                        cells: {
                          values: [graphStateConst.graphState.layout.xaxis.ticktext, data3.y1],
                          align: ["center", "right"],
                          line: {color: "black", width: 1},
                          fill: {color: ['lightgrey', 'white']},
                          font: {family: "Arial", size: 10, color: ["black"]}
                        },
                        xaxis: 'x',
                        yaxis: 'y',
                        domain: {x: [0.8,1], y: [0,1]}
                      }

                ],

                frames: [],
                config: { 'displayModeBar': false, 'displaylogo': false },
                layout: {
                    width: 1200,
                    height: 700,
                    autoSize: true,
                    staticPlot: true,
                    title: {
                        text: 'New ' + data3.make_model + ' projection price depreciation',
                        font: {
                            size: 28,
                            color: 'black',
                            style: 'bold'
                        }
                    },

                    xaxis: {
                        autorange: 'reversed',
                        title: 'Years old',
                        titlefont: {
                            family: 'Arial, sans-serif',
                            size: 18,
                            color: 'lightgrey',

                        },
                        // showgrid: false,
                        // zeroline: false,
                        // showline: false,
                        showticklabels: true,
                        tickangle: 'auto',
                        tickfont: {
                            family: 'Old Standard TT, serif',
                            size: 14,
                            color: 'black'
                        },
                        tick0: 2020,
                        dtick: 1,
                        tickmode: 'array',
                        tickvals: data3.x1,
                        ticktext: ['NEW', '1', '3',
                            '5 ', '7', '10', '20', '30']
                    },

                    yaxis: {
                        title: 'Price',

                        tickformat: '$',
                        titlefont: {
                            family: 'Arial, sans-serif',
                            size: 18,
                            color: 'lightgrey',
                            showgrid: false,
                        },
                        tick0: 0,
                        dtick: 4000,

                        showgrid: false,
                        zeroline: true,
                        showline: false,
                        showticklabels: true,
                        tickangle: 'auto',
                        tickfont: {
                            family: 'Old Standard TT, serif',
                            size: 14,
                            color: 'black'
                        }
                    },

                    images: [
                        {
                            "source": data3.photo,
                            "xref": "paper",
                            "yref": "paper",
                            "x": 0,
                            "y": 0,
                            "sizex": 1,
                            "sizey": 1,
                            "xanchor": "left",
                            "yanchor": "bottom",
                            "opacity": 0.4,
                            "layer": "below",
                            'sizing': 'stretch'
                        },
                    ],
                }

            },
        })
    }



    render() {
        let chart = null;
        if (this.state.graphState) {
            chart = <Graph graphState={this.state.graphState} />
        }

        let chartNewCar = null;
        if (this.state.NewCarGraphState) {
            chartNewCar = <NewCarGraph NewCarGraphState={this.state.NewCarGraphState} />
        }

        return (
            <div>

                <Header />
                <br />
                <br />
                <Tabs forceRenderTabPanel>
                    <TabList>
                        <Tab>Search with budget</Tab>
                        <Tab>Compare Cars</Tab>
                        <Tab>Looking for a new car</Tab>
                    </TabList>

                    <TabPanel>
                        <Budgetform submitHandler={this.handleSubmit} />
                        <br />
                        <div > Recomended Luxury
                            {
                                this.state.cars.slice(0, 2).map((item, index) => {
                                    return <Bs key={index}
                                        href={item.vdp_url}
                                        make={item.build.make}
                                        model={item.build.model}
                                        price={item.price}
                                        miles={item.miles}
                                        year={item.build.year}
                                        picture={item.media.photo_links[0]}
                                        dist={item.dist}
                                        > 
                                    </Bs>
                                })
                            }
                        </div>
                        <div > Recomended Domestic
                            {
                                this.state.cars.slice(2, 4).map((item, index) => {
                                    return <Bs key={index}
                                        href={item.vdp_url}
                                        make={item.build.make}
                                        model={item.build.model}
                                        price={item.price}
                                        miles={item.miles}
                                        year={item.build.year}
                                        picture={item.media.photo_links[0]}
                                        dist={item.dist}
                                        > 
                                    </Bs>
                                })
                            }
                        </div>

                        <div > Recomended Foreign
                            {
                                this.state.cars.slice(4, 6).map((item, index) => {
                                    return <Bs key={index}
                                        href={item.vdp_url}
                                        make={item.build.make}
                                        model={item.build.model}
                                        price={item.price}
                                        miles={item.miles}
                                        year={item.build.year}
                                        picture={item.media.photo_links[0]}
                                        dist={item.dist}
                                        > 
                                    </Bs>
                                })
                            }
                        </div>
                    </TabPanel>

                    <TabPanel>
                        <Compareform submitHandlerGraph={this.handleGraphSubmit} />
                        <br />
                        {chart}
                        <br />
                    </TabPanel>

                    <TabPanel>
                        <NewCarForm newCarSubmit={this.handleNewCarSubmit} />
                        <br />
                        {chartNewCar}
                    </TabPanel>
                </Tabs>

              
                {/* <Footer /> */}

            </div>
        )
    }
}

export default App 