import { Routes } from '@angular/router';
import { TicketCounter } from './ticket-counter/ticket-counter';
import { Popcorn } from './popcorn/popcorn';
import { OtherMovies } from './other-movies/other-movies';

export const routes: Routes = [
    {path: 'ticket-counter', component: TicketCounter}, //http://localhost:4200/ticket-counter
    {path: 'snacks', component: Popcorn},
    {path: 'other-movies',component: OtherMovies},
];
