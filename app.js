
/**
 * Module dependencies.
 */

var express = require('express')
  , routes = require('./routes')
  , http = require('http')
  , path = require('path')
  , swig = require('swig')
  , cons = require('consolidate')
  , mongodb = require('mongodb');

var app = express();
swig.init({ root: __dirname + '/views', allowErrors: true });
app.engine('html', cons.swig);

app.configure(function(){
  app.set('port', process.env.PORT || 3000);
  app.set('views', __dirname + '/views');
  app.set('view cache', true);
  app.set('view engine', 'html');
  app.use(express.favicon(__dirname + '/public/images/favicon.ico'));
  app.use(express.logger('dev'));
  app.use(express.bodyParser());
  app.use(express.methodOverride());
  app.use(express.cookieParser('ipoohrdtwkmedniwhqbc80ryv6yw4hj98eoiqnc'));
  app.use(express.session({
    secret: 'goredsbengalsetc',
  }));
  app.use(require('less-middleware')({ src: __dirname + '/public' }));
  app.use(express.static(path.join(__dirname, 'public')));
  app.use(app.router);
});

app.configure('development', function(){
  app.use(express.errorHandler());
});

app.get('/', routes.index);
app.get('/about', routes.about);

http.createServer(app).listen(app.get('port'), function(){
  console.log("Express server listening on port " + app.get('port'));
});
