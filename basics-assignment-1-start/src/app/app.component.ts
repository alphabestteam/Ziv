// app.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  selectedNumber: number = 1;
  numbers: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
  messages: string[] = [];

  onButtonClick(showSuccess: boolean): void {
    let messageArray: string[] = [];
    for(let _ = 0; _ < this.selectedNumber; _++){
      messageArray.push(showSuccess ? 'Success Message' : 'Warning Message')
    }
    this.messages = messageArray;
  }
}
