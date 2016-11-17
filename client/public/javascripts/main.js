socket = io.connect('http://localhost:8000', () => {
  console.log('socket connected');
});

socket.on('signup', (data) => console.log(data));

function signup() {
  console.log('CLICK');
  let load = {
    'user': {
      'first_name': 'Sebastian',
      'last_name': 'Verga',
      'username': 'sebasvega95',
      'password': 'pepito123',
      'age': '21',
      'gender': 'M'
    }
  }
  socket.emit('signup', JSON.stringify(load));
}
