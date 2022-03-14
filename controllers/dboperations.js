var config = require('../config/dbConnection.js');
const sql = require("mssql");

async function getMaps () {
    try {
        let pool = await sql.connect(config);
        let maps = await pool.request().query("SELECT * FROM maps");
        return maps.recordset;
    } 
    catch (err) {
        console.log(err);
        return err;
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
        return err;
    }
}

async function getSummoners() {
    try {
        let pool = await sql.connect(config);
        let summoners = await pool.request().query("SELECT * FROM summoners");
        return summoners.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function addSummoner(summoner) {
    try {
        let pool = await sql.connect(config);
        let insertSummoner = await pool.request()
        .input('id', sql.NVarChar(100), summoner.id)
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
        return err;
    }
}

async function getMatches() {
    try {
        let pool = await sql.connect(config);
        let matches = await pool.request().query("SELECT * FROM matches");
        return matches.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
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
        .execute('Insert_Match');
        return insertMatch.recordsets;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getLeagues() {
    try {
        let pool = await sql.connect(config);
        let leagues = await pool.request().query("SELECT * FROM leagues");
        return leagues.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function addLeague(league) {
    try {
        let pool = await sql.connect(config);
        let insertLeague = await pool.request()
        .input('leagueid', sql.NVarChar(100), league.leagueid)
        .input('queuetype', sql.NVarChar(100), league.queuetype)
        .input('tier', sql.NVarChar(100), league.tier)
        .input('rank', sql.NVarChar(100), league.rank)
        .input('summonerid', sql.NVarChar(100), league.summonerid)
        .input('summonername', sql.NVarChar(100), league.summonername)
        .input('leaguepoints', sql.Int, league.leaguepoints)
        .input('wins', sql.Int, league.wins)
        .input('losses', sql.Int, league.losses)
        .input('veteran', sql.Bit, league.veteran)
        .input('inactive', sql.Bit, league.inactive)
        .input('freshblood', sql.Bit, league.freshblood)
        .input('hotstreak', sql.Bit, league.hotstreak)
        .execute('Insert_League');
        return insertLeague.recordsets;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getChampionMasteries() {
    try {
        let pool = await sql.connect(config);
        let championMasteries = await pool.request().query("SELECT * FROM championMastery");
        return championMasteries.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function addChampionMastery(championMastery) {
    try {
        let pool = await sql.connect(config);
        let insertChampionMastery = await pool.request()
        .input('summonerid', sql.NVarChar(100), championMastery.summonerid)
        .input('championid', sql.Int, championMastery.championid)
        .input('championlevel', sql.Int, championMastery.championlevel)
        .input('championpoints', sql.Int, championMastery.championpoints)
        .input('championpointssincelastlevel', sql.Numeric(18,0), championMastery.championpointsuntilnextlevel)
        .input('championpointsuntilnextlevel', sql.Numeric(18,0), championMastery.lastplayed)
        .input('chestgranted', sql.Bit, championMastery.playerid)
        .input('tokensearned', sql.Int, championMastery.summonerid)
        .execute('Insert_ChampionMastery');
        return insertChampionMastery.recordsets;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getQueues() {
    try {
        let pool = await sql.connect(config);
        let queues = await pool.request().query("SELECT * FROM queues");
        return queues.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getRunes() {
    try {
        let pool = await sql.connect(config);
        let runes = await pool.request().query("SELECT * FROM runes");
        return runes.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getRuneStyles() {
    try {
        let pool = await sql.connect(config);
        let runeStyles = await pool.request().query("SELECT * FROM runeStyles");
        return runeStyles.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getSummonerSpells() {
    try {
        let pool = await sql.connect(config);
        let summonerSpells = await pool.request().query("SELECT * FROM summonerSpells");
        return summonerSpells.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getMatchTeams() {
    try {
        let pool = await sql.connect(config);
        let matchTeams = await pool.request().query("SELECT * FROM matchTeams");
        return matchTeams.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function addMatchTeam(matchTeam) {
    try {
        let pool = await sql.connect(config);
        let insertMatchTeam = await pool.request()
        .input('matchid', sql.NVarChar(100), matchTeam.matchid)
        .input('teamid', sql.Int, matchTeam.teamid)
        .input('win', sql.Bit, matchTeam.win)
        .input('ban1', sql.Int, matchTeam.ban1)
        .input('ban2', sql.Int, matchTeam.ban2)
        .input('ban3', sql.Int, matchTeam.ban3)
        .input('ban4', sql.Int, matchTeam.ban4)
        .input('ban5', sql.Int, matchTeam.ban5)
        .input('firstbaron', sql.Bit, matchTeam.firstbaron)
        .input('baronkills', sql.Int, matchTeam.baronkills)
        .input('firstchampion', sql.Bit, matchTeam.firstchampion)
        .input('championkills', sql.Int, matchTeam.championkills)
        .input('firstdragon', sql.Bit, matchTeam.firstdragon)
        .input('dragonkills', sql.Int, matchTeam.dragonkills)
        .input('firstinhibitor', sql.Bit, matchTeam.firstinhibitor)
        .input('inhibitorkills', sql.Int, matchTeam.inhibitorkills)
        .input('firstriftherald', sql.Bit, matchTeam.firstriftherald)
        .input('riftheraldkills', sql.Int, matchTeam.riftheraldkills)
        .input('firsttower', sql.Bit, matchTeam.firsttower)
        .input('towerkills', sql.Int, matchTeam.towerkills)
        .execute('Insert_MatchTeam');
        return insertMatchTeam.recordsets;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getChampions() {
    try {
        let pool = await sql.connect(config);
        let champions = await pool.request().query("SELECT * FROM champions");
        return champions.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getItems() {
    try {
        let pool = await sql.connect(config);
        let items = await pool.request().query("SELECT * FROM items");
        return items.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function getMatchParticipants() {
    try {
        let pool = await sql.connect(config);
        let matchParticipants = await pool.request().query("SELECT * FROM matchParticipants");
        return matchParticipants.recordset;
    }
    catch (err) {
        console.log(err);
        return err;
    }
}

async function addMatchParticipant() {
    try {
        let pool = await sql.connect(config);
        let insertMatchParticipant = await pool.request()
        .input('matchid', sql.NVarChar(100), matchParticipant.matchid)
        .input('summonerid', sql.NVarChar(100), matchParticipant.summonerid)
        .input('assists', sql.Int, matchParticipant.assists)
        .input('baronkills', sql.Int, matchParticipant.baronkills)
        .input('champexperience', sql.Int, matchParticipant.champexperience)
        .input('champlevel', sql.Int, matchParticipant.champlevel)
        .input('championid', sql.Int, matchParticipant.championid)
        .input('championname', sql.NVarChar(100), matchParticipant.championname)
        .input('damagedealttobuildings', sql.Int, matchParticipant.damagedealttobuildings)
        .input('damagedealttoobjectives', sql.Int, matchParticipant.damagedealttoobjectives)
        .input('damagedealttoturrets', sql.Int, matchParticipant.damagedealttoturrets)
        .input('damageselfmitigated', sql.Int, matchParticipant.damageselfmitigated)
        .input('deaths', sql.Int, matchParticipant.deaths)
        .input('detectorwardsplaced', sql.Int, matchParticipant.detectorwardsplaced)
        .input('doublekills', sql.Int, matchParticipant.doublekills)
        .input('dragonkills', sql.Int, matchParticipant.dragonkills)
        .input('firstbloodassist', sql.Bit, matchParticipant.firstbloodassist)
        .input('firstbloodkill', sql.Bit, matchParticipant.firstbloodkill)
        .input('firsttowerassisted', sql.Bit, matchParticipant.firsttowerassisted)
        .input('firsttowerkill', sql.Bit, matchParticipant.firsttowerkill)
        .input('gameendedinearlysurrender', sql.Bit, matchParticipant.gameendedinearlysurrender)
        .input('gameendedinsurrender', sql.Bit, matchParticipant.gameendedinsurrender)
        .input('goldearned', sql.Int, matchParticipant.goldearned)
        .input('goldspent', sql.Int, matchParticipant.goldspent)
        .input('inhibitorkills', sql.Int, matchParticipant.inhibitorkills)
        .input('inhibitortakedowns', sql.Int, matchParticipant.inhibitortakedowns)
        .input('inhibitorslost', sql.Int, matchParticipant.inhibitorslost)
        .input('item0', sql.Int, matchParticipant.item0)
        .input('item1', sql.Int, matchParticipant.item1)
        .input('item2', sql.Int, matchParticipant.item2)
        .input('item3', sql.Int, matchParticipant.item3)
        .input('item4', sql.Int, matchParticipant.item4)
        .input('item5', sql.Int, matchParticipant.item5)
        .input('item6', sql.Int, matchParticipant.item6)
        .input('itemspurchased', sql.Int, matchParticipant.itemspurchased)
        .input('killingsprees', sql.Int, matchParticipant.killingsprees)
        .input('kills', sql.Int, matchParticipant.kills)
        .input('lane', sql.NVarChar(100), matchParticipant.lane)
        .input('largestcriticalstrike', sql.Int, matchParticipant.largestcriticalstrike)
        .input('largestkillingspree', sql.Int, matchParticipant.largestkillingspree)
        .input('largestmultikill', sql.Int, matchParticipant.largestmultikill)
        .input('longesttimespentliving', sql.Int, matchParticipant.longesttimespentliving)
        .input('magicdamagedealt', sql.Int, matchParticipant.magicdamagedealt)
        .input('magicdamagedealttochampions', sql.Int, matchParticipant.magicdamagedealttochampions)
        .input('magicdamagetaken', sql.Int, matchParticipant.magicdamagetaken)
        .input('neutralminionskilled', sql.Int, matchParticipant.neutralminionskilled)
        .input('nexuskills', sql.Int, matchParticipant.nexuskills)
        .input('nexuslost', sql.Int, matchParticipant.nexuslost)
        .input('nexustakedowns', sql.Int, matchParticipant.nexustakedowns)
        .input('objectivesstolen', sql.Int, matchParticipant.objectivesstolen)
        .input('objectivesstolenassists', sql.Int, matchParticipant.objectivesstolenassists)
        .input('participantid', sql.NVarChar(100), matchParticipant.participantid)
        input('pentakills', sql.Int, matchParticipant.pentakills)
        .input('physicaldamagedealt', sql.Int, matchParticipant.physicaldamagedealt)
        .input('physicaldamagedealttochampions', sql.Int, matchParticipant.physicaldamagedealttochampions)
        .input('physicaldamagetaken', sql.Int, matchParticipant.physicaldamagetaken)
        .input('profileiconid', sql.Int, matchParticipant.profileiconid)
        .input('puuid', sql.NVarChar(100), matchParticipant.puuid)
        .input('quadrakills', sql.Int, matchParticipant.quadrakills)
        .input('riotidname', sql.NVarChar(100), matchParticipant.riotidname)
        .input('riotidtagline', sql.NVarChar(100), matchParticipant.riotidtagline)
        .input('role', sql.NVarChar(100), matchParticipant.role)
        .input('rune1id', sql.Int, matchParticipant.rune1id)
        .input('rune2id', sql.Int, matchParticipant.rune2id)
        .input('rune3id', sql.Int, matchParticipant.rune3id)
        .input('rune4id', sql.Int, matchParticipant.rune4id)
        .input('rune5id', sql.Int, matchParticipant.rune5id)
        .input('rune6id', sql.Int, matchParticipant.rune6id)
        .input('runestyle1id', sql.Int, matchParticipant.runestyle1id)
        .input('runestyle2id', sql.Int, matchParticipant.runestyle2id)
        .input('sightwardsboughtingame', sql.Int, matchParticipant.sightwardsboughtingame)
        .input('spell1casts', sql.Int, matchParticipant.spell1casts)
        .input('spell2casts', sql.Int, matchParticipant.spell2casts)
        .input('spell3casts', sql.Int, matchParticipant.spell3casts)
        .input('spell4casts', sql.Int, matchParticipant.spell4casts)
        .input('summoner1casts', sql.Int, matchParticipant.summoner1casts)
        .input('summoner1id', sql.Int, matchParticipant.summoner1id)
        .input('summoner2casts', sql.Int, matchParticipant.summoner2casts)
        .input('summoner2id', sql.Int, matchParticipant.summoner2id)
        .input('summonerlevel', sql.Int, matchParticipant.summonerlevel)
        .input('summonername', sql.NVarChar(100), matchParticipant.summonername)
        .input('teamearlysurrendered', sql.Bit, matchParticipant.teamearlysurrendered)
        .input('teamid', sql.Int, matchParticipant.teamid)
        .input('teamposition', sql.Int, matchParticipant.teamposition)
        .input('timeccingothers', sql.Int, matchParticipant.timeccingothers)
        .input('timeplayed', sql.Int, matchParticipant.timeplayed)
        .input('totaldamagedealt', sql.Int, matchParticipant.totaldamagedealt)
        .input('totaldamagedealttochampions', sql.Int, matchParticipant.totaldamagedealttochampions)
        .input('totaldamageshieldedonteammates', sql.Int, matchParticipant.totaldamageshieldedonteammates)
        .input('totaldamagetaken', sql.Int, matchParticipant.totaldamagetaken)
        .input('totalheal', sql.Int, matchParticipant.totalheal)
        .input('totalhealsonteammates', sql.Int, matchParticipant.totalhealsonteammates)
        .input('totalminionskilled', sql.Int, matchParticipant.totalminionskilled)
        .input('totaltimeccdealt', sql.Int, matchParticipant.totaltimeccdealt)
        .input('totaltimespentdead', sql.Int, matchParticipant.totaltimespentdead)
        .input('totalunitshealed', sql.Int, matchParticipant.totalunitshealed)
        .input('triplekills', sql.Int, matchParticipant.triplekills)
        .input('truedamagedealt', sql.Int, matchParticipant.truedamagedealt)
        .input('truedamagedealttochampions', sql.Int, matchParticipant.truedamagedealttochampions)
        .input('truedamagetaken', sql.Int, matchParticipant.truedamagetaken)
        .input('turretkills', sql.Int, matchParticipant.turretkills)
        .input('turrettakedowns', sql.Int, matchParticipant.turrettakedowns)
        .input('turretslost', sql.Int, matchParticipant.turretslost)
        .input('unrealkills', sql.Int, matchParticipant.unrealkills)
        .input('visionscore', sql.Int, matchParticipant.visionscore)
        .input('visionwardsboughtingame', sql.Int, matchParticipant.visionwardsboughtingame)
        .input('wardskilled', sql.Int, matchParticipant.wardskilled)
        .input('wardsplaced', sql.Int, matchParticipant.wardsplaced)
        .input('win', sql.Bit, matchParticipant.win)
        .execute('Insert_MatchParticipant')
        return insertMatchParticipant.recordssets;
    }
    catch(err) {
        console.log(err);
        return err;
    }
}

module.exports = {
    getMaps : getMaps,
    addMap : addMap,
    getSummoners : getSummoners,
    addSummoner : addSummoner,
    getMatches : getMatches,
    addMatch : addMatch,
    getLeagues : getLeagues,
    addLeague : addLeague,
    getChampionMasteries : getChampionMasteries,
    addChampionMastery : addChampionMastery,
    getQueues : getQueues,
    getRunes : getRunes,
    getRuneStyles : getRuneStyles,
    getSummonerSpells : getSummonerSpells,
    getMatchTeams : getMatchTeams,
    addMatchTeam : addMatchTeam,
    getChampions : getChampions,
    getItems : getItems,
    getMatchParticipants : getMatchParticipants,
    addMatchParticipant : addMatchParticipant
}