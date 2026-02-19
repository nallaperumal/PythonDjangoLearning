import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { MovieItem } from './movie-item';

@Injectable({
  providedIn: 'root',
})
export class MovieService {
  apiURL_for_top_3 = 'http://127.0.0.1:8000/api/movies/';
  
  constructor(private http: HttpClient) { }

  getTop3Movies(): Observable<MovieItem[]> {
    const movies = this.http.get<MovieItem[]>(this.apiURL_for_top_3);
    return movies;
  }

    
  SaveMovie(movie: MovieItem): Observable<MovieItem> {
    return this.http.post<MovieItem>('http://127.0.0.1:8000/api/movies/', movie);
  }

}
