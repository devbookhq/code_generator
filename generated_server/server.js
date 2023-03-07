const express = require('express');
const app = express();

app.use(express.json());

app.get('/', function(req, res) {
  if (req.method !== 'GET') {
    return res.status(405).send('Method Not Allowed');
  }
  const { email } = req.body;
  if (!email) {
    return res.status(400).send('Email is required');
  }
  const { createClient } = require('@supabase/supabase-js');
  const supabase = createClient(process.env.SUPABASE_URL, process.env.SUPABASE_KEY);
  supabase
    .from('emails')
    .insert([{ email }])
    .then(() => {
      return res.status(200).send('Email inserted successfully');
    })
    .catch((error) => {
      return res.status(500).send(error.message);
    });
});

app.listen(8080, () => console.log('Listening on port 8080'));