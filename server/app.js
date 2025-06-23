const express = require('express')
const { spawn } = require('node:child_process');
const profiles = require("./db/initialDB.json")

require('dotenv').config()
const mongoose = require('mongoose')

const app = express()
const dburl = process.env.DATABASE_API_KEY;

mongoose.connect(dburl)
    .then((result) => app.listen(3000))
    .catch((err) => console.log(err));

app.get("/", (req,res) => {
    
})

const acquireInstagramListData = (datalist) => {
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

const acquireTiktokListData = (datalist) => {
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
