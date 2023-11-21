import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyInnerComponent } from './my-inner.component';

describe('MyInnerComponent', () => {
  let component: MyInnerComponent;
  let fixture: ComponentFixture<MyInnerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MyInnerComponent]
    });
    fixture = TestBed.createComponent(MyInnerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
