
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , calendar = require('./calendar')
  , startups = require('./startups')
  , http = require('http')
  , path = require('path')
  , swig = require('swig')
  , cons = require('consolidate')
  , mongoose = require('mongoose')
  , everyauth = require('everyauth')
  , MongoStore = require('connect-mongo')(express);

mongoose.connect('mongodb://localhost/test');

require('./schemas/users.js')();
require('./schemas/events.js')();

User = mongoose.model('User');

// Session store options
session_options = {
    clear_interval: -1, // Do not clear
    mongoose_connection: mongoose.connections[0]
};

var app = express();
swig.init({ root: __dirname + '/views', allowErrors: true });
app.engine('html', cons.swig);

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view cache', false);
  app.set('view engine', 'html');
  app.use(express.favicon(__dirname + '/public/images/favicon.ico'));
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(express.cookieParser('ipoohrdtwkmedniwhqbc80ryv6yw4hj98eoiqnc'));
  app.use(express.session({
    secret: 'goredsbengalsetc',
    store: new MongoStore(session_options)
  }));
  app.use(require('less-middleware')({ src: __dirname + '/public' }));
  app.use(express.static(path.join(__dirname, 'public')));
  app.use(everyauth.middleware());
  app.use(app.routes);
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);
app.get('/about', routes.about);
app.get('/events/refresh', calendar.refresh);
app.get('/events', calendar.list);
app.get('/startups', startups.list);

http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
