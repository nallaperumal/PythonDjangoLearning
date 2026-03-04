import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MovieService } from '../movie-service';

@Component({
  selector: 'app-login-form',
  imports: [ReactiveFormsModule],
  templateUrl: './login-form.html',
  styleUrl: './login-form.css',
})
export class LoginForm {
  private fb = inject(FormBuilder);
  constructor(private movieService: MovieService){}

  loginForm = this.fb.group({
    usr: ['', Validators.required],
    pwd: ['', Validators.required],
  }, { nonNullable: true });

  onSubmit() {
    const payload = this.loginForm.value;
    console.log(payload);
    const {usr, pwd} = this.loginForm.getRawValue();
    this.movieService.performLogin(usr, pwd);
  }
}
