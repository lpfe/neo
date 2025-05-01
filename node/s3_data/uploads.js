// const fs = require('fs')
// const env = require('dotenv').config({ path: '../../.env'})

// const AWS = require('aws-sdk')
// const ID = process.env.ID
// const SECRET = process.env.SECRET
// const BUCKET_NAME = 'kibwa-08'
// const MYREGION = 'ap-northeast-3'
// const s3 = new AWS.S3({ accessKeyID : ID, accessAccesskey : SECRET, region : MYREGION})

// const uploadFile = filename => {
//     const fileContent = fs.readFileSync(fileName)
//     const params = {
//         Bucket : BUCKET_NAME,
//         Key : 'axios.png',
//         Body : fileContent,
//     }
//     s3.upload(params, function (err, data) {
//         if (err) {
//             throw err;
//         }
//         console.log(`File uploaded successfully. ${data.location}`)
//     })
// }
// uploadFile('axios.png')





const fs = require('fs')
const env = require('dotenv').config({ path: '../../.env' })

const AWS = require('aws-sdk')
const ID = process.env.ID
const SECRET = process.env.SECRET
const BUCKET_NAME = 'kibwa-08'
const MYREGEION = 'ap-northeast-3'
const s3 = new AWS.S3({ accessKeyId : ID, accessAccessKey : SECRET, region : MYREGEION})

const uploadFile = fileName => {
    const fileContent = fs.readFileSync(fileName)
    const params = {
        Bucket : BUCKET_NAME,
        Key : 'axios.png',
        Body : fileContent,
    }
    s3.upload(params, function (err, data) {
        if (err) {
            throw err;
        }
        console.log(`File uploaded successfully. ${data.Location}`)
    })
}
uploadFile('axios.png')