# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Championmastery(models.Model):
    summonerid = models.ForeignKey('Summoners', models.DO_NOTHING, db_column='summonerId')  # Field name made lowercase.
    championid = models.ForeignKey('Champions', models.DO_NOTHING, db_column='championId')  # Field name made lowercase.
    championlevel = models.IntegerField(db_column='championLevel', blank=True, null=True)  # Field name made lowercase.
    championpoints = models.IntegerField(db_column='championPoints', blank=True, null=True)  # Field name made lowercase.
    championpointssincelastlevel = models.DecimalField(db_column='championPointsSinceLastLevel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    championpointsuntilnextlevel = models.DecimalField(db_column='championPointsUntilNextLevel', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    chestgranted = models.BooleanField(db_column='chestGranted', blank=True, null=True)  # Field name made lowercase.
    tokensearned = models.IntegerField(db_column='tokensEarned', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'championMastery'


class Champions(models.Model):
    championid = models.IntegerField(db_column='championId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    blurb = models.CharField(max_length=1000, blank=True, null=True)
    info_attack = models.FloatField(db_column='info_attack', blank=True, null=True)
    info_defense = models.FloatField(db_column='info_defense', blank=True, null=True)
    info_magic = models.FloatField(db_column='info_magic', blank=True, null=True)
    info_difficulty = models.FloatField(db_column='info_difficulty', blank=True, null=True)
    tag1 = models.CharField(max_length=25, blank=True, null=True)
    tag2 = models.CharField(max_length=25, blank=True, null=True)
    partype = models.CharField(max_length=25, blank=True, null=True)
    stats_hp = models.FloatField(db_column='stats_hp', blank=True, null=True)
    stats_hpperlevel = models.FloatField(db_column='stats_hpperlevel', blank=True, null=True)
    stats_mp = models.FloatField(db_column='stats_mp', blank=True, null=True)
    stats_mpperlevel = models.FloatField(db_column='stats_mpperlevel', blank=True, null=True)
    stats_movespeed = models.FloatField(db_column='stats_movespeed', blank=True, null=True)
    stats_armor = models.FloatField(db_column='stats_armor', blank=True, null=True)
    stats_armorperlevel = models.FloatField(db_column='stats_armorperlevel', blank=True, null=True)
    stats_spellblock = models.FloatField(db_column='stats_spellblock', blank=True, null=True)
    stats_spellblockperlevel = models.FloatField(db_column='stats_spellblockperlevel', blank=True, null=True)
    stats_attackrange = models.FloatField(db_column='stats_attackrange', blank=True, null=True)
    stats_hpregen = models.FloatField(db_column='stats_hpregen', blank=True, null=True)
    stats_hpregenperlevel = models.FloatField(db_column='stats_hpregenperlevel', blank=True, null=True)
    stats_mpregen = models.FloatField(db_column='stats_mpregen', blank=True, null=True)
    stats_mpregenperlevel = models.FloatField(db_column='stats_mpregenperlevel', blank=True, null=True)
    stats_crit = models.FloatField(db_column='stats_crit', blank=True, null=True)
    stats_critperlevel = models.FloatField(db_column='stats_critperlevel', blank=True, null=True)
    stats_attackdamage = models.FloatField(db_column='stats_attackdamage', blank=True, null=True)
    stats_attackdamageperlevel = models.FloatField(db_column='stats_attackdamageperlevel', blank=True, null=True)
    stats_attackspeedperlevel = models.FloatField(db_column='stats_attackspeedperlevel', blank=True, null=True)
    stats_attackspeed = models.FloatField(db_column='stats_attackspeed', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'champions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Items(models.Model):
    itemid = models.IntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    cost_base = models.FloatField(blank=True, null=True)
    cost_purchaseable = models.BooleanField(blank=True, null=True)
    cost_total = models.FloatField(blank=True, null=True)
    cost_sell = models.FloatField(blank=True, null=True)
    is_rune = models.BooleanField(blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    colloq = models.CharField(max_length=100, blank=True, null=True)
    plaintext = models.CharField(max_length=100, blank=True, null=True)
    consumed = models.BooleanField(blank=True, null=True)
    stacks = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    consumeonfull = models.BooleanField(blank=True, null=True)
    _from = models.CharField(max_length=1000, blank=True, null=True)
    _into = models.CharField(max_length=1000, blank=True, null=True)
    specialrecipe = models.FloatField(blank=True, null=True)
    instore = models.BooleanField(blank=True, null=True)
    hidefromall = models.BooleanField(blank=True, null=True)
    requiredchampion = models.CharField(max_length=100, blank=True, null=True)
    requireddaily = models.CharField(max_length=100, blank=True, null=True)
    flathppoolmod = models.FloatField(blank=True, null=True)
    flatmppoolmod = models.FloatField(blank=True, null=True)
    flathpregenmod = models.FloatField(blank=True, null=True)
    flatmpregenmod = models.FloatField(blank=True, null=True)
    flatarmormod = models.FloatField(blank=True, null=True)
    flatphysicaldamagemod = models.FloatField(blank=True, null=True)
    flatmagicdamagemod = models.FloatField(blank=True, null=True)
    flatmovementspeedmod = models.FloatField(blank=True, null=True)
    percentmovementspeedmod = models.FloatField(blank=True, null=True)
    percentattackspeedmod = models.FloatField(blank=True, null=True)
    flatcritchancemod = models.FloatField(blank=True, null=True)
    flatspellblockmod = models.FloatField(blank=True, null=True)
    percentlifestealmod = models.FloatField(blank=True, null=True)
    tags = models.CharField(max_length=1000, blank=True, null=True)
    map1 = models.BooleanField(blank=True, null=True)
    map2 = models.BooleanField(blank=True, null=True)
    map3 = models.BooleanField(blank=True, null=True)
    map4 = models.BooleanField(blank=True, null=True)
    effects = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'


class Leagues(models.Model):
    leagueid = models.CharField(db_column='leagueId', primary_key=True, max_length=100)  # Field name made lowercase.
    queuetype = models.CharField(db_column='queueType', max_length=100)  # Field name made lowercase.
    tier = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    summonerid = models.ForeignKey('Summoners', models.DO_NOTHING, db_column='summonerId')  # Field name made lowercase.
    summonername = models.CharField(db_column='summonerName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    leaguepoints = models.IntegerField(db_column='leaguePoints', blank=True, null=True)  # Field name made lowercase.
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    veteran = models.BooleanField(blank=True, null=True)
    inactive = models.BooleanField(blank=True, null=True)
    freshblood = models.BooleanField(db_column='freshBlood', blank=True, null=True)  # Field name made lowercase.
    hotstreak = models.BooleanField(db_column='hotStreak', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'leagues'


class Maps(models.Model):
    mapid = models.IntegerField(primary_key=True)
    mapname = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'maps'


class Matchparticipants(models.Model):
    matchid = models.ForeignKey('Matches', models.DO_NOTHING, db_column='matchId')  # Field name made lowercase.
    summonerid = models.CharField(db_column='summonerId', max_length=100, blank=True, null=True)  # Field name made lowercase.
    assists = models.IntegerField(blank=True, null=True)
    baronkills = models.IntegerField(db_column='baronKills', blank=True, null=True)  # Field name made lowercase.
    bountylevel = models.IntegerField(db_column='bountyLevel', blank=True, null=True)  # Field name made lowercase.
    champexperience = models.IntegerField(db_column='champExperience', blank=True, null=True)  # Field name made lowercase.
    champlevel = models.IntegerField(db_column='champLevel', blank=True, null=True)  # Field name made lowercase.
    championid = models.ForeignKey(Champions, models.DO_NOTHING, db_column='championId', blank=True, null=True)  # Field name made lowercase.
    championname = models.CharField(db_column='championName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    damagedealttobuildings = models.IntegerField(db_column='damageDealtToBuildings', blank=True, null=True)  # Field name made lowercase.
    damagedealttoobjectives = models.IntegerField(db_column='damageDealtToObjectives', blank=True, null=True)  # Field name made lowercase.
    damagedealttoturrets = models.IntegerField(db_column='damageDealtToTurrets', blank=True, null=True)  # Field name made lowercase.
    damageselfmitigated = models.IntegerField(db_column='damageSelfMitigated', blank=True, null=True)  # Field name made lowercase.
    deaths = models.IntegerField(blank=True, null=True)
    detectorwardsplaced = models.IntegerField(db_column='detectorWardsPlaced', blank=True, null=True)  # Field name made lowercase.
    doublekills = models.IntegerField(db_column='doubleKills', blank=True, null=True)  # Field name made lowercase.
    dragonkills = models.IntegerField(db_column='dragonKills', blank=True, null=True)  # Field name made lowercase.
    firstbloodassist = models.BooleanField(db_column='firstBloodAssist', blank=True, null=True)  # Field name made lowercase.
    firstbloodkill = models.BooleanField(db_column='firstBloodKill', blank=True, null=True)  # Field name made lowercase.
    firsttowerassist = models.BooleanField(db_column='firstTowerAssist', blank=True, null=True)  # Field name made lowercase.
    firsttowerkill = models.BooleanField(db_column='firstTowerKill', blank=True, null=True)  # Field name made lowercase.
    gameendedinearlysurrender = models.BooleanField(db_column='gameEndedInEarlySurrender', blank=True, null=True)  # Field name made lowercase.
    gameendedinsurrender = models.BooleanField(db_column='gameEndedInSurrender', blank=True, null=True)  # Field name made lowercase.
    goldearned = models.IntegerField(db_column='goldEarned', blank=True, null=True)  # Field name made lowercase.
    goldspent = models.IntegerField(db_column='goldSpent', blank=True, null=True)  # Field name made lowercase.
    individualposition = models.CharField(db_column='individualPosition', max_length=100, blank=True, null=True)  # Field name made lowercase.
    inhibitorkills = models.IntegerField(db_column='inhibitorKills', blank=True, null=True)  # Field name made lowercase.
    inhibitortakedowns = models.IntegerField(db_column='inhibitorTakedowns', blank=True, null=True)  # Field name made lowercase.
    inhibitorslost = models.IntegerField(db_column='inhibitorsLost', blank=True, null=True)  # Field name made lowercase.
    item0 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item0', blank=True, null=True, related_name='item0')
    item1 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item1', blank=True, null=True, related_name='item1')
    item2 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item2', blank=True, null=True, related_name='item2')
    item3 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item3', blank=True, null=True, related_name='item3')
    item4 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item4', blank=True, null=True, related_name='item4')
    item5 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item5', blank=True, null=True, related_name='item5')
    item6 = models.ForeignKey(Items, models.DO_NOTHING, db_column='item6', blank=True, null=True, related_name='item6')
    itemspurchased = models.IntegerField(db_column='itemsPurchased', blank=True, null=True)  # Field name made lowercase.
    killingsprees = models.IntegerField(db_column='killingSprees', blank=True, null=True)  # Field name made lowercase.
    kills = models.IntegerField(blank=True, null=True)
    lane = models.CharField(max_length=100, blank=True, null=True)
    largestcriticalstrike = models.IntegerField(db_column='largestCriticalStrike', blank=True, null=True)  # Field name made lowercase.
    largestkillingspree = models.IntegerField(db_column='largestKillingSpree', blank=True, null=True)  # Field name made lowercase.
    largestmultikill = models.IntegerField(db_column='largestMultiKill', blank=True, null=True)  # Field name made lowercase.
    longesttimespentliving = models.IntegerField(db_column='longestTimeSpentLiving', blank=True, null=True)  # Field name made lowercase.
    magicdamagedealt = models.IntegerField(db_column='magicDamageDealt', blank=True, null=True)  # Field name made lowercase.
    magicdamagedealttochampions = models.IntegerField(db_column='magicDamageDealtToChampions', blank=True, null=True)  # Field name made lowercase.
    magicdamagetaken = models.IntegerField(db_column='magicDamageTaken', blank=True, null=True)  # Field name made lowercase.
    neutralminionskilled = models.IntegerField(db_column='neutralMinionsKilled', blank=True, null=True)  # Field name made lowercase.
    nexuskills = models.IntegerField(db_column='nexusKills', blank=True, null=True)  # Field name made lowercase.
    nexuslost = models.IntegerField(db_column='nexusLost', blank=True, null=True)  # Field name made lowercase.
    nexustakedowns = models.IntegerField(db_column='nexusTakedowns', blank=True, null=True)  # Field name made lowercase.
    objectivesstolen = models.IntegerField(db_column='objectivesStolen', blank=True, null=True)  # Field name made lowercase.
    objectivesstolenassists = models.IntegerField(db_column='objectivesStolenAssists', blank=True, null=True)  # Field name made lowercase.
    participantid = models.IntegerField(db_column='participantId', blank=True, null=True)  # Field name made lowercase.
    pentakills = models.IntegerField(db_column='pentaKills', blank=True, null=True)  # Field name made lowercase.
    physicaldamagedealt = models.IntegerField(db_column='physicalDamageDealt', blank=True, null=True)  # Field name made lowercase.
    physicaldamagedealttochampions = models.IntegerField(db_column='physicalDamageDealtToChampions', blank=True, null=True)  # Field name made lowercase.
    physicaldamagetaken = models.IntegerField(db_column='physicalDamageTaken', blank=True, null=True)  # Field name made lowercase.
    profileicon = models.IntegerField(db_column='profileIcon', blank=True, null=True)  # Field name made lowercase.
    puuid = models.ForeignKey('Summoners', models.DO_NOTHING, db_column='puuid', blank=True, null=True)
    quadrakills = models.IntegerField(db_column='quadraKills', blank=True, null=True)  # Field name made lowercase.
    riotidname = models.CharField(db_column='riotIdName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    riotidtagline = models.CharField(db_column='riotIdTagLine', max_length=100, blank=True, null=True)  # Field name made lowercase.
    role = models.CharField(max_length=100, blank=True, null=True)
    rune1id = models.ForeignKey('Runes', models.DO_NOTHING, db_column='rune1Id', blank=True, null=True, related_name='rune1id')  # Field name made lowercase.
    rune2id = models.ForeignKey('Runes', models.DO_NOTHING, db_column='rune2Id', blank=True, null=True, related_name='rune2id')  # Field name made lowercase.
    rune3id = models.ForeignKey('Runes', models.DO_NOTHING, db_column='rune3Id', blank=True, null=True, related_name='rune3id')  # Field name made lowercase.
    rune4id = models.ForeignKey('Runes', models.DO_NOTHING, db_column='rune4Id', blank=True, null=True, related_name='rune4id')  # Field name made lowercase.
    rune5id = models.ForeignKey('Runes', models.DO_NOTHING, db_column='rune5Id', blank=True, null=True, related_name='rune5id')  # Field name made lowercase.
    rune6id = models.ForeignKey('Runes', models.DO_NOTHING, db_column='rune6Id', blank=True, null=True, related_name='rune6id')  # Field name made lowercase.
    runestyle1id = models.ForeignKey('Runestyles', models.DO_NOTHING, db_column='runeStyle1Id', blank=True, null=True, related_name='runestyle1id')  # Field name made lowercase.
    runestyle2id = models.ForeignKey('Runestyles', models.DO_NOTHING, db_column='runeStyle2Id', blank=True, null=True, related_name='runestyle2id')  # Field name made lowercase.
    sightwardsboughtingame = models.IntegerField(db_column='sightWardsBoughtInGame', blank=True, null=True)  # Field name made lowercase.
    spell1casts = models.IntegerField(db_column='spell1Casts', blank=True, null=True)  # Field name made lowercase.
    spell2casts = models.IntegerField(db_column='spell2Casts', blank=True, null=True)  # Field name made lowercase.
    spell3casts = models.IntegerField(db_column='spell3Casts', blank=True, null=True)  # Field name made lowercase.
    spell4casts = models.IntegerField(db_column='spell4Casts', blank=True, null=True)  # Field name made lowercase.
    summoner1casts = models.IntegerField(db_column='summoner1Casts', blank=True, null=True)  # Field name made lowercase.
    summoner1id = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='summoner1Id', blank=True, null=True, related_name='summoner1id')  # Field name made lowercase.
    summoner2casts = models.IntegerField(db_column='summoner2Casts', blank=True, null=True)  # Field name made lowercase.
    summoner2id = models.ForeignKey('Summonerspells', models.DO_NOTHING, db_column='summoner2Id', blank=True, null=True, related_name='summoner2id')  # Field name made lowercase.
    summonerlevel = models.IntegerField(db_column='summonerLevel', blank=True, null=True)  # Field name made lowercase.
    summonername = models.CharField(db_column='summonerName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    teamearlysurrendered = models.BooleanField(db_column='teamEarlySurrendered', blank=True, null=True)  # Field name made lowercase.
    teamid = models.IntegerField(db_column='teamId', blank=True, null=True)  # Field name made lowercase.
    teamposition = models.CharField(db_column='teamPosition', max_length=100, blank=True, null=True)  # Field name made lowercase.
    timeccingothers = models.IntegerField(db_column='timeCCingOthers', blank=True, null=True)  # Field name made lowercase.
    timeplayed = models.IntegerField(db_column='timePlayed', blank=True, null=True)  # Field name made lowercase.
    totaldamagedealt = models.IntegerField(db_column='totalDamageDealt', blank=True, null=True)  # Field name made lowercase.
    totaldamagedealttochampions = models.IntegerField(db_column='totalDamageDealtToChampions', blank=True, null=True)  # Field name made lowercase.
    totaldamageshieldedonteammates = models.IntegerField(db_column='totalDamageShieldedOnTeammates', blank=True, null=True)  # Field name made lowercase.
    totaldamagetaken = models.IntegerField(db_column='totalDamageTaken', blank=True, null=True)  # Field name made lowercase.
    totalheal = models.IntegerField(db_column='totalHeal', blank=True, null=True)  # Field name made lowercase.
    totalhealsonteammates = models.IntegerField(db_column='totalHealsOnTeammates', blank=True, null=True)  # Field name made lowercase.
    totalminionskilled = models.IntegerField(db_column='totalMinionsKilled', blank=True, null=True)  # Field name made lowercase.
    totaltimeccdealt = models.IntegerField(db_column='totalTimeCCDealt', blank=True, null=True)  # Field name made lowercase.
    totaltimespentdead = models.IntegerField(db_column='totalTimeSpentDead', blank=True, null=True)  # Field name made lowercase.
    totalunitshealed = models.IntegerField(db_column='totalUnitsHealed', blank=True, null=True)  # Field name made lowercase.
    triplekills = models.IntegerField(db_column='tripleKills', blank=True, null=True)  # Field name made lowercase.
    truedamagedealt = models.IntegerField(db_column='trueDamageDealt', blank=True, null=True)  # Field name made lowercase.
    truedamagedealttochampions = models.IntegerField(db_column='trueDamageDealtToChampions', blank=True, null=True)  # Field name made lowercase.
    truedamagetaken = models.IntegerField(db_column='trueDamageTaken', blank=True, null=True)  # Field name made lowercase.
    turretkills = models.IntegerField(db_column='turretKills', blank=True, null=True)  # Field name made lowercase.
    turrettakedowns = models.IntegerField(db_column='turretTakedowns', blank=True, null=True)  # Field name made lowercase.
    turretslost = models.IntegerField(db_column='turretsLost', blank=True, null=True)  # Field name made lowercase.
    unrealkills = models.IntegerField(db_column='unrealKills', blank=True, null=True)  # Field name made lowercase.
    visionscore = models.IntegerField(db_column='visionScore', blank=True, null=True)  # Field name made lowercase.
    visionwardsboughtingame = models.IntegerField(db_column='visionWardsBoughtInGame', blank=True, null=True)  # Field name made lowercase.
    wardskilled = models.IntegerField(db_column='wardsKilled', blank=True, null=True)  # Field name made lowercase.
    wardsplaced = models.IntegerField(db_column='wardsPlaced', blank=True, null=True)  # Field name made lowercase.
    win = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matchParticipants'


class Queues(models.Model):
    queueid = models.IntegerField(db_column='queueId', primary_key=True)  # Field name made lowercase.
    map = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queues'


class Matches(models.Model):
    matchid = models.CharField(db_column='matchId', primary_key=True, max_length=100)  # Field name made lowercase.
    gamemode = models.CharField(db_column='gameMode', max_length=100)  # Field name made lowercase.
    gameduration = models.IntegerField(db_column='gameDuration')  # Field name made lowercase.
    gamename = models.CharField(db_column='gameName', max_length=100)  # Field name made lowercase.
    gametype = models.CharField(db_column='gameType', max_length=100)  # Field name made lowercase.
    mapid = models.ForeignKey(Maps, models.DO_NOTHING, db_column='mapId')  # Field name made lowercase.
    queueid = models.ForeignKey(Queues, models.DO_NOTHING, db_column='queueId')  # Field name made lowercase.
    platformid = models.CharField(db_column='platformId', max_length=100)  # Field name made lowercase.
    gameversion = models.CharField(db_column='gameVersion', max_length=100)  # Field name made lowercase.
    gamecreation = models.BigIntegerField(db_column='gameCreation')  # Field name made lowercase.
    gameendtimestamp = models.BigIntegerField(db_column='gameEndTimestamp')  # Field name made lowercase.
    gamestarttimestamp = models.BigIntegerField(db_column='gameStartTimestamp')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matches'


class Matchteams(models.Model) :
    matchid = models.ForeignKey(Matches, models.DO_NOTHING, db_column='matchId')  # Field name made lowercase.
    teamid = models.IntegerField(db_column='teamId')  # Field name made lowercase.
    win = models.BooleanField(blank=True, null=True)
    ban1 = models.IntegerField(db_column='ban1', blank=True, null=True)  # Field name made lowercase.
    ban2 = models.IntegerField(db_column='ban2', blank=True, null=True)  # Field name made lowercase.
    ban3 = models.IntegerField(db_column='ban3', blank=True, null=True)  # Field name made lowercase.
    ban4 = models.IntegerField(db_column='ban4', blank=True, null=True)  # Field name made lowercase.
    ban5 = models.IntegerField(db_column='ban5', blank=True, null=True)  # Field name made lowercase.
    firstbaron = models.BooleanField(blank=True, null=True)
    baronkills = models.IntegerField(db_column='baronKills', blank=True, null=True)  # Field name made lowercase.
    firstchampion = models.BooleanField(blank=True, null=True)
    championkills = models.IntegerField(db_column='championKills', blank=True, null=True)  # Field name made lowercase.
    firstdragon = models.BooleanField(blank=True, null=True)
    dragonkills = models.IntegerField(db_column='dragonKills', blank=True, null=True)  # Field name made lowercase.
    firstinhibitor = models.BooleanField(blank=True, null=True)
    inhibitorkills = models.IntegerField(db_column='inhibitorKills', blank=True, null=True)  # Field name made lowercase.
    firstriftherald = models.BooleanField(blank=True, null=True)
    riftheraldkills = models.IntegerField(db_column='riftHeraldKills', blank=True, null=True)  # Field name made lowercase.
    firsttower = models.BooleanField(blank=True, null=True)
    towerkills = models.IntegerField(db_column='towerKills', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'matchteams'


class Runestyles(models.Model):
    styleid = models.IntegerField(db_column='styleId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'runeStyles'


class Runes(models.Model):
    runeid = models.IntegerField(db_column='runeId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100)
    style = models.ForeignKey(Runestyles, models.DO_NOTHING, db_column='style')
    shortdescription = models.CharField(db_column='shortDescription', max_length=1000)
    longdescription = models.CharField(db_column='longDescription', max_length=1000)

    class Meta:
        managed = False
        db_table = 'runes'


class Summonerspells(models.Model):
    spellkey = models.IntegerField(db_column='spellKey', primary_key=True)  # Field name made lowercase.
    spellid = models.CharField(db_column='spellId', max_length=100)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    cooldown = models.FloatField(db_column='cooldown', blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'summonerSpells'


class Summoners(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    accountid = models.CharField(db_column='accountId', max_length=100)  # Field name made lowercase.
    puuid = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    profileiconid = models.IntegerField(db_column='profileIconId', blank=True, null=True)  # Field name made lowercase.
    revisiondate = models.DecimalField(db_column='revisionDate', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    summonerlevel = models.IntegerField(db_column='summonerLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'summoners'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128)
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
