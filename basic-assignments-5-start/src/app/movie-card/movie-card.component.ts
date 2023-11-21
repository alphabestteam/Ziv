import { Component, Input } from '@angular/core';
import { StarWarsMovie } from '../app.component';


@Component({
  selector: 'app-movie-card',
  templateUrl: './movie-card.component.html',
  styleUrls: ['./movie-card.component.scss']
})
export class MovieCardComponent {
  @Input() movie!: StarWarsMovie;
}
