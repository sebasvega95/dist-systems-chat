const socketUrl = 'http://localhost:8000';
const serverUrl = 'http://localhost:3000';

socket = io.connect(socketUrl);

socket.on('connect', () => {
  console.log('Connected');
  if (localStorage.token) {
    let load = {
      'token': localStorage.token
    }
    socket.emit('back', JSON.stringify(load));
    console.log('Logged in');
    if (window.location.toString() !== `${serverUrl}/chat`)
      window.location.replace(`${serverUrl}/chat`);
  }
});

socket.on('signup', (data) => {
  console.log(data);
  data = JSON.parse(data);

  if (data.response) {
    window.location.replace(`${serverUrl}/login`);
  }
  alert(data.message);
});

socket.on('login', (data) => {
  console.log(data);
  data = JSON.parse(data);

  if (data.response) {
    localStorage.token = data.token;
    console.log('Logged in');
    window.location.replace(`${serverUrl}/chat`);
  }
  alert(data.message);
})

function signup() {
  let form = document.getElementById('signup_form');
  if (is_signup_valid(form)) { // function in sign_up_utils.js file
    let load = {
      'user': {
        'first_name': form['first_name'].value,
        'last_name': form['last_name'].value,
        'username': form['username'].value,
        'password': form['password'].value,
        'age': form['age'].value,
        'gender': (form['male'].checked)? "M" : "F"
      }
    };
    console.log('Data to signup:', load);
    socket.emit('signup', JSON.stringify(load));
  }
}

function login() {
  let form = document.getElementById('login_form');
  if (is_login_valid(form)) {
    let load = {
      'user': {
        'username': form['username'].value,
        'password': form['password'].value
      }
    };
    console.log('Data to login:', load);
    socket.emit('login', JSON.stringify(load));
  }
}
