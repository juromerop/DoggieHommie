import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/pages/home/home.component';

const routes: Routes = [
  { 
    path: 'home',
    component: HomeComponent,
    loadChildren: () => import(`./home/home.module`).then(m => m.HomeModule),
  },
  {
    path: 'login',
    loadChildren: () => import(`./DoggieHommie/login/login.module`).then(m => m.LoginModule),
  },
  {
    path: '**',
    redirectTo: 'home'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
