import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Movie } from './movie';
//ng generate service fetchMovies

@Injectable({
  providedIn: 'root',
})
export class FetchMovies {

  apiURL_for_top_3 = 'http://127.0.0.1:8000/api/movies/top_3_movies/';
  apiUR_for_good_movies = 'http://127.0.0.1:8000/api/movies/only_good_movies/';

  constructor(private http: HttpClient) { }

  //to get top3 movies
  getTop3Movies(): Observable<Movie[]> {
    const movies = this.http.get<Movie[]>(this.apiURL_for_top_3);
    return movies;
  }

  getGoodMovies(): Observable<Movie[]> {
    const movies = this.http.get<Movie[]>(this.apiUR_for_good_movies);
    return movies;
  }
  
}
