import { Routes } from '@angular/router';
import { MovieComp } from './movie-comp/movie-comp';
import { AddMovie } from './add-movie/add-movie';

export const routes: Routes = [
    {path: 'movie-comp', component: MovieComp}, // localhost:4200/movie-comp
    {path: 'add-movie', component: AddMovie}, // localhost:4200/add-movie
];
