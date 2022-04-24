import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PostComponent } from './components/post/post.component';
import { WhiteBaseComponent } from './components/white-base/white-base.component';
import { HeadbarComponent } from './components/headbar/headbar.component';



@NgModule({
  declarations: [
    PostComponent,
    WhiteBaseComponent,
    HeadbarComponent
  ],
  imports: [
    CommonModule
  ],
  exports: [
    HeadbarComponent
  ]
})
export class SharedModule { }
