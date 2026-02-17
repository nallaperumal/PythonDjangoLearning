import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('my-new-angular');
  movie = 'Avatar';
  lang = 'English';
  imdb = 7.8;
  year_of_release = 2009;
  price = 120;
  num_of_tickets = 1;
  img = 'avatar.jpg';
  computed_price = 120;
  IsDiscounted = false;
  dec_counter() {
    if (this.num_of_tickets > 1)
      this.num_of_tickets--;
    this.computed_price = this.price * this.num_of_tickets;
  }
  inc_counter() {
    this.num_of_tickets++;
    console.log("entered the inc counter:"+this.num_of_tickets);
    
    this.computed_price = this.price * this.num_of_tickets;
    if (this.num_of_tickets > 5) {
      this.computed_price = this.computed_price * 0.9;
      this.IsDiscounted = true;
    }
  }
}
