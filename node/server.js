var http = require("http");
var fs = require("fs");

http.createServer(function(req, res){

    if(req.url ==="/") {
        fs.readFile("./Public/index.html","UTF-8", function(err, body){
            res.writeHead(200, {"Content-Type":"text/html"});
            res.end(body);
        });
    }
        else{
            res.writeHead(404, {"Content-Type": "text/plain"});
            res.end(`404 File Not Found at ${req.url}`);
        }
}).listen(3000);
console.log("Server Listening on port 3000");