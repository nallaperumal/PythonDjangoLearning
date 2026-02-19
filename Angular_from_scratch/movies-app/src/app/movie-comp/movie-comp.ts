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
    console.log("before making the request...");    
    this.movieService.getTop3Movies().subscribe(
      movies => {
        console.log("received response from server...");
        this.movies.set(movies);
        console.log(this.movies());
      });
      console.log("after making the request...");
  }
}
