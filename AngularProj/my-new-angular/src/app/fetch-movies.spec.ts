import { TestBed } from '@angular/core/testing';

import { FetchMovies } from './fetch-movies';

describe('FetchMovies', () => {
  let service: FetchMovies;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FetchMovies);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
