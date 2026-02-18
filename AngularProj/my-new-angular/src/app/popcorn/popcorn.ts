import { Component } from '@angular/core';
import { SnackItem } from '../snack-item'

@Component({
  selector: 'app-popcorn',
  imports: [],
  templateUrl: './popcorn.html',
  styleUrl: './popcorn.css',
})
export class Popcorn {
  todaySpecial: SnackItem =  new SnackItem(0, '', 0, '');

  otherItems: SnackItem[] = [
    new SnackItem(2, 'Fruit juice', 120, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXaYzA-Ld5I99hCMQ7nfph7HjJuL2xkb5tRw&s'),
    
    new SnackItem(3, 'Smoothie', 100, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTZ1Bnaj4J6xI4ZUxV36GnU9TdTgqG2Uk-NOQ&s'),
  ];

  ngOnInit(): void {
    this.todaySpecial = new SnackItem(1, 'Popcorn', 150, 'https://www.sharmispassions.com/wp-content/uploads/2022/07/popcorn-recipe1.jpg');
  }

}
