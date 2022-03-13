class Match {
    constructor(matchid, gamemode, gameduration, gamename, gametype, mapid, queueid, platformid, gameversion, gamecreation, gameendtimestamp, gamestarttimestamp) {
        this.matchid = matchid;
        this.gamemode = gamemode;
        this.gameduration = gameduration;
        this.gamename = gamename;
        this.gametype = gametype;
        this.mapid = mapid;
        this.queueid = queueid;
        this.platformid = platformid;
        this.gameversion = gameversion;
        this.gamecreation = gamecreation;
        this.gameendtimestamp = gameendtimestamp;
        this.gamestarttimestamp = gamestarttimestamp;
    }
}

module.exports = Match;