import { Component, inject } from '@angular/core';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { MovieService } from '../movie-service';

@Component({
  selector: 'app-add-movie',
  imports: [ReactiveFormsModule],
  templateUrl: './add-movie.html',
  styleUrl: './add-movie.css',
})
export class AddMovie {
  private fb = inject(FormBuilder);

   constructor(private movieService: MovieService) {}

  movieForm = this.fb.group({
    id: [0 , [Validators.required, Validators.min(1)]],
    name: ['', [Validators.required, Validators.minLength(3)]],
    lang: ['', [Validators.required, Validators.minLength(3)]],
    year_of_release: ['', [Validators.required, Validators.min(1900)]],
    imdb_rating: ['', [Validators.required, Validators.min(0), Validators.max(10)]],
    director: ['', [Validators.required, Validators.minLength(3)]],
  }, { nonNullable: true });

  onSubmit() {
    if (this.movieForm.valid) {
      const payload = this.movieForm.value;
      console.log('Form Data:', payload);
       this.movieService.saveMovie(payload).subscribe((data) => {
        console.log(".....", data);
      })
    } else {
      console.log('Form is invalid');
    }
  }
}
