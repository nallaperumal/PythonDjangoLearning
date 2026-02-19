import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddMovieComp } from './add-movie-comp';

describe('AddMovieComp', () => {
  let component: AddMovieComp;
  let fixture: ComponentFixture<AddMovieComp>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddMovieComp]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddMovieComp);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
