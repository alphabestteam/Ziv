import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  showDetails = false;
  buttonClicks: { timestamp: string }[] = [];

  displayDetails() {
    if (this.showDetails){
      this.showDetails = false;
    }
    else{
      this.showDetails = true;
    }

    this.buttonClicks.push({
      timestamp: this.clickTimestamp()
    });
  }

  clickTimestamp(): string {
    const current_time = new Date();
    return current_time.toString();
  }
}