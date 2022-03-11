class Summoner {
    constructor(id, accountid, puuid, name, profileiconid, revisiondate, summonerlevel) {
        this.id = id;
        this.accountid = accountid;
        this.puuid = puuid;
        this.name = name;
        this.profileiconid = profileiconid;
        this.revisiondate = revisiondate;
        this.summonerlevel = summonerlevel;
    }
}

module.exports = Summoner;