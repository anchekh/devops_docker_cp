const http = require('http');

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.end('<h1>Hello, World!</h1><p>From Node.js Application</p>');
});

const port = 3000;
server.listen(port, () => {
    console.log(`Node.js server running at http://localhost:${port}/`);
});
