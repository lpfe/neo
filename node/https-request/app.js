const https = require('http');

const data = JSON.stringify({ todo : 'Buy the milk'});

const options = {
    hostname: '192.168.1.43',
    port: 8000,
    path: '/data',  // 여기 바꾸면 콘솔 출력값 /node/request/app.js의 문장에 따라 바뀜     // 계속 띄워둘게 아니니까 여기선 node app.js  // /node/reqeust/app.js는 nodemon app.js로 띄워둬야 함
    method: 'GET'
};

const req = https.request(options, res => {
    console.log(`statusCode: ${res.statusCode}`);
    res.on('data', d => {
        process.stdout.write(d);
    })
})

req.on('error', error => {
    console.log(error);
})

req.write(data);
req.end();