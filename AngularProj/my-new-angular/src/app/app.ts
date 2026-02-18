import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TicketCounter } from './ticket-counter/ticket-counter';
import { Popcorn } from './popcorn/popcorn';
import { OtherMovies } from './other-movies/other-movies';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, TicketCounter, Popcorn, OtherMovies],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('my-new-angular');
  movie = 'Avatar';
  lang = 'English';
  imdb = 7.8;
  year_of_release = 2009;

  img = 'avatar.jpg';
// ng generate component <component-name>
// ng generate class MovieItem
// ng generate service <service-name>

}
