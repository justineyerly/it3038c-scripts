var http = require("http");

var server = http.createServer(function(req, res){
    res.writeHead(200, {"Content-Type":"text/html"});
    res.end("Hello from Node!");
});

server.listen(3000); 
console.log("Server Listening on port 3000");