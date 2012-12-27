/*
 * Calendar functions
 */

var request = require('request')
  , moment = require('moment')
  , everyauth = require('everyauth')
  , apiKey = 'AIzaSyCL7Eka-IMkXB8amWt8r5YtXZQd2tUlwI0';

exports.list = function(req, res) {

  if(req.user !== undefined) {
  
    request({url: 'https://www.googleapis.com/calendar/v3/calendars/vo699536a30qdr83eo8c89ud5g%40group.calendar.google.com/events?singleEvents=true&timeMin=' + formatToday() + '&timeMax=' + formatThreeMonth(), headers: { Authorization: 'OAuth ya29.AHES6ZSMGKfbktlt6OOuK3ODH_tGbt9nrPD9VlOmhLuxHyo'}}, function (err, resp, body) {
      if (err) { console.log(err); return; }
      if(resp.statusCode == 200) {
        var data = JSON.parse(body)
        res.render('list-events', { events: data.items })
      } else {
        res.send('Error loading events', 500)
      }
    });

  } else {

    res.send('Access denied.', 404)
    
  }
}

formatToday = function() {
  var now = moment()
  return now.format("YYYY-MM-DDT00%3\\A00%3\\A00-04%3\\A00")
}

formatThreeMonth = function() {
  var oneMonth = moment().add('M', 3)
  return oneMonth.format("YYYY-MM-DDT00%3\\A00%3\\A00-04%3\\A00")
}