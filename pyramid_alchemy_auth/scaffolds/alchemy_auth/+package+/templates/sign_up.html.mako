<form action="/sign_up" method="POST">
	${registration_form.username.label}
	${registration_form.username}
	<br/>
	${registration_form.first_name.label}
	${registration_form.first_name}
	<br/>
	${registration_form.last_name.label}
	${registration_form.last_name}
	<br/>
	${registration_form.password.label}
	${registration_form.password}
	<br/>
	${registration_form.confirm.label}
	${registration_form.confirm}
	<br/>
  <input type="submit" value="Sign Up"></form>
</form>