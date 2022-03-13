class League {
    constructor(leagueid, queuetype, tier, rank, summonerid, summonername, leaguepoints, wins, losses, veteran, inactive, freshblood, hotstreak) {
        this.leagueid = leagueid;
        this.queuetype = queuetype;
        this.tier = tier;
        this.rank = rank;
        this.summonerid = summonerid;
        this.summonername = summonername;
        this.leaguepoints = leaguepoints;
        this.wins = wins;
        this.losses = losses;
        this.veteran = veteran;
        this.inactive = inactive;
        this.freshblood = freshblood;
        this.hotstreak = hotstreak;
    }
}

module.exports = League;