const express = require('express');
const jwtDecode = require('jwt-decode');
const { readFileSync } = require("fs");
const cookieParser = require('cookie-parser');
const jsonwebtoken = require('jsonwebtoken');
const path = require('path');

const serverPort = 2489;

let firewall = readFileSync('firewall.txt');

let initialState = {
    isUserRegistered: false,
};

const baseToken = jsonwebtoken.sign(initialState, firewall);
const successResponse = JSON.stringify({ message: 0 });
const errorResponse = JSON.stringify({ message: 1 });
const ctfResponse = JSON.stringify({ message: "BUETCTF{P4ul_r3vs3ngin3s_br0k3_Hm@c_syst3m_fl4g_23cr7y}" });

const serverApp = express();
const staticFilesPath = path.join(__dirname, 'public');
serverApp.use(express.static(staticFilesPath));
serverApp.use(cookieParser());

serverApp.get('/validate-token', (request, response) => {
    let result = successResponse;

    if (request.cookies.token) {
        try {
            if (jsonwebtoken.verify(request.cookies.token, firewall)) {
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