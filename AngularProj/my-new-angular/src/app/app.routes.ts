import { Routes } from '@angular/router';
import { OtherMovies } from './other-movies/other-movies';
import { tick } from '@angular/core/testing';
import { TicketCounter } from './ticket-counter/ticket-counter';
import { Popcorn } from './popcorn/popcorn';

export const routes: Routes = [
    {path: 'other-movies', component: OtherMovies}, // localhost:4200/other-movies
    {path: 'ticket-counter', component: TicketCounter}, // localhost:4200/ticket-counter
    {path: 'snacks', component: Popcorn}
];
