var db = require('./controllers/dboperations.js');

var map = require('./models/maps.js');
var summoner = require('./models/summoners.js');
var match = require('./models/matches.js');
var league = require('./models/leagues.js');
var championMastery = require('./models/championMasteries.js');

var express = require('express');
var bodyParser = require('body-parser');
var cors = require('cors');
const { response } = require('express');
var app = express();
var router = express.Router();

app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.use(cors());
app.use('/api', router);

var port = process.env.PORT || 8080;
app.listen(port);
console.log('Server is running on port ' + `http://localhost:${port}`);

router.use((request, response, next) => {
    console.log('middleware');
    next();
});

router.route('/maps').get((request, response) => {
    db.getMaps().then((data) => {
        response.json(data);
    });
});

router.route('/maps').post((request, response) => {
    let map = request.body;
    db.addMap(map).then((data) => {
        response.status(201).json(data);
    });
});

router.route('/summoners').get((request, response) => {
    db.getSummoners().then((data) => {
        response.json(data);
    });
});

router.route('/summoners').post((request, response) => {
    let summoner = request.body;
    db.addSummoner(summoner).then((data) => {
        response.status(201).json(data);
    });
});

router.route('/matches').get((request, response) => {
    db.getMatches().then((data) => {
        response.json(data);
    });
});

router.route('/matches').post((request, response) => {
    let match = request.body;
    db.addMatch(match).then((data) => {
        response.status(201).json(data);
    });
});

router.route('/leagues').get((request, response) => {
    db.getLeagues().then((data) => {
        response.json(data);
    });
});

router.route('/leagues').post((request, response) => {
    let league = request.body;
    db.addLeague(league).then((data) => {
        response.status(201).json(data);
    });
});

router.route('/championmasteries').get((request, response) => {
    db.getChampionMasteries().then((data) => {
        response.json(data);
    });
});

router.route('/championmasteries').post((request, response) => {
    let championMastery = request.body;
    db.addChampionMastery(championMastery).then((data) => {
        response.status(201).json(data);
    });
});