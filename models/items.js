class Item {
    constructor(itemid, name, cost_base, cost_total, cost_sell, cost_purchaseable, isrune, description, colloq, plaintext, consumed, stacks, depth, consumeonfull, _from, _into, specialrecipe, instore, hidefromall, requiredchampion, requiredaily, flathppoolmod, flatmppoolmod, flathpregenmod, flatmpregenmod, flatarmormod, flatphysicaldamagemod, flatmagicdamagemod, flatmovementspeedmod, percentmovespeedmod, percentattackspeedmod, flatcritchancemod, flatspellblockmod, percentlifestealmod, tags, map1, map2, map3, map4, effects) {
        this.itemid = itemid;
        this.name = name;
        this.cost_base = cost_base;
        this.cost_total = cost_total;
        this.cost_sell = cost_sell;
        this.cost_purchaseable = cost_purchaseable;
        this.isrune = isrune;
        this.description = description;
        this.colloq = colloq;
        this.plaintext = plaintext;
        this.consumed = consumed;
        this.stacks = stacks;
        this.depth = depth;
        this.consumeonfull = consumeonfull;
        this._from = _from;
        this._into = _into;
        this.specialrecipe = specialrecipe;
        this.instore = instore;
        this.hidefromall = hidefromall;
        this.requiredchampion = requiredchampion;
        this.requiredaily = requiredaily;
        this.flathppoolmod = flathppoolmod;
        this.flatmppoolmod = flatmppoolmod;
        this.flathpregenmod = flathpregenmod;
        this.flatmpregenmod = flatmpregenmod;
        this.flatarmormod = flatarmormod;
        this.flatphysicaldamagemod = flatphysicaldamagemod;
        this.flatmagicdamagemod = flatmagicdamagemod;
        this.flatmovementspeedmod = flatmovementspeedmod;
        this.percentmovespeedmod = percentmovespeedmod;
        this.percentattackspeedmod = percentattackspeedmod;
        this.flatcritchancemod = flatcritchancemod;
        this.flatspellblockmod = flatspellblockmod;
        this.percentlifestealmod = percentlifestealmod;
        this.tags = tags;
        this.map1 = map1;
        this.map2 = map2;
        this.map3 = map3;
        this.map4 = map4;
        this.effects = effects;
    }
}

module.exports = Item;