import { Component } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {
  title = 'DoggieHommie';
  
  
  checkoutForm = this.formBuilder.group({
    name: '',
    address: ''
  });
  constructor(
    private formBuilder: FormBuilder,
  ) {}
  
  onSubmit():void{
    console.log("Submitted");
  }  
  
}
