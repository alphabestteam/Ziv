import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyOuterComponent } from './my-outer.component';

describe('MyOuterComponent', () => {
  let component: MyOuterComponent;
  let fixture: ComponentFixture<MyOuterComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MyOuterComponent]
    });
    fixture = TestBed.createComponent(MyOuterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
