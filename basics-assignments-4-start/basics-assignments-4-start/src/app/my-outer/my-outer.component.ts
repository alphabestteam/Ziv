import { Component } from '@angular/core';

@Component({
  selector: 'app-my-outer',
  template: `
    <div class="mat-container mat-mt-3">
      <h3>My Outer Works!</h3>
      <app-my-inner (updateOuterTotal)="updateOuterTotal($event)"></app-my-inner>
      <h3>Outer Total: {{ outerTotal }}</h3>
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
    `,
  ],
})
export class MyOuterComponent {
  outerTotal: number = 0;

  updateOuterTotal(value: number): void {
    this.outerTotal += value;
  }
}
