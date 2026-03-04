import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { MovieItem, MovieWithSongItem, LoginToken } from './movie-item';

@Injectable({
  providedIn: 'root',
})
export class MovieService {
  apiUrl_for_top_3_movies = 'http://localhost:8000/api/movies/top_3_movies/';

  constructor(private http: HttpClient) { }

  performLogin(usr: String, pwd: String) {

    const body = {
      "username": usr,
      "password": pwd
    }
     this.http.post<LoginToken>(`http://localhost:8000/api/token/`, body).subscribe({
      next:(res) => {
        const accesstoken = res.access;
        console.log(accesstoken);
        localStorage.setItem('access_token', accesstoken);
      },
      error:(err) => {
        console.log(`error: ${err}`);
      }
     })
    //  subscribe(res =>{
    //     const accesstoken = res.access;
    //     console.log(accesstoken);
    //     localStorage.setItem('access_token', accesstoken);
    // });
  }

  deleteMovie(id: number): Observable<any> {
    return this.http.delete(`http://localhost:8000/api/movies/${id}/`);
  }

  getTop3Movies(): Observable<MovieItem[]> {
    const movies = this.http.get<MovieItem[]>(this.apiUrl_for_top_3_movies);
    return movies;
  }

  getAllMoviesWithSongs(): Observable<MovieWithSongItem[]> {
    const movies = this.http.get<MovieWithSongItem[]>("http://localhost:8000/api/movies/get_movies_with_songs/")
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
