import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MinutesMeetingOutputComponent } from './minutes-meeting-output/minutes-meeting-output.component';
import { MeetingRecordingComponent } from './meeting-recording/meeting-recording.component';

const routes: Routes = [
  { path: 'pdf-generated', component: MinutesMeetingOutputComponent },
  { path: '', component: MeetingRecordingComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
