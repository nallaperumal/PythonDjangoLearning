import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Popcorn } from './popcorn';

describe('Popcorn', () => {
  let component: Popcorn;
  let fixture: ComponentFixture<Popcorn>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Popcorn]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Popcorn);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
