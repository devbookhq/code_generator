const express = require('express');
const app = express();

app.use(express.json());

// Insert the handler here.
// [{HANDLER}]
///////////////////////////

app.listen(8080, () => console.log('Listening on port 8080'));