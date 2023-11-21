import { Component } from '@angular/core';
import { FILMS } from './star-wars-fake-db/film-data';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'basics-assignments-5-start';
  opening_crawl = FILMS[0].opening_crawl;
}

export interface StarWarsMovie{
    title: string,
    episode_id: number,
    opening_crawl: string, 
    director: string,
    producer: string,
    release_date: Date
}