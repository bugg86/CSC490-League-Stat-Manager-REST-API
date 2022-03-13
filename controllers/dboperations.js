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
        return insertMap.recordsets;
    }
    catch (err) {
        console.log(err);
    }
}

async function getSummoners() {
    try {
        let pool = await sql.connect(config);
        let summoners = await pool.request().query("SELECT * FROM summoners");
        return summoners.recordset;
    }
    catch (error) {
        console.log(error);
    }
}

async function addSummoner(summoner) {
    try {
        let pool = await sql.connect(config);
        let insertSummoner = await pool.request()
        .input('summonerid', sql.NVarChar(100), summoner.summonerid)
        .input('name', sql.NVarChar(100), summoner.name)
        .input('accountid', sql.NVarChar(100), summoner.accountid)
        .input('puuid', sql.NVarChar(100), summoner.puuid)
        .input('profileiconid', sql.Int, summoner.profileiconid)
        .input('revisiondate', sql.Numeric(18,0), summoner.revisiondate)
        .input('summonerlevel', sql.Int, summoner.summonerlevel)
        .execute('Insert_Summoner');
        return insertSummoner.recordsets;
    }
    catch (err) {
        console.log(err);
    }
}

async function getMatches() {
    try {
        let pool = await sql.connect(config);
        let matches = await pool.request().query("SELECT * FROM matches");
        return matches.recordset;
    }
    catch (error) {
        console.log(error);
    }
}

async function addMatch(match) {
    try {
        let pool = await sql.connect(config);
        let insertMatch = await pool.request()
        .input('matchid', sql.NVarChar(100), match.matchid)
        .input('gamemode', sql.NVarChar(100), match.gamemode)
        .input('gameduration', sql.Int, match.gameduration)
        .input('gamename', sql.NVarChar(100), match.gamename)
        .input('gametype', sql.NVarChar(100), match.gametype)
        .input('mapid', sql.Int, match.mapid)
        .input('queueid', sql.Int, match.queueid)
        .input('platformid', sql.NVarChar(100), match.platformid)
        .input('gameversion', sql.NVarChar(100), match.gameversion)
        .input('gamecreation', sql.BigInt, match.gamecreation)
        .input('gameendtimestamp', sql.BigInt, match.gameendtimestamp)
        .input('gamestarttimestamp', sql.BigInt, match.gamestarttimestamp)
        .execute('Insert_Matches');
        return insertMatch.recordsets;
    }
    catch (err) {
        console.log(err);
    }
}

module.exports = {
    getMaps : getMaps,
    addMap : addMap,
    getSummoners : getSummoners,
    addSummoner : addSummoner
}