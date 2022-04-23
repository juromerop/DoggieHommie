import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from '../../home/pages/home/home.component';
import { SignupComponent } from '../signup/pages/signup/signup.component';
import { SignupModule } from '../signup/signup.module';

const routes: Routes = [
    {
        path: '',
        children: [
          { 
            path: 'signup',
            component: SignupComponent,
            loadChildren: () => import(`../signup/signup.module`).then(m => m.SignupModule)
          },
        
        ]
      }
]

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
  })

export class LoginRoutingModule{}