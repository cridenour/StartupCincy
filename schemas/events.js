/*
 * Event schemas
 *
 * Event - Meetup or suggested event. Needs approval and is saved to the Google Calendar
 *
 * EventDetail - 1:1 with the calendar. Will also hold additional information such as pictures. 
 * This will be created on approval or for "newly" appeared events on the calendar.
 */

 module.exports = function() {
  var   mongoose = require('mongoose')
      , Schema = mongoose.Schema;

  var EventSchema = new Schema({
        title: String
      , link: String
      , importDetails: { 
            importedDate: { type: Date, default: Date.now }
          , importedFrom: String
          , sourceId: String
        }
      , approvalDetails: { 
            isApproved: Boolean
          , approvedBy: String
          , approvalDate: Date
          , destinationId: String
        }
      , submissionDetails: {
            submittedDate: { type: Date, default: Date.now }
          , submittedBy: String
          , submittedIp: String
        }
      , description: String
      , start: Date
      , end: Date
      , location: String
  });

  mongoose.model('Event', EventSchema);



  var EventDetailSchema = new Schema({
        gCalId: String
      , title: String
      , description: String
      , start: Date
      , end: Date
      , location: String
      , link: String

  });

  mongoose.model('EventDetail', EventDetailSchema);

 }