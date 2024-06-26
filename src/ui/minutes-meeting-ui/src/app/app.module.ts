import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MinutesMeetingOutputComponent } from './minutes-meeting-output/minutes-meeting-output.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MeetingRecordingComponent } from './meeting-recording/meeting-recording.component';
import { SweetAlert2Module } from '@sweetalert2/ngx-sweetalert2';

@NgModule({
  declarations: [
    AppComponent,
    MinutesMeetingOutputComponent,
    MeetingRecordingComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    SweetAlert2Module
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
