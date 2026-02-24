import { Component, signal } from '@angular/core';
import { MovieItem } from '../movie-item';
import { MovieService } from '../movie-service';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-movie-comp',
  imports: [],
  templateUrl: './movie-comp.html',
  styleUrl: './movie-comp.css',
})
export class MovieComp {
  movies = signal<MovieItem[]>([]);
  IsGrid = signal(true);

  DisplayAsGrid()
  {
    this.IsGrid.set(true);
  }

  DisplayAsList()
  {
    this.IsGrid.set(false);
  }

  deleteMovie(id: number) {
    this.movieService.deleteMovie(id).subscribe(res => {
      console.log("deleted");
      this.fetchMovies();
    }
    )
  }

  gotoAddMoviePage() {
    this.router.navigate(['add-movie']);
  }

  constructor(private movieService: MovieService, private router: Router) {
    console.log("before making the request...");
    this.fetchMovies();
    console.log("after making the request...");
  }

  fetchMovies() {
    this.movieService.getAllMovies().subscribe(
      movies => {
        console.log("received response from server...");
        this.movies.set(movies);
        console.log(this.movies());
      });
  }

}
