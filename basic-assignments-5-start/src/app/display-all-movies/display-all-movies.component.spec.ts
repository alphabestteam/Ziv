import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DisplayAllMoviesComponent } from './display-all-movies.component';

describe('DisplayAllMoviesComponent', () => {
  let component: DisplayAllMoviesComponent;
  let fixture: ComponentFixture<DisplayAllMoviesComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DisplayAllMoviesComponent]
    });
    fixture = TestBed.createComponent(DisplayAllMoviesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
