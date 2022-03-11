var db = require('./controllers/dboperations.js');
var map = require('./models/maps.js');
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