class TempDatabase {
    constructor() {
        this.tiktokList = [] 
        this.instagramList = []
        this.actualDatabase = []
    }

    updateTiktokList(json) {
        this.tiktokList = json;
    }

    updateInstagramList(json) {
        this.instagramList = json;
    }

    getTiktokList() {
        return this.tiktokList;
    }

    getInstagramList() {
        return this.instagramList;
    }

    mergeList() {
        for (i in range
    }

    getDatabase() {
        return this.ActualDatabase;
    }
}

const temp_database = new TempDatabase()
module.exports = temp_database