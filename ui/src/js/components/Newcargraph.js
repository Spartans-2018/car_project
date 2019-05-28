import React from 'react';
import Plot from 'react-plotly.js';
// const Plot = createPlotlyComponent(Plotly);
import graphStateConst from './graphstate'
/**
 * To render this graph we pass in the state using a prop called "graphState"
 */
class NewCarGraph extends React.Component {
  constructor(props) {
    super(props);
    this.props = props;
  }

  render() {
    return (
      <Plot
        data= {this.props.NewCarGraphState.data}
        // layout= {graphStateConst.graphState.layout}
        layout= {this.props.NewCarGraphState.layout}
        frames={this.props.NewCarGraphState.frames}
        config={this.props.NewCarGraphState.config}
        // images= {this.props.NewCarGraphState.images}
      />
    )
  }
}

export default NewCarGraph