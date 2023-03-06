function middleware(req, res, next) {
  if(req.method !== 'POST') {
    return res.status(400).send('Invalid request method');
  }
  const email = req.body.email;
  const { createClient } = require('@supabase/supabase-js');
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseKey = process.env.SUPABASE_KEY;
  const supabase = createClient(supabaseUrl, supabaseKey);
  supabase
    .from('emails')
    .insert([{ email }])
    .then(() => {
      next();
    })
    .catch((error) => {
      return res.status(500).send(error.message);
    });
}