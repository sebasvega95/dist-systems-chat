socket = io.connect('http://10.253.44.192:8000', () => {
  console.log('socket connected');
});

socket.on('signup', (data) => console.log(data));

function signup() {
  console.log('CLICK');
  socket.emit('signup', `{
    'user': {
      'first_name': 'Sebastian',
      'last_name': 'Verga',
      'username': 'sebasvega95',
      'password': 'pepito123',
      'age': '21',
      'gender': 'M'
      }
    }`
  );

}
