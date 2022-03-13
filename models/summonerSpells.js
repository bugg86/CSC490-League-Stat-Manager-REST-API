class SummonerSpell {
    constructor(spellkey, spellid, name, cooldown, description) {
        this.spellkey = spellkey;
        this.spellid = spellid;
        this.name = name;
        this.cooldown = cooldown;
        this.description = description;
    }
}

module.exports = SummonerSpell;