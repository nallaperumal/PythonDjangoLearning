import { Routes } from '@angular/router';
import { MovieComp } from './movie-comp/movie-comp';
import { AddMovieComp } from './add-movie-comp/add-movie-comp';

export const routes: Routes = [
    {path: 'movie-comp', component: MovieComp},
    {path: 'add-movie', component: AddMovieComp}
];
