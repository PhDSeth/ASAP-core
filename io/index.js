import http from 'http'
import socketIO from 'socket.io'
import fetch from "node-fetch";


export default function () {
  this.nuxt.hook('render:before', (renderer) => {
    const server = http.createServer(this.nuxt.renderer.app)
    const io = socketIO(server, {
      cors: {
        origin: "http://localhost:8000",
        methods: ["GET", "POST"]
      }
    });

    // overwrite nuxt.server.listen()
    this.nuxt.server.listen = (port, host) => new Promise(resolve => server.listen(port || 5000, host || 'localhost', resolve)) //porten för browsern
    // close this server on 'close' event
    this.nuxt.hook('close', () => new Promise(server.close))

    // Add socket.io events
    const messages = []
    io.on('connection', (socket) => {
      socket.on('last-messages', function (fn) {
        fn(messages.slice(-50))
        
      })
      socket.on('send-message', function (message) {
        // console.log("hej") //server side
        messages.push(message, "HEJ")
        socket.broadcast.emit('new-message', message)
        const data = fetch('http://localhost:8000/').then(result => result.text())
        .then(data => {
            console.log(data)
        })

      
      })
    })
  })

}