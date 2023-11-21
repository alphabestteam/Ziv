// my-inner.component.ts
import { Component, EventEmitter, Output} from '@angular/core';

@Component({
  selector: 'app-my-inner',
  template: `
    <div class="mat-container mat-mt-3">
      <h3>My Inner Works!</h3>
      <button color="primary" (click)="increaseByTen()">+1</button>
      <button color="warn" (click)="decreaseByTen()">-1</button>
      <h3>Inner Total: {{ innerTotal}}</h3>
    </div>
  `,
  styles: [
    `
      .mat-container {
        text-align: center;
        border-style: dotted;
      }

      h3 {
        color: #1976D2;
      }

      button {
        margin: 0 8px;
        color: white;
        background-color: blue;

      }
    `,
  ],
})

export class MyInnerComponent{
  /*Define updateOuterTotal- the property is an instance of the eventEmitter<number> class and it
  takes part on the updating of the outer total */
  @Output() updateOuterTotal: EventEmitter<number> = new EventEmitter<number>();
  innerTotal: number = 5;


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
