import { Component, signal } from '@angular/core';
import { MovieItem } from '../movie-item';
import { MovieService } from '../movie-service';

@Component({
  selector: 'app-movie-comp',
  imports: [],
  templateUrl: './movie-comp.html',
  styleUrl: './movie-comp.css',
})
export class MovieComp {
  movies = signal<MovieItem[]>([]);

  constructor(private movieService: MovieService) {
   this.movieService.getTop3Movies().subscribe(movies => {
      this.movies.set(movies);
      console.log(this.movies());

    });
  }
}
