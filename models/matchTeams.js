class MatchTeam {
    constructor(matchid, win, ban1, ban2, ban3, ban4, ban5, firstbaron, baronkills, firstchampion, championkills, firstdragon, dragonkills, firstinhibitor, inhibitorkills, firstriftherald, riftheraldkills, firsttower, towerkills) {
        this.matchid = matchid;
        this.win = win;
        this.ban1 = ban1;
        this.ban2 = ban2;
        this.ban3 = ban3; 
        this.ban4 = ban4;
        this.ban5 = ban5;
        this.firstbaron = firstbaron;
        this.baronkills = baronkills;
        this.firstchampion = firstchampion;
        this.championkills = championkills;
        this.firstdragon = firstdragon;
        this.dragonkills = dragonkills;
        this.firstinhibitor = firstinhibitor;
        this.inhibitorkills = inhibitorkills;
        this.firstriftherald = firstriftherald;
        this.riftheraldkills = riftheraldkills;
        this.firsttower = firsttower;
        this.towerkills = towerkills;
    }
}

module.exports = MatchTeam;