const express = require('express');
const crypto = require('crypto');
const bodyParser = require('body-parser');
const rateLimit = require('express-rate-limit');
const path = require('path');

const app = express();
const PORT = 3000;
const SECRET_KEY = "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"; 
const encryptedText = "79,235,211,11,248,78,200,30,66,16,242,243,53,91,199,219,251,226,42,33,139,43,60,233,239,101,47,40,56,231,228,249,53,0,84,12,27,173,96,172,28,132,143,63,43,221,116,198,220,140,119,159,216,143,198,164,212,255,32,52,189,36,217,177,116,198,52,172,111,201,37,138,244,77,93,26,226,237,133,127,251,226,31,53,182,137,170,228,151,226,31,53,94,34,209,131,3,37,198,164,199,219,102,94,220,89,19,253,234,226,31,141,52,90,201,76,84,12,252,125,99,193,17,45,116,198,181,92,162,229,176,246,226,237,52,90,32,75,116,198,228,249,68,180,68,22"
const keyMatrix = [[5, 8], [17, 3]]; 
const mod = 257; 


const limiter = rateLimit({
    windowMs: 60 * 10000, 
    max: 5000, 
    message: "Too many requests, please try again later.",
});

app.use(bodyParser.json());
app.use(limiter);


app.use(express.static(path.join(__dirname, 'public')));


const validOrigins = [ "http://localhost", "http://127.0.0.1"];


app.use((req, res, next) => {
    const origin = req.get('Origin');
    console.log("Received Origin:", origin);  
    if (validOrigins.includes(origin)) {
        res.setHeader('Access-Control-Allow-Origin', origin);
        next();
    } else {
        res.status(403).json({ error: 'Invalid origin' });
    }
});



function modExp(base, exp, mod) {
    let result = 1;
    base = base % mod;
    while (exp > 0) {
        if (exp % 2 === 1) {
            result = (result * base) % mod;
        }
        exp = Math.floor(exp / 2);
        base = (base * base) % mod;
    }
    return result;
}

function modInverse(a, mod) {
    let m0 = mod, t, q;
    let x0 = 0, x1 = 1;
    if (mod === 1) return 0;
    while (a > 1) {
        q = Math.floor(a / mod);
        t = mod;
        mod = a % mod;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if (x1 < 0) x1 += m0;
    return x1;
}

function matrixMultiply(matrix, vector, mod) {
    return [
        (matrix[0][0] * vector[0] + matrix[0][1] * vector[1]) % mod,
        (matrix[1][0] * vector[0] + matrix[1][1] * vector[1]) % mod
    ].map(num => (num + mod) % mod); 
}

function matrixInverse(matrix, mod) {
    const det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod;
    const invDet = modInverse((det + mod) % mod, mod); 
    return [
        [(matrix[1][1] * invDet) % mod, (-matrix[0][1] * invDet + mod) % mod],
        [(-matrix[1][0] * invDet + mod) % mod, (matrix[0][0] * invDet) % mod]
    ];
}

function decrypt(encryptedText, keyMatrix, mod) {
    const encryptedArray = encryptedText.split(",").map(Number);
    const decryptedText = [];
    const inverseMatrix = matrixInverse(keyMatrix, mod);

    for (let i = 0; i < encryptedArray.length; i += 2) {
        const vector = [
            modExp(encryptedArray[i], modInverse(3, mod - 1), mod),
            modExp(encryptedArray[i + 1], modInverse(3, mod - 1), mod)
        ];
        const decryptedVector = matrixMultiply(inverseMatrix, vector, mod);
        decryptedText.push(String.fromCharCode(decryptedVector[0]));
        decryptedText.push(String.fromCharCode(decryptedVector[1]));
    }

    return decryptedText.join("").trim(); 
}

function verifySignature(signature) {
    const message = "1337Haxxor";  
    const hmac = crypto.createHmac('sha256', SECRET_KEY);
    hmac.update(message);  
    const expectedSignature = hmac.digest('hex');
    return expectedSignature === signature;
}



app.post('/decrypt', (req, res) => {
    const { signature } = req.body;

    if (!verifySignature(signature)) {
        return res.status(403).json({ error: 'Invalid request signature' });
    }

    const decrypted = decrypt(encryptedText, keyMatrix, mod);
    res.json({ decrypted });
});


app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});


app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
