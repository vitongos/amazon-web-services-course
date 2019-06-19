var AWS = require('aws-sdk');
var ses = new AWS.SES();
 
var RECEIVER = 'MI CORREO DE YAHOO';
var SENDER = 'Contact Form <MI CORREO DE GMAIL>';

var response = {
 "isBase64Encoded": false,
 "headers": { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
 "statusCode": 200,
 "body": "{\"result\": \"Success.\"}"
 };

exports.handler = function (event, context) {
    console.log('Received event:', event);
    sendEmail(event, function (err, data) {
        context.done(err, response);
    });
};
 
function sendEmail (event, done) {
    var params = {
        Destination: {
            ToAddresses: [
                RECEIVER
            ]
        },
        Message: {
            Body: {
                Text: {
                    Data: 'Hi dude, ' + event.name + ' sent you a message:\n'
                      + event.message + '\n'
                      + 'Reply to: ' + event.email,
                    Charset: 'UTF-8'
                }
            },
            Subject: {
                Data: 'You have received a New Contact Email',
                Charset: 'UTF-8'
            }
        },
        Source: SENDER
    };
    ses.sendEmail(params, done);
}