
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'StartupCincy', STATIC_URL: 'http://startupcincy.com/static/' });
};

exports.about = function(req, res) {
	res.render('about', {title: 'About Startup Cincy'});
};