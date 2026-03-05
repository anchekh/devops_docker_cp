import React from 'react';
import ReactDOM from 'react-dom';

function App() {
    return (
        <div style={{textAlign: 'center', marginTop: '50px'}}>
            <h1>Hello, World!</h1>
            <p>From React Application</p>
            <p>Built with multi-stage Docker</p>
            <p>Served by Nginx</p>
        </div>
    );
}

ReactDOM.render(<App />, document.getElementById('root'));
