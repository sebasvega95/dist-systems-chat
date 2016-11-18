socket = io.connect('http://localhost:8000', () => {
  console.log('socket connected');
});

socket.on('signup', (data) => console.log(data));

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
    }
    console.log("Data to signup: ", load);
    socket.emit('signup', JSON.stringify(load));
    window.location.replace("http://localhost:3000/login");
  }
}
