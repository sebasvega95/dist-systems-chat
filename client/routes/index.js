const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('signup', { title: 'Sign Up and start chatting' });
});

router.get('/signup', (req, res) => {
  res.render('signup', { title: 'Sign Up and start chatting' });
});

router.get('/login', (req, res) => {
  res.render('login', { title: 'Login'});
});
module.exports = router;
