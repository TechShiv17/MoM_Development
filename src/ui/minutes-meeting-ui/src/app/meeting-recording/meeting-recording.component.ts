import { Component } from '@angular/core';
import { MeetingMinutesService } from '../services/meeting-minutes.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-meeting-recording',
  templateUrl: './meeting-recording.component.html',
  styleUrls: ['./meeting-recording.component.scss']
})
export class MeetingRecordingComponent {

  constructor(private meetingMinutesService: MeetingMinutesService, private router: Router) { }

  processLink(linkInput: string) {
    if (linkInput) {
      this.meetingMinutesService.convertRecording(linkInput).subscribe(
        (response) => {
          console.log('POST request successful!', response);
          this.router.navigate(["pdf-generated"])
        },
        (error) => {
          console.error('POST request failed!', error);
        }
      );
    }
  }

}
