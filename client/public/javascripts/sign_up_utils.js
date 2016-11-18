function is_signup_valid(form) {
  // validate first name and last name
  let name_patt = new RegExp('[a-zA-Záéíóúñ]+');
  if (!name_patt.test(form['first_name'].value)) {
    form['first_name'].focus();
    return false;
  }
  console.log('first_name validated');
  if (!name_patt.test(form['last_name'].value)) {
    form['last_name'].focus();
    return false;
  }
  console.log('last_name validated');

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

  // validate age
  let age_patt = new RegExp('[1-9]+');
  if (!age_patt.test(form['age'].value)) {
    form['age'].focus();
    return false;
  }
  console.log('age validated');

  return true;
}
