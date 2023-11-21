import { Component } from '@angular/core';
import { FILMS } from '../star-wars-fake-db/film-data';
import { StarWarsMovie } from '../app.component'; 

@Component({
  selector: 'app-display-all-movies',
  templateUrl: './display-all-movies.component.html',
  styleUrls: ['./display-all-movies.component.scss']
})
export class DisplayAllMoviesComponent {
  movies: StarWarsMovie[] = FILMS; 
}
