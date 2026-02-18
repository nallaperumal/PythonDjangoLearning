import { Component } from '@angular/core';
import { SnackItem } from '../snack-item'

@Component({
  selector: 'app-popcorn',
  imports: [],
  templateUrl: './popcorn.html',
  styleUrl: './popcorn.css',
})
export class Popcorn {
  todaySpecial: SnackItem = new SnackItem('', 0, '');

  ngOnInit(): void {
    this.todaySpecial = new SnackItem('Popcorn', 150, 'https://www.sharmispassions.com/wp-content/uploads/2022/07/popcorn-recipe1.jpg');
  }

}
