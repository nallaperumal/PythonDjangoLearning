import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { MovieItem } from './movie-item';

@Injectable({
  providedIn: 'root',
})
export class MovieService {
  apiUrl_for_top_3_movies = 'http://localhost:8000/api/movies/top_3_movies/';

  constructor(private http: HttpClient) { }

  deleteMovie(id: number): Observable<any> {
    return this.http.delete(`http://localhost:8000/api/movies/${id}/`);
  }

  getTop3Movies(): Observable<MovieItem[]> {
    const movies = this.http.get<MovieItem[]>(this.apiUrl_for_top_3_movies);
    return movies;
  }

  getAllMovies(): Observable<MovieItem[]> {
    const movies = this.http.get<MovieItem[]>("http://localhost:8000/api/movies/")
    return movies;
  }

  saveMovie(movie: MovieItem): Observable<MovieItem> {
    return this.http.post<MovieItem>('http://localhost:8000/api/movies/', movie);
  }
}
