/*
 * Calendar functions
 */

var request = require('request')
  , moment = require('moment')
  , everyauth = require('everyauth')
  , mongoose = require('mongoose')
  , async = require('async')
  , apiKey = 'AIzaSyCL7Eka-IMkXB8amWt8r5YtXZQd2tUlwI0'
  , appId = '656554964746.apps.googleusercontent.com'
  , appSecret = '0hdqBv4ylHPV32wt29wuBr4R'
  , token
  , user;

exports.refresh = function(req, res) {

  var User = mongoose.model('User')
  var EventDetail = mongoose.model('EventDetail');

  async.waterfall([
    function(callback) {
      User.findOne({'email': 'chrisridenour@gmail.com'}, callback);
    },
    function(userFound, callback) {
      var now = new Date()
      user = userFound

      if(user) {
        if(user.expires.getTime() < now.getTime()) {
          var refreshObject = {
            client_secret: appSecret,
            grant_type: 'refresh_token',
            refresh_token: user.refreshToken,
            client_id: appId
          }

          request.post({url: 'https://accounts.google.com/o/oauth2/token', 
            form: refreshObject }, 
            callback
          )
        } else {
          callback(null, null, null)
        }
      } else {
        callback(true, null)
      }
    },
    function(resp, body, callback) {
      if(body != null) {
        var data = JSON.parse(body)
        var expiresDate = new Date
        expiresDate.setSeconds(expiresDate.getSeconds() + data.expires_in)
        user.expires = expiresDate
        user.accessToken = data.access_token
        user.save(function(err) {})
      }

      token = user.accessToken

      request({
          url: 'https://www.googleapis.com/calendar/v3/calendars/vo699536a30qdr83eo8c89ud5g%40group.calendar.google.com/events?singleEvents=true&timeMin=' + formatToday() + '&timeMax=' + formatSixMonth(), 
          headers: { Authorization: 'OAuth ' + token }
      }, callback)
    },
    function (resp, body, callback) {
      if(resp.statusCode != 200) {
        console.log(resp.statusCode)
        callback(true, null)
      }
      var data = JSON.parse(body)
      
      async.forEach(
        data.items, 
        function(item, feCallback) {
          var start = moment(item.start.dateTime, "YYYY-MM-DDTHH%3\\Amm%3\\AssZZ")
          var end = moment(item.end.dateTime, "YYYY-MM-DDTHH%3\\Amm%3\\AssZZ")
          

          async.waterfall([
            function(wfCallback) {
              EventDetail.findOne({ 'gCalId': item.id }, wfCallback)
            },
            function(eventFound, wfCallback) {
              if(eventFound) {
                console.log("Updating event.")
                eventFound.title = item.summary
                eventFound.description = item.description
                eventFound.start = start.toDate()
                eventFound.end = end.toDate()
                eventFound.location = item.location
                eventFound.link = ''
                eventFound.save(wfCallback)
              } else {
                console.log("Adding event.")
                var params = {
                  gCalId: item.id,
                  title: item.summary,
                  description: item.description,
                  start: start.toDate(),
                  end: end.toDate(),
                  location: item.location,
                  link: ''
                }

                EventDetail.create(params, wfCallback)
              }
            }
          ], function(err, result) {
            feCallback(null)
          })
        },
        function(err) {
          callback(err, 'Done')
        }
      )

    }
  ], function(err, result) {
    if(err) {
      res.send('Error getting calendar access', 500)
    } else {
      res.send('', 200)
    }
  }
  );
}

exports.list = function(req, res) {

  var EventDetail = mongoose.model('EventDetail');
  var now = moment().toDate()
  var page = req.query.page ? req.query.page : 1
  var eventCount;

  async.waterfall([
    function(callback) {
      EventDetail.count().where('start').gt(now).exec(callback)
    },
    function(count, callback) {
      eventCount = count
      var skipFrom = (page * 10) - 10
      if(skipFrom > count)
        callback(null, [])
      EventDetail.find().where('start').gt(now).sort('start').skip(skipFrom).limit(10).exec(callback)
    }
  ], function(err, events) {
    if(err) {
      res.send('Error accessing database.', 500)
    } else {
      var pages = Math.ceil(eventCount / 10)
      res.render('list-events', { events: events, pages: pages, page: page })
    }
  })
  

}

formatToday = function() {
  var now = moment()
  return now.format("YYYY-MM-DDT00%3\\A00%3\\A00ZZ")
}

formatSixMonth = function() {
  var sixMonth = moment().add('M', 6)
  return sixMonth.format("YYYY-MM-DDT00%3\\A00%3\\A00ZZ")
}