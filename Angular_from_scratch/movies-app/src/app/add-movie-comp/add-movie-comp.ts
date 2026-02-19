import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MovieService } from '../movie-service';

@Component({
  selector: 'app-add-movie-comp',
  imports: [ReactiveFormsModule],
  templateUrl: './add-movie-comp.html',
  styleUrl: './add-movie-comp.css',
})
export class AddMovieComp {
  private fb = inject(FormBuilder);

  constructor(private movieService: MovieService) { }

  movieForm = this.fb.group({
    id: ['', Validators.required],
    name: ['', Validators.required],
    lang: ['', Validators.required],
    imdb_rating: ['', [Validators.required, Validators.min(0), Validators.max(10)]],
    year_of_release: ['', Validators.required],
    director: ['', Validators.required]
  },  { nonNullable: true });

  onSubmit() {
    const payload = this.movieForm.value;
    console.log(payload);
    this.movieService.saveMovie(payload).subscribe(res =>{
      console.log(res);
    });
  }
}
