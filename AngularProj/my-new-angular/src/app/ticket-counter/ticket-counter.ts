import { Component, input } from '@angular/core';

@Component({
  selector: 'app-ticket-counter',
  imports: [],
  templateUrl: './ticket-counter.html',
  styleUrl: './ticket-counter.css',
})
export class TicketCounter {
  price = input<number>(120);
  discount =  input<number>(0.9);
  computed_price = 120;
  IsDiscounted = false;
  num_of_tickets = 1;
  dec_counter() {
    if (this.num_of_tickets > 1)
      this.num_of_tickets--;
    this.computed_price = this.price() * this.num_of_tickets;
  }
  inc_counter() {
    this.num_of_tickets++;
    console.log("entered the inc counter:" + this.num_of_tickets);

    this.computed_price = this.price() * this.num_of_tickets;
    if (this.num_of_tickets > 5) {
      this.computed_price = this.computed_price * this.discount();
      this.IsDiscounted = true;
    }
  }
}
