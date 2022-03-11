var config = require('../config/dbConnection.js');
const sql = require("mssql");

async function getMaps () {
    try {
        let pool = await sql.connect(config);
        let maps = await pool.request().query("SELECT * FROM maps");
        return maps.recordset;
    } 
    catch (error) {
        console.log(error);
    }
}

async function addMap (map) {
    try {
        let pool = await sql.connect(config);
        let insertMap = await pool.request()
        .input('mapid', sql.Int, map.mapid)
        .input('mapname', sql.NVarChar(100), map.mapname)
        .execute('Insert_Map');
    }
    catch (err) {
        console.log(err);
    }
}

module.exports = {
    getMaps : getMaps,
    addMap : addMap
}