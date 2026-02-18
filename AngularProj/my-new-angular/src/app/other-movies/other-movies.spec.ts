import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OtherMovies } from './other-movies';

describe('OtherMovies', () => {
  let component: OtherMovies;
  let fixture: ComponentFixture<OtherMovies>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OtherMovies]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OtherMovies);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
