import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TicketCounter } from './ticket-counter';

describe('TicketCounter', () => {
  let component: TicketCounter;
  let fixture: ComponentFixture<TicketCounter>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TicketCounter]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TicketCounter);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
