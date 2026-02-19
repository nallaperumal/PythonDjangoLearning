import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MovieComp } from './movie-comp';

describe('MovieComp', () => {
  let component: MovieComp;
  let fixture: ComponentFixture<MovieComp>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [MovieComp]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MovieComp);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
