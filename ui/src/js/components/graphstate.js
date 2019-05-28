const graphStateConst = {
    graphState: {
        frames: [],
        config: {},
        layout: {
            width: 800,
            height: 600,
            autoSize: true,
            staticPlot: true,
            title: 'Car graph',
            xaxis: {
                autorange: 'reversed',
                title: 'Year',
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
                tick0: 2019,
                dtick: 1,
                tickmode: 'array',
                tickvals: ['2019', '2018', '2016', '2014', '2012', '2009'],
                ticktext: ['NEW', '1', '3', '5', '7', '10', '20', '30']
            },

            yaxis: {
                title: 'Price USD',
                tickformat: '$',
                titlefont: {
                    family: 'Arial, sans-serif',
                    size: 18,
                    color: 'lightgrey',
                    showgrid: false
                },
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
                    "source": "https://images.plot.ly/language-icons/api-home/python-logo.png",
                    "xref": "paper",
                    "yref": "paper",
                    "x": 0,
                    "y": 0,
                    "sizex": 0.2,
                    "sizey": 0.2,
                    "xanchor": "right",
                    "yanchor": "bottom"
                },
                {
                    "source": 'https://content.homenetiol.com/1280x960/92d50ad157264b64b6fd1ea0939b8d3e.jpg',
                    "xref": "paper",
                    "yref": "paper",
                    "x": 0,
                    "y": 0,
                    "sizex": 1,
                    "sizey": 1,
                    "xanchor": "left",
                    "yanchor": "bottom",
                    "opacity": 0.4,
                    "layer": "below"
                },
            ]


            
            // annotations: [
            //     {

            //         xref: 'x',
            //         yref: 'y',
            //         text: 'max=5',
            //         showarrow: true,
            //         font: {
            //             family: 'Courier New, monospace',
            //             size: 16,
            //             color: '#ffffff'
            //         },
            //         align: 'center',
            //         arrowhead: 2,
            //         arrowsize: 1,
            //         arrowwidth: 2,
            //         arrowcolor: '#636363',
            //         ax: 20,
            //         ay: -30,
            //         bordercolor: '#c7c7c7',
            //         borderwidth: 2,
            //         borderpad: 4,
            //         bgcolor: '#ff7f0e',
            //         opacity: 0.8
            //     }
            // ]


        }
    },
}

export default graphStateConst