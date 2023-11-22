import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-my-inner',
  templateUrl: './my-inner.component.html',
  styleUrls: ['./my-inner.component.css']
})

export class MyInnerComponent {
  @Input() innerTotal: number = 5;
  @Output() updateOuterTotal: EventEmitter<number> = new EventEmitter<number>();

  increaseByTen(): void {
    this.innerTotal++;
    if (this.innerTotal > 10) {
      this.innerTotal = 5;
      this.updateOuterTotal.emit(10);
    }
  }

  decreaseByTen(): void {
    this.innerTotal--;
    if (this.innerTotal < -10) {
      this.innerTotal = 5;
      this.updateOuterTotal.emit(-10);
    }
  }
}
