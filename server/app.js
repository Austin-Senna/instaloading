const express = require('express')
const { spawn } = require('node:child_process');
const mongoose = require('mongoose')

const app = express()
const dburl = "mongodb+srv://austinsenna:GpD86ojpvfEhKITw@firsttest.g7wvtu6.mongodb.net/blogs";

mongoose.connect(dburl)
    .then((result) => app.listen(3000))
    .catch((err) => console.log(err));


const acquireInstagramData = () => {
    const runInstaLoad = spawn('python', ['./modules/instaload.py'])

    runInstaLoad.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })

    runInstaLoad.stderr.on('data', (data) => {
        console.log(`error: ${data}`)
    })

    runInstaLoad.on('close', (code) => {
        console.log(`child process excited with code ${code}`)
    })
}

const acquireTiktokData = () => {
    const runTiktokLoad = spawn('pytest', ['./modules/tiktokload.py'])

    runTiktokLoad.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`)
    })

    runTiktokLoad.stderr.on('data', (data) => {
        console.log(`error: ${data}`)
    })

    runTiktokLoad.on('close', (code) => {
        console.log(`child process excited with code ${code}`)
    })
}

acquireInstagramData()


// app.get('/', (req,res) => {

// })