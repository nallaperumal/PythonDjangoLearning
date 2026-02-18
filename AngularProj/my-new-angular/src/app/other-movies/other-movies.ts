import { Component } from '@angular/core';
import { Movie } from '../movie';
import { FetchMovies } from '../fetch-movies';
@Component({
  selector: 'app-other-movies',
  imports: [],
  templateUrl: './other-movies.html',
  styleUrl: './other-movies.css',
})
export class OtherMovies {
  movies: Movie[] = [];
  constructor(private fetchMovies: FetchMovies) { }
  ngOnInit(): void {
    console.log('.......other-movies component just initialized');
    // this.fetchMovies.getTop3Movies().subscribe((data) => {
    //   console.log(data);
    //   this.movies = data;
    // })
    this.fetchMovies.getGoodMovies().subscribe((data) => {
      console.log(".....",data);
      this.movies = data;
    })
  }
  ngAfterContentInit(){
    console.log('.......other-movies after content initialized');
  }
  ngAfterViewInit(){
    console.log('.......other-movies after view initialized');
  }
}
