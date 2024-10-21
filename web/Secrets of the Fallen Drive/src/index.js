const express = require('express');
const jwtDecode = require('jwt-decode');
const cookieParser = require('cookie-parser');
const jsonwebtoken = require('jsonwebtoken');
const path = require('path');

const serverPort = 2488;

let initialState = {
    isUserRegistered: false,
};

const baseToken = jsonwebtoken.sign(initialState, '', { algorithm: 'none' });
const successResponse = JSON.stringify({ message: 0 });
const errorResponse = JSON.stringify({ message: 1 });
const ctfResponse = JSON.stringify({ message: "BUETCTF{N0x_G34rsh1ft_F4llC0d3_420_1337}" });

const serverApp = express();
const staticFilesPath = path.join(__dirname, 'public');
serverApp.use(express.static(staticFilesPath));
serverApp.use(cookieParser());

serverApp.get('/validate-token', (request, response) => {
    let result = successResponse;

    if (request.cookies.token) {
        try {
            if (jsonwebtoken.verify(request.cookies.token, '', { algorithms: 'none' })) {
                const decodedToken = jsonwebtoken.decode(request.cookies.token);
                if (decodedToken.isUserRegistered === true) {
                    result = ctfResponse;
                }
            }
        } catch (error) {
            result = errorResponse;
        }
    }

    response.setHeader('Content-Type', 'application/json');
    response.cookie('token', baseToken);
    response.send(result);
});
serverApp.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
serverApp.get('/garage', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'garage.html'));
});
serverApp.listen(serverPort, () => {
    console.log(`Server is operational at http://localhost:${serverPort}`);
});