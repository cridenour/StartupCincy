/*
 * User schemas
 */

 module.exports = function() {
  var   mongoose = require('mongoose')
      , async = require('async')
      , Schema = mongoose.Schema
      , User;

  var UserSchema = new Schema({
        name: String
      , email: String
      , twitter: String
      , picUrl: String
      , accessToken: String
      , expires: Date
      , refreshToken: String
  });

  mongoose.model('User', UserSchema);

  User = mongoose.model('User')

  var everyauth = require('everyauth');

  everyauth.everymodule.findUserById( function (userId, callback) {
    User.findById(userId, callback);
  });

  everyauth.google
    .appId('656554964746.apps.googleusercontent.com')
    .appSecret('0hdqBv4ylHPV32wt29wuBr4R')
    .scope('https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.readonly') // What you want access to
    .handleAuthCallbackError( function (req, res) {
      // If a user denies your app, Google will redirect the user to
      // /auth/google/callback?error=access_denied
      // This configurable route handler defines how you want to respond to
      // that.
      // If you do not configure this, everyauth renders a default fallback
      // view notifying the user that their authentication failed and why.
    })
    .findOrCreateUser( function (session, accessToken, accessTokenExtra, googleUser) {
      var promise = this.Promise();
      
      async.waterfall([
        function(callback) {
          User.findOne({'email': googleUser.email}, callback);
        },
        function(userFound, callback) {
          if (userFound) {
            var expiresDate = new Date;
            expiresDate.setSeconds(expiresDate.getSeconds() + accessTokenExtra.expires_in);

            userFound.picUrl = googleUser.picture
            userFound.accessToken = accessToken
            userFound.refreshToken = accessTokenExtra.refresh_token
            userFound.expires = expiresDate
            userFound.save(function(err) {
              if (err)
                console.log('Error updating user.')
              else
                console.log('Successfully updated user.')
            });

            callback(null, userFound);

          } else {
            // Create the user if it doesn't exist
            var expiresDate = new Date;
            expiresDate.setSeconds(expiresDate.getSeconds() + accessTokenExtra.expires_in);

            var params = {
                name: googleUser.name
              , email: googleUser.email
              , picUrl: googleUser.picture
              , accessToken: accessToken
              , refreshToken: accessTokenExtra.refresh_token
              , expires: expiresDate
            }

            console.log(accessToken);

            User.create(params, callback);
          }
        },
      ], function(err, user) {
          if (err) {
            promise.fail(err)
          }

          promise.fulfill(user)
      });

      return promise;
    })
    .redirectPath('/');
 }