
/*
 * GET home page.
 */


exports.index = function(req, res){
  name = false;
  if (req.user) { name = req.user.name; }
  res.render('index', { title: 'StartupCincy', STATIC_URL: '/', name: name });
};

exports.about = function(req, res) {
	res.render('about', {title: 'About Startup Cincy'});
};