var express = require('express');
var hana = require('@sap/hana-client');
 
const app = express();
var conn = hana.createConnection();
 
var conn_params = {
  serverNode  : '53b7bc70-d08b-432b-992d-f09750172772.hana.trial-eu10.hanacloud.ondemand.com:443',
  uid         : 'MAGENTA_VOICE',
  pwd         : '<PW goes here>'
};

app.get('/all', (req, res) => {

conn.connect(conn_params, function(err) {

  conn.exec('SELECT product, amount FROM VOICE_MAPPING', function (err, result) {
    return res.send(result);
  })
});
});

app.get('/product/:productId', (req, res) => {

conn.connect(conn_params, function(err) {

  conn.exec('SELECT product, amount FROM VOICE_MAPPING WHERE product = ?', [req.params.productId], function (err, result) {
    return res.send(result);
  })
});
});

app.listen(8080, () =>
  console.log(`Example app listening on port 8080!`),
);