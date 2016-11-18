const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.redirect('/signup')
});

router.get('/signup', (req, res) => {
  res.render('signup', { title: 'Sign Up and start chatting' });
});

router.get('/login', (req, res) => {
  res.render('login', { title: 'Login' });
});

router.get('/chat', (req, res) => {
  res.render('chat', { title: 'Chat' });
});

module.exports = router;
