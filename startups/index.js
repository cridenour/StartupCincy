/*
 * Startup functions
 */

 var request = require('request')
   , mongoose = require('mongoose')
   , async = require('async')
   , apiKey = '80552cafe149dcf33cc8e2427894a308';


 exports.list = function(req, res) {

 	var startups = []

 	async.waterfall([
 		function(callback) {
 			request({
 				url: 'http://startupgenome.com/api/organizations/city/cincinnati-oh',
 				headers: { 'AUTH-CODE': '80552cafe149dcf33cc8e2427894a308' }
 			}, callback)
 		},
 		function(resp, body, callback) {
 			if(resp.statusCode != 200) {
		        callback(true, null)
		    }
		    var data = JSON.parse(body)

		    for(var s in data.response) {
		    	var startup = data.response[s]
		    	var isStartup = false
		    	startup.categories.forEach(function(c) {
		    		if(c.name == 'Startups')
		    			isStartup = true
		    	})

		    	if(startup.logo_image_url)
		    		startup.logo_image_url = startup.logo_image_url.replace(/\/450\//g, '/')
		    	else
		    		startup.logo_image_url = '/img/placeholder.jpg'

		    	if(isStartup)
		    		startups.push(startup)
		    }
		    callback(null, null)
 		}
 	],
 	function(err, result) {
 		res.render('list-startups', {startups: startups})
 	}
 	)

 }