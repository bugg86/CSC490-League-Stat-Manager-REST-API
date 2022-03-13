class ChampionMastery {
    constructor(summonerid, championid, championlevel, championpoints,  championpointssincelastlevel, championpointsuntilnextlevel, chestgranted, tokensEarned) {
        this.summonerid = summonerid;
        this.championid = championid;
        this.championlevel = championlevel;
        this.championpoints = championpoints;
        this.championpointssincelastlevel = championpointssincelastlevel;
        this.championpointsuntilnextlevel = championpointsuntilnextlevel;
        this.chestgranted = chestgranted;
        this.tokensEarned = tokensEarned;
    }
}

module.exports = ChampionMastery;