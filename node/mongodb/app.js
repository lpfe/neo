const express = require('express');
const morgan = require('morgan');
const fs = require('fs');
const path = require('path');
const mongoClient = require('mongodb').MongoClient;

const app = express();
app.set('port', process.env.Port || 8000);
app.use(morgan('dev'));

var db;
var databaseUrl = 'mongodb://192.168.1.43:27017';

app.get('/', async (req, res) => {
    res.send('Webl Server Started~!!')
})

app.get('/things', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, client) {
        if (err != null) {
            res.json({'count' : 0})
        } else {
            db = client.db('test');
            db.connection('things').find().toArray(function (err, result) {
                if (err) throw err
                    console.log('result : ');
                    console.log(result);
                    res.json(JSON.stringify(result));
            })
        }
    })
})

app.get('/things', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, client) {
        if (err != null) {
            res.json({'count' : 0})
        } else {
            db = client.db('test');
            db.connection('emp').find().toArray(function (err, result) {
                if (err) throw err
                    console.log('result : ');
                    console.log(result);
                    res.json(JSON.stringify(result));
            })
        }
    })
})


app.get('/things', (req, res) => {
    mongoClient.connect(databaseUrl, function (err, client) {
        if (err != null) {
            res.json({'count' : 0})
        } else {
            db = client.db('test');
            db.connection('primer').find().toArray(function (err, result) {
                if (err) throw err
                    console.log('result : ');
                    console.log(result);
                    res.json(JSON.stringify(result));
            })
        }
    })
})



app.listen(app.get('port'), function () {
    console.log("Server is Started~!!" + app.get('port'));
});