import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  registrationForm: FormGroup;
  formSubmittedFlag = false;

  constructor(private FormBuilder: FormBuilder) {
    this.registrationForm = this.FormBuilder.group({
      username: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required]
    });
  }

  onSubmit(): void {
    this.formSubmittedFlag = true;
    if (this.registrationForm.valid) {
      console.log(this.registrationForm.value);
    }
    else {
      console.log("The user information is invalid. Here are the issues in the form:")
      Object.keys(this.registrationForm.controls).forEach(field => {
        const control = this.registrationForm.get(field);
        if (control?.invalid) {
          console.log(`Field: ${field}, Errors:`, control.errors);
        }
      });
    }
  }  
  
}
