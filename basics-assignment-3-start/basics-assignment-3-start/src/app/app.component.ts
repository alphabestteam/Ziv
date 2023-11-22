import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  showDetails = false;
  buttonClicks: { timestamp: string }[] = [];

  displayDetails(): void {
    this.showDetails = !this.showDetails;
  
    this.buttonClicks.push({
      timestamp: this.clickTimestamp()
    });
  }

  clickTimestamp(): string {
    const currentTime = new Date();
    return currentTime.toString();
  }
}