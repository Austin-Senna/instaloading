const mongoose = require('mongoose')

const Schema = mongoose.Schema

// const profileSchema = new Schema ({
//     name : {
//         type: String,
//         required: true
//     },
//     TT_username: {
//         type: String,
//         required: true
//     },
//     TT_followers: {
//         type: String,
//         required: true
//     },
//     TT_likes: {
//         type: String,
//         required: true
//     },
//     IG_username: {
//         type: String,
//         required: true
//     },
//     IG_followers: {
//         type: String,
//         required: true
//     }
// })

const profileSchema = new Schema ({
    TT_username: {
        type: String,
        required: true
    },
    TT_followers: {
        type: String,
        required: true
    },
    TT_likes: {
        type: String,
        required: true
    },
})


const Profile = mongoose.model("Profile", profileSchema)
module.exports = Profile