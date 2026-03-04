import { Component, signal } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { LoginForm } from './login-form/login-form';
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, RouterLink, LoginForm],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('movies-app');
}
