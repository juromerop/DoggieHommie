import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from '../../home/pages/home/home.component';
import { SignupComponent } from '../signup/pages/signup/signup.component';
import { SignupModule } from '../signup/signup.module';
import { RestorePassComponent } from '../restore-pass/pages/restore-pass/restore-pass.component';
import { ProfileModule } from '../profile/profile.module';
import { FeedComponent } from '../feed/pages/feed/feed.component';
import { FeedModule } from '../feed/feed.module';
import { ProfileComponent } from '../profile/pages/profile/profile.component';

const routes: Routes = [
    {
        path: '',
        children: [
          { 
            path: 'signup',
            component: SignupComponent,
            loadChildren: () => import(`../signup/signup.module`).then(m => m.SignupModule)
          },
          { 
            path: 'restore-pass',
            component: RestorePassComponent,
            loadChildren: () => import(`../restore-pass/restore-pass.module`).then(m => m.RestorePassModule)
          },
          { 
            path: 'profile',
            component: ProfileComponent,
            loadChildren: () => import(`../profile/profile.module`).then(m => m.ProfileModule)
          },
          { 
            path: 'feed',
            component: FeedComponent,
            loadChildren: () => import(`../feed/feed.module`).then(m => m.FeedModule)
          },
        ]
      }
]

@NgModule({
    imports: [RouterModule.forChild(routes)],
    exports: [RouterModule]
  })

export class LoginRoutingModule{}