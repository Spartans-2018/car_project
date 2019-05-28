import React from 'react';
import Plot from 'react-plotly.js';
// const Plot = createPlotlyComponent(Plotly);
import graphStateConst from './graphstate'
/**
 * To render this graph we pass in the state using a prop called "graphState"
 */
class Graph extends React.Component {
  constructor(props) {
    super(props);
    this.props = props;
  }

  render() {
    return (
      <Plot
        data={this.props.graphState.data}
        // layout={this.props.graphState.layout}
        layout= {graphStateConst.graphState.layout}
        frames={this.props.graphState.frames}
        config={this.props.graphState.config}
      />
    )
  }
}

export default Graph