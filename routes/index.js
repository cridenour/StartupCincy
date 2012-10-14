
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index', { title: 'StartupCincy' });
};

exports.about = function(req, res) {
	res.render('about', {title: 'About Startup Cincy'});
};