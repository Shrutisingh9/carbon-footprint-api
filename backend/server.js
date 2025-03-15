import express from 'express';
import cors from 'cors';
import { Server } from 'socket.io';
import http from 'http';
import dotenv from 'dotenv';

dotenv.config();
const app = express();
const server = http.createServer(app);
const io = new Server(server, { cors: { origin: '*' } });

app.use(cors());
app.use(express.json());

io.on('connection', (socket) => {
  console.log('A user connected');
  socket.on('send_data', (data) => {
    io.emit('receive_data', data);
  });
});

const PORT = process.env.PORT || 5000;
server.listen(PORT, () => console.log(Server running on port ${PORT}));