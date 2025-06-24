const express = require('express')
const { spawn } = require('node:child_process');
const temp_database = require('./tempdb.js');
require('dotenv').config()
const mongoose = require('mongoose')

const app = express()
const dburl = process.env.DATABASE_API_KEY;


mongoose.connect(dburl)
    .then((result) => app.listen(3000))
    .catch((err) => console.log(err));


app.get("/loadtiktok", (req,res) => loadAllTiktokData(req,res));
app.get("/loadinstagram", (req,res) => loadAllInstagramData(req,res));

const loadAllTiktokData = (req,res) => {
    const runTiktokLoad = spawn('python', ['./modules/alltiktokload.py']);

    let output = '';

    runTiktokLoad.stdout.on('data', (data) => {
        output += data.toString();
    });

    runTiktokLoad.stderr.on('data', (data) => {
        console.log(`error: ${data}`);
    });

    runTiktokLoad.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        if (output.length > 0) {
            try {
                const json = JSON.parse(trimmedOutput);
                temp_database.updateTiktokList(json)
                res.json(temp_database.getTiktokList()); 
            } catch (e) {
                console.log("Failed to parse JSON.", e);
                res.status(500).json({ error: "Failed to parse JSON.", raw: trimmedOutput });
            }
        } else {
            res.status(500).json({ error: "No output from Python script." });
        }
    });
}

const loadAllInstagramData = (req,res) => {
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


