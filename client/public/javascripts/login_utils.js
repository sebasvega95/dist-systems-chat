function is_login_valid(form) {
  // validate first name and last name

  // validate username
  let user_patt = new RegExp('[a-zA-Z][a-zA-Z0-9_-]*');
  if (!user_patt.test(form['username'].value)) {
    form['username'].focus();
    return false;
  }
  console.log('username validated');

  // validate password
  let pass_patt = new RegExp('[a-zA-Z0-9_-]+');
  if (!pass_patt.test(form['password'].value)) {
    form['password'].focus();
    return false;
  }
  console.log('password validated');

  return true;
}
