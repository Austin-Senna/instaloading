class TempDatabase {
    constructor() {
        this.tiktokList = [] 
        this.instagramList = []
        this.databaseList = []
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
        this.databaseList = []

        const len = Math.min(this.tiktokList.length, this.instagramList.length);

        for (let i = 0; i < len; i++) {
            const combinedDict = { ...this.tiktokList[i], ...this.instagramList[i] };
            this.databaseList.push(combinedDict);
        }
    }

    getDatabaseList() {
        return this.databaseList;
    }
}

const temp_database = new TempDatabase()
module.exports = temp_database